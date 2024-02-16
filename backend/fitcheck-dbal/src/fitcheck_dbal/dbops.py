"""
    :module_name: dbops
    :module_summary: a functional approach to database operations
    :module_author: Nathan Mendoza
"""


import pymongo
import bson

import logging
from typing import Callable, Union, Mapping, Any

from .exceptions import NoSuchUser

LOGGER = logging.getLogger(__name__)


def make_user_document_factory(
        client: pymongo.MongoClient,
        username: str,
        password: str) -> Callable[[], bson.ObjectId]:
    """Factory function for creating a new user document in the appp database
    Args:
        client: a mongodb client object
        username: the username of the new user
        password: the (hashed) password of the new user
    Returns:
        callable to actually create the user in the database
    """
    LOGGER.debug(
        "Creating function to create user document with username %s",
        username
    )

    def do_it():
        """Created function that actually creates the user.
        Returns:
            database assigned unique ID for the new user
        **Raises**:
            pymongo.errors.PyMongoError: in the event user creation failes
            #TODO: figure out more specific errors raised
        """
        new_user_doc = {
            'username': username,
            'password': password,
            'avatar': {
                'hostname': '',
                'resource': ''
            },
            'spaces': {
                'default': []
            },
            'custom_sizes': {},
            'custom_fabrics': {}
        }
        LOGGER.debug("Executing user document creation for %s", username)
        return client.fitcheck.users.insert_one(new_user_doc).inserted_id

    return do_it


def update_username(
        client: pymongo.MongoClient,
        userid: Union[str, bson.ObjectId],
        new_username: str) -> Callable[[], None]:
    """Factory function for performing an update to a user's username
    Args:
        client: a mongodb client object
        userid: the document ID of the username to update
        new_username: the replacement username
    Returns:
        callable to actually perform the username update
    """
    LOGGER.debug(
        "Creating function to update user %s's username to %s",
        str(userid),
        new_username
    )

    def do_it():
        """Created function that actually updates the username
        Returns:
            None
        **Raises**:
            pymongo.errors.PyMongoError: in the event username update fails
            bson.errors.InvalidId: in the event the provided ID is invalid
        """
        LOGGER.debug("Executing username update for user %s", str(userid))
        client.fitcheck.users.update_one(
            {"_id": bson.ObjectId(userid) if isinstance(
                userid, str) else userid},
            {"$set": {"username": new_username}}
        )

    return do_it


def update_password(
        client: pymongo.MongoClient,
        userid: Union[str, bson.ObjectId],
        new_password: str) -> Callable[[], None]:
    """Factory function for performing an update to a user's username
    Args:
        client: a mongodb client object
        userid: the document ID of the username to update
        new_password: the replacement (hashed) password
    Returns:
        callable to actually perform the password update
    """
    LOGGER.debug(
        "Creating function to update password of user %s",
        str(userid)
    )

    def do_it():
        """Created function that actually updates the password
        Returns:
            None
        **Raises**:
            pymongo.errors.PyMongoError: in the event username update fails
            bson.errors.InvalidId: in the the event the provided ID is invalid
        """
        LOGGER.debug("Executing password update for user %s", str(userid))
        client.fitcheck.users.update_one(
            {"_id": bson.ObjectId(userid) if isinstance(
                userid, str) else userid},
            {"$set": {"password": new_password}}
        )

    return do_it


