from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ActionCompleted(_message.Message):
    __slots__ = ("complete",)
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    complete: bool
    def __init__(self, complete: bool = ...) -> None: ...

class CollectionModified(_message.Message):
    __slots__ = ("item_count",)
    ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    item_count: int
    def __init__(self, item_count: _Optional[int] = ...) -> None: ...
