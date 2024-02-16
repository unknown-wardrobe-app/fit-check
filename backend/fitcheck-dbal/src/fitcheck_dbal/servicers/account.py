"""
    :module_name: account
    :module_summary: gRPC servicer implementation for account management
    :module_author: Nathan Mendoza
"""

import logging

import pymongo
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


def new_account_error(
        error: Exception,
        request: CreateAccount,
        context: grpc.ServicerContext) -> UserId:
    context.set_code(grpc.StatusCode.UNKNOWN)
    context.set_details(f"Account could not be created: {str(error)}")
    return UserId()


class FitcheckAccountManagementServicer(AccountManagementServicer):
    def __init__(self):
        self._db_client = pymongo.MongoClient(
            "mongodb://127.0.0.1:9000/fitcheck"
        )

    @property
    def db(self):
        """Public reference for the internal mongodb client."""
        return self._db_client

    @safe_callback(errs={
        pymongo.errors.PyMongoError: new_account_error
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
        return UserId(user=DocumentIdentifier(id=str(new_account_id)))

    """
    def UpdateUsername(self, request: UpdateAccountUsername, context) -> ActionCompleted:
        pass

    def UpdatePassword(self, request: UpdateAccountPassword, context) -> ActionCompleted:
        pass

    def UpdateAvatar(self, request: UpdateAccountAvatar, context) -> ActionCompleted:
        pass

    def GetDetails(self, request: UserId, context) -> BasicAccountDetails:
        pass

    def GetAuth(self, request: UserId, context) -> AuthenticationDetails:
        pass

    def CloseAccount(self, request: UserId, context) -> ActionCompleted:
        pass
    """
