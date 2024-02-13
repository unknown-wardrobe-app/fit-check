from fitcheckprotos.dblayer import confirmation_pb2 as _confirmation_pb2
from fitcheckprotos.dblayer.users import account_pb2 as _account_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateNewSpace(_message.Message):
    __slots__ = ("doc", "space_name")
    DOC_FIELD_NUMBER: _ClassVar[int]
    SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    doc: _account_pb2.UserId
    space_name: str
    def __init__(self, doc: _Optional[_Union[_account_pb2.UserId, _Mapping]] = ..., space_name: _Optional[str] = ...) -> None: ...

class DeleteSpace(_message.Message):
    __slots__ = ("doc", "space_name")
    DOC_FIELD_NUMBER: _ClassVar[int]
    SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    doc: _account_pb2.UserId
    space_name: str
    def __init__(self, doc: _Optional[_Union[_account_pb2.UserId, _Mapping]] = ..., space_name: _Optional[str] = ...) -> None: ...

class AddItemToSpace(_message.Message):
    __slots__ = ("doc", "space_name", "item_id")
    DOC_FIELD_NUMBER: _ClassVar[int]
    SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    doc: _account_pb2.UserId
    space_name: str
    item_id: str
    def __init__(self, doc: _Optional[_Union[_account_pb2.UserId, _Mapping]] = ..., space_name: _Optional[str] = ..., item_id: _Optional[str] = ...) -> None: ...

class RemoveItemFromSpace(_message.Message):
    __slots__ = ("doc", "space_name", "item_id")
    DOC_FIELD_NUMBER: _ClassVar[int]
    SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    doc: _account_pb2.UserId
    space_name: str
    item_id: str
    def __init__(self, doc: _Optional[_Union[_account_pb2.UserId, _Mapping]] = ..., space_name: _Optional[str] = ..., item_id: _Optional[str] = ...) -> None: ...