def update_avatar(
        client: pymongo.MongoClient,
        userid: Union[str, bson.ObjectId],
        new_avatar_hostname: str,
        new_avatar_path: str) -> Callable[[], None]:
    """Factory function for performing an update to a user's avatar
    Args:
        client: a mongdb client object
        userid: document ID of the user whose avatar to update
        new_avatar_hostname: hostname of the avatar file location
        new_avatar_path: resource path of the avatar file
    Returns:
        callable to perform the avatar update
    """
    LOGGER.debug("Creating function to update avatar of user %s", str(userid))

    def do_it():
        """Created function that actually updates the avatar
        Returns:
            None
        **Raises**:
            pymongo.errors.PyMongoError: in the event that avatar update fails
            bson.errors.InvalidId: in the event the provided ID is invalid
        """
        LOGGER.debug("Executing avatar update for user %s", str(userid))
        client.fitcheck.users.update_one(
            {"_id": bson.ObjectId(userid) if isinstance(
                userid, str) else userid},
            {"$set": {
                "avatar.hostname": new_avatar_hostname,
                "avatar.resource": new_avatar_path
            }}
        )

    return do_it


def get_basic_details(
        client: pymongo.MongoClient,
        userid: Union[str, bson.ObjectId]) -> Callable[[], Mapping[str, Any]]:
    """Factory function for obtaining basic details for a user account
    Args:
        client: a mongodb client object
        userid: the document ID of which user details to obtain
    Returns
        callable to actually retrieve requested information
    """
    LOGGER.debug(
        "Creating function to obtain basic info for user %s",
        str(userid)
    )

    def do_it():
        """Created function that actually obtains basic account details
        Returns:
            projected mapping of basic account details for the requested userid
        **Raises**
            pymongo.errors.PyMongoError: in the event of a database issue
            bson.errors.InvalidId: in the event the provided ID is invalid
            NoSuchUser: in the event a matching user document is not found
        """
        LOGGER.debug(
            "Executing retrieval of basic info for user %s",
            str(userid)
        )
        result = client.fitcheck.users.find_one(
            {"_id": bson.ObjectId(userid) if isinstance(
                userid, str) else userid},
            projection=["username", "avatar.hostname", "avatar.resource"]
        )
        if result:
            return result
        raise NoSuchUser(f"User with ID {str(userid)} does not exist")

    return do_it


def get_auth_details(
        client: pymongo.MongoClient,
        userid: Union[str | bson.ObjectId]) -> Callable[[], Mapping[str, str]]:
    """Factory function for obtaining authentication details for an account
    Args:
        client: a mongodb client object
        userid: the document ID of the user to obtain auth details for
    Returns:
        callable to perform the auth data retrieval
    """
    LOGGER.debug(
        "Creating function to get auth details for user %s",
        str(userid)
    )

    def do_it():
        """Created function to actually retrieve specified user auth details
        Returns:
            the requested account's (hashed) password
        **Raises**
            pymongo.errors.PyMongoError: in the event of a database issue
            bson.errors.InvalidId: in the event the provided ID is invalid
            NoSuchUser: in the event a matching user document is not found
        """
        LOGGER.debug(
            "Executing retrieval of auth details for user %s",
            str(userid)
        )

        result = client.fitcheck.users.find_one(
            {"_id": bson.ObjectId(userid) if isinstance(
                userid, str) else userid},
            projection=["password"]
        )
        if result:
            return result
        raise NoSuchUser(f"User with ID {str(userid)} does not exist")


def delete_user(
        client: pymongo.MongoClient,
        userid: Union[str, bson.ObjectId]) -> Callable[[], None]:
    """Factory function for deleting the request account document
    Args:
        client: a mongodb client object
        userid: the document ID of the user to be deleted
    Returns:
        callable to perform the deletion
    """
    LOGGER.debug("Creating function to delete user %s", str(userid))

    def do_it():
        """Created function to actually delete the user
        Returns:
            None
        **Raises**:
            pymongo.errors.PyMongoError: in the event of a database issue
            bson.errors.InvalidId: in the event the provided ID is invalid
            NoSuchUser: in the event a matching user document is not found
        """
        LOGGER.debug("Deleting user %s", str(userid))
        result = client.fitcheck.users.delete_one(
            {"_id": bson.ObjectId(userid) if isinstance(
                userid, str) else userid}
        )
        if result.deleted_count != 1:
            raise NoSuchUser(
                f"User {str(userid)} does not exist"
            )
