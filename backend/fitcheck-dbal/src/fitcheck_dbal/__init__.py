"""
    :module_name: fitcheck_dbal
    :module_summary: A database access layer for the fitcheck backend
    :module_author: Nathan Mendoza
"""

import pymongo
from bson import ObjectId

from dbal_pb2 import CreatedUser, GetUser, QueryError, PutError, UserDocument
from dbal_pb2_grpc import UserDocumentServiceServicer


class UserDocumentController(UserDocumentServiceServicer):

    def __init__(self):
        self._db = pymongo.MongoClient("mongodb://127.0.0.1:9000/fitcheck")

    def GetUserDocument(self, request, context) -> GetUser:
        try:
            result = self._db.fitcheck.users.find_one(
                {"_id": ObjectId(request.userid)}
            )
            if result:
                return GetUser(user=UserDocument(
                    userid=str(result['_id']),
                    username=result['username'],
                    password=result['password']
                ))
            return GetUser(
                err=QueryError.ErrorType.NO_SUCH_USER,
                detail=f'No such user with ID: {request.userid}'
            )
        except pymongo.errors.PyMongoError as e:
            return GetUser(err=QueryError(
                error_type=QueryError.ErrorType.UNSPECIFIED,
                detail=str(e)
            ))

    def CreateUserDocument(self, request, context) -> CreatedUser:
        try:
            result = self._db.fitcheck.users.insert_one({
                "username": request.username,
                "password": request.password
            })
            return CreatedUser(new_user=UserDocument(
                userid=str(result.inserted_id),
                username=request.username,
                password=request.password
            ))
        except pymongo.errors.PyMongoError as e:
            return CreatedUser(err=PutError(
                error_type=PutError.ErrorType.UNSPECIFIED,
                detail=str(e)
            ))
