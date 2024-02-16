"""
    :module_name: account
    :module_summary: gRPC servicer implementation for account management
    :module_author: Nathan Mendoza
"""

import logging
from typing import Union

from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.errors import InvalidId
import grpc
from fitcheckprotos.dblayer.users.account_pb2 import (
    CreateAccount,
    BasicAccountDetails,
    AuthenticationDetails,
    UpdateAccountAvatar,
    UpdateAccountPassword,
    UpdateAccountUsername,
    UserId
)
from fitcheckprotos.dblayer.confirmation_pb2 import ActionCompleted
from fitcheckprotos.dblayer.resource_pb2 import DocumentIdentifier

from fitcheckprotos.dblayer.users.account_pb2_grpc import AccountManagementServicer


from ..dbops import (
    make_user_document_factory,
    update_username,
    update_password,
    update_avatar,
    get_auth_details,
    get_basic_details,
    delete_user
)
from ..exceptions import (
    safe_callback,
    NoSuchUser
)

LOGGER = logging.getLogger(__name__)


class AccountManagementErrorCallback:

    @staticmethod
    def new_account_error(
            error: Exception,
            request: CreateAccount,
            context: grpc.ServicerContext) -> UserId:
        context.set_code(grpc.StatusCode.UNKNOWN)
        context.set_details(f"Account could not be created: {str(error)}")
        LOGGER.error("Account not created")
        return UserId()

    @staticmethod
    def update_username_error(
            error: Exception,
            request: UpdateAccountUsername,
            context: grpc.ServicerContext) -> ActionCompleted:
        context.set_code(grpc.StatusCode.UNKNOWN)
        context.set_details(
            f"Acount username could not be updated: {str(error)}"
        )
        LOGGER.error("Username not updated")
        return ActionCompleted(complete=False)

    @staticmethod
    def update_password_error(
        error: Exception,
        request: UpdateAccountPassword,
        context: grpc.ServicerContext
    ) -> ActionCompleted:
        context.set_code(grpc.StatusCode.UNKNOWN)
        context.set_details(
            f"Account password could not be updated: {str(error)}"
        )
        LOGGER.error("Password not updated")
        return ActionCompleted(complete=False)

    @staticmethod
    def update_avatar_error(
        error: Exception,
        request: UpdateAccountAvatar,
        context: grpc.ServicerContext
    ) -> ActionCompleted:
        context.set_code(grpc.StatusCode.UNKNOWN)
        context.set_details(
            f"Account avatar could not be updated: {str(error)}"
        )
        LOGGER.error("Avatar not updated")
        return ActionCompleted(complete=False)

    @staticmethod
    def find_user_error(
        error: Exception,
        request: UserId,
        context: grpc.ServicerContext
    ) -> BasicAccountDetails:
        context.set_code(grpc.StatusCode.UNKNOWN)
        context.set_details(
            f"Account information could not be retrieved: {str(error)}"
        )
        LOGGER.error("User information not retrieved")
        return BasicAccountDetails()

    @staticmethod
    def user_not_found(
        error: Exception,
        request: UserId,
        context: grpc.ServicerContext
    ) -> BasicAccountDetails:
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details(
            f"No user with ID: {request.user.id}"
        )
        LOGGER.error("User does not exist")
        return BasicAccountDetails()

    @staticmethod
    def user_cannot_auth(
        error: Exception,
        request: UserId,
        context: grpc.ServicerContext
    ) -> AuthenticationDetails:
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details(
            f"No user with ID: {request.user.id}"
        )
        LOGGER.error("User does not exist")
        return AuthenticationDetails()

    @staticmethod
    def user_not_deleted(
        error: Exception,
        request: UserId,
        context: grpc.ServicerContext
    ) -> ActionCompleted:
        context.set_code(grpc.StatusCode.UNKNOWN)
        context.set_details(
            f"Failed to delete user {request.user.id}: {str(error)}"
        )
        LOGGER.error("User not deleted")
        return ActionCompleted(complete=False)

    @staticmethod
    def invalid_id_argument(
        error: Exception,
        request: Union[
            UserId,
            UpdateAccountUsername,
            UpdateAccountAvatar,
            UpdateAccountPassword
        ],
        context: grpc.ServicerContext
    ) -> ActionCompleted:
        provided_id = request.user.id if isinstance(
            request, UserId) else request.doc.user.id
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.set_details(f"Invalid ID argument: {provided_id}")
        LOGGER.error("Provided ID is not valid")
        return ActionCompleted(complete=False)


