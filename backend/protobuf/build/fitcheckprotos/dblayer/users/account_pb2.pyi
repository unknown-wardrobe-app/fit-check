from fitcheckprotos.dblayer import resource_pb2 as _resource_pb2
from fitcheckprotos.dblayer import confirmation_pb2 as _confirmation_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAccount(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class UserId(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _resource_pb2.DocumentIdentifier
    def __init__(self, user: _Optional[_Union[_resource_pb2.DocumentIdentifier, _Mapping]] = ...) -> None: ...

class UpdateAccountUsername(_message.Message):
    __slots__ = ("doc", "new_username")
    DOC_FIELD_NUMBER: _ClassVar[int]
    NEW_USERNAME_FIELD_NUMBER: _ClassVar[int]
    doc: UserId
    new_username: str
    def __init__(self, doc: _Optional[_Union[UserId, _Mapping]] = ..., new_username: _Optional[str] = ...) -> None: ...

class UpdateAccountAvatar(_message.Message):
    __slots__ = ("doc", "new_host", "new_path")
    DOC_FIELD_NUMBER: _ClassVar[int]
    NEW_HOST_FIELD_NUMBER: _ClassVar[int]
    NEW_PATH_FIELD_NUMBER: _ClassVar[int]
    doc: UserId
    new_host: str
    new_path: str
    def __init__(self, doc: _Optional[_Union[UserId, _Mapping]] = ..., new_host: _Optional[str] = ..., new_path: _Optional[str] = ...) -> None: ...

class UpdateAccountPassword(_message.Message):
    __slots__ = ("doc", "new_password")
    DOC_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    doc: UserId
    new_password: str
    def __init__(self, doc: _Optional[_Union[UserId, _Mapping]] = ..., new_password: _Optional[str] = ...) -> None: ...

class BasicAccountDetails(_message.Message):
    __slots__ = ("username", "avatar_host", "avatar_path")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_HOST_FIELD_NUMBER: _ClassVar[int]
    AVATAR_PATH_FIELD_NUMBER: _ClassVar[int]
    username: str
    avatar_host: str
    avatar_path: str
    def __init__(self, username: _Optional[str] = ..., avatar_host: _Optional[str] = ..., avatar_path: _Optional[str] = ...) -> None: ...

class AuthenticationDetails(_message.Message):
    __slots__ = ("password",)
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    password: str
    def __init__(self, password: _Optional[str] = ...) -> None: ...
