from fitcheckprotos.dblayer import confirmation_pb2 as _confirmation_pb2
from fitcheckprotos.dblayer import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserDefinedSize(_message.Message):
    __slots__ = ("size_name", "size_value")
    SIZE_NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_VALUE_FIELD_NUMBER: _ClassVar[int]
    size_name: str
    size_value: str
    def __init__(self, size_name: _Optional[str] = ..., size_value: _Optional[str] = ...) -> None: ...

class UserDefinedFabric(_message.Message):
    __slots__ = ("fabric_name", "materials")
    class MaterialsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    FABRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    MATERIALS_FIELD_NUMBER: _ClassVar[int]
    fabric_name: str
    materials: _containers.ScalarMap[str, int]
    def __init__(self, fabric_name: _Optional[str] = ..., materials: _Optional[_Mapping[str, int]] = ...) -> None: ...

class ListUserSizes(_message.Message):
    __slots__ = ("sizes",)
    SIZES_FIELD_NUMBER: _ClassVar[int]
    sizes: _containers.RepeatedCompositeFieldContainer[UserDefinedSize]
    def __init__(self, sizes: _Optional[_Iterable[_Union[UserDefinedSize, _Mapping]]] = ...) -> None: ...

class ListUserFabrics(_message.Message):
    __slots__ = ("fabrics",)
    FABRICS_FIELD_NUMBER: _ClassVar[int]
    fabrics: _containers.RepeatedCompositeFieldContainer[UserDefinedFabric]
    def __init__(self, fabrics: _Optional[_Iterable[_Union[UserDefinedFabric, _Mapping]]] = ...) -> None: ...
