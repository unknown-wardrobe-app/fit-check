from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserDocument(_message.Message):
    __slots__ = ("userid", "username", "password", "created_at")
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    userid: str
    username: str
    password: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, userid: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class QueryForUser(_message.Message):
    __slots__ = ("userid",)
    USERID_FIELD_NUMBER: _ClassVar[int]
    userid: str
    def __init__(self, userid: _Optional[str] = ...) -> None: ...

class NewUser(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class QueryError(_message.Message):
    __slots__ = ("error_type", "detail")
    class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[QueryError.ErrorType]
        NO_SUCH_USER: _ClassVar[QueryError.ErrorType]
        INVALID_ID: _ClassVar[QueryError.ErrorType]
    UNSPECIFIED: QueryError.ErrorType
    NO_SUCH_USER: QueryError.ErrorType
    INVALID_ID: QueryError.ErrorType
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    error_type: QueryError.ErrorType
    detail: str
    def __init__(self, error_type: _Optional[_Union[QueryError.ErrorType, str]] = ..., detail: _Optional[str] = ...) -> None: ...

class PutError(_message.Message):
    __slots__ = ("error_type", "detail")
    class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PutError.ErrorType]
        SCHEMA_FAIL: _ClassVar[PutError.ErrorType]
        ALREADY_EXISTS: _ClassVar[PutError.ErrorType]
    UNSPECIFIED: PutError.ErrorType
    SCHEMA_FAIL: PutError.ErrorType
    ALREADY_EXISTS: PutError.ErrorType
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    error_type: PutError.ErrorType
    detail: str
    def __init__(self, error_type: _Optional[_Union[PutError.ErrorType, str]] = ..., detail: _Optional[str] = ...) -> None: ...

class GetUser(_message.Message):
    __slots__ = ("user", "err")
    USER_FIELD_NUMBER: _ClassVar[int]
    ERR_FIELD_NUMBER: _ClassVar[int]
    user: UserDocument
    err: QueryError
    def __init__(self, user: _Optional[_Union[UserDocument, _Mapping]] = ..., err: _Optional[_Union[QueryError, _Mapping]] = ...) -> None: ...

class CreatedUser(_message.Message):
    __slots__ = ("new_user", "err")
    NEW_USER_FIELD_NUMBER: _ClassVar[int]
    ERR_FIELD_NUMBER: _ClassVar[int]
    new_user: UserDocument
    err: PutError
    def __init__(self, new_user: _Optional[_Union[UserDocument, _Mapping]] = ..., err: _Optional[_Union[PutError, _Mapping]] = ...) -> None: ...