class FitcheckAccountManagementServicer(AccountManagementServicer):
    def __init__(self):
        self._db_client = MongoClient(
            "mongodb://127.0.0.1:9000/fitcheck"
        )

    @property
    def db(self):
        """Public reference for the internal mongodb client."""
        return self._db_client

    @safe_callback(errs={
        PyMongoError: AccountManagementErrorCallback.new_account_error,
    })
    def NewAccount(
        self,
        request: CreateAccount,
        context: grpc.ServicerContext
    ) -> UserId:
        make_new_account = make_user_document_factory(
            self.db,
            request.username,
            request.password
        )

        new_account_id = make_new_account()
        LOGGER.info("Created new account with ID: %s", str(new_account_id))
        return UserId(user=DocumentIdentifier(id=str(new_account_id)))

    @safe_callback(errs={
        PyMongoError: AccountManagementErrorCallback.update_username_error,
        InvalidId: AccountManagementErrorCallback.invalid_id_argument
    })
    def UpdateUsername(
        self,
        request: UpdateAccountUsername,
        context: grpc.ServicerContext
    ) -> ActionCompleted:
        LOGGER.info("Update username for user %s", request.doc.user.id)
        do_username_update = update_username(
            self.db,
            request.doc.user.id,
            request.new_username
        )
        do_username_update()
        return ActionCompleted(complete=True)

    @safe_callback(errs={
        PyMongoError: AccountManagementErrorCallback.update_password_error,
        InvalidId: AccountManagementErrorCallback.invalid_id_argument
    })
    def UpdatePassword(
        self,
        request: UpdateAccountPassword,
        context: grpc.ServicerContext
    ) -> ActionCompleted:
        LOGGER.info("Update passwor for user %s", request.doc.user.id)
        do_password_update = update_password(
            self.db,
            request.doc.user.id,
            request.new_password
        )
        do_password_update()
        return ActionCompleted(complete=True)

    @safe_callback(errs={
        PyMongoError: AccountManagementErrorCallback.update_avatar_error,
        InvalidId: AccountManagementErrorCallback.invalid_id_argument
    })
    def UpdateAvatar(
        self,
        request: UpdateAccountAvatar,
        context: grpc.ServicerContext
    ) -> ActionCompleted:
        LOGGER.info("Update avatar for user %s", request.doc.user.id)
        do_avatar_update = update_avatar(
            self.db,
            request.doc.user.id,
            request.new_host,
            request.new_path
        )
        do_avatar_update()
        return ActionCompleted(complete=True)

    @safe_callback(errs={
        PyMongoError: AccountManagementErrorCallback.find_user_error,
        InvalidId: AccountManagementErrorCallback.find_user_error,
        NoSuchUser: AccountManagementErrorCallback.user_cannot_auth
    })
    def GetDetails(
        self,
        request: UserId,
        context: grpc.ServicerContext
    ) -> BasicAccountDetails:
        LOGGER.info("Looking up basic details for user: %s", request.user.id)
        account_details = get_basic_details(
            self.db,
            request.user.id
        )()
        return BasicAccountDetails(
            username=account_details['username'],
            avatar_host=account_details['avatar']['hostname'],
            avatar_path=account_details['avatar']['resource']
        )

    @safe_callback(errs={
        PyMongoError: AccountManagementErrorCallback.user_cannot_auth,
        InvalidId: AccountManagementErrorCallback.user_cannot_auth,
        NoSuchUser: AccountManagementErrorCallback.user_cannot_auth
    })
    def GetAuth(
        self,
        request: UserId,
        context: grpc.ServicerContext
    ) -> AuthenticationDetails:
        LOGGER.info("Looking up auth details for user: %s", request.user.id)
        auth_details = get_auth_details(
            self.db,
            request.user.id
        )()
        return AuthenticationDetails(
            password=auth_details['password']
        )

    @safe_callback(errs={
        PyMongoError: AccountManagementErrorCallback.user_not_deleted,
        InvalidId: AccountManagementErrorCallback.invalid_id_argument,
        NoSuchUser: AccountManagementErrorCallback.invalid_id_argument
    })
    def CloseAccount(
        self,
        request: UserId,
        context: grpc.ServicerContext
    ) -> ActionCompleted:
        do_delete_account = delete_user(
            self.db,
            request.user.id
        )
        LOGGER.info("Deleting account: %s", request.user.id)
        do_delete_account()
        return ActionCompleted(complete=True)
