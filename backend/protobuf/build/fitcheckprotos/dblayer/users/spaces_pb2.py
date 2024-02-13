# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fitcheckprotos/dblayer/users/spaces.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fitcheckprotos.dblayer import confirmation_pb2 as fitcheckprotos_dot_dblayer_dot_confirmation__pb2
from fitcheckprotos.dblayer.users import account_pb2 as fitcheckprotos_dot_dblayer_dot_users_dot_account__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)fitcheckprotos/dblayer/users/spaces.proto\x12\x1c\x66itcheckprotos.dblayer.users\x1a)fitcheckprotos/dblayer/confirmation.proto\x1a*fitcheckprotos/dblayer/users/account.proto\"W\n\x0e\x43reateNewSpace\x12\x31\n\x03\x64oc\x18\x01 \x01(\x0b\x32$.fitcheckprotos.dblayer.users.UserId\x12\x12\n\nspace_name\x18\x02 \x01(\t\"T\n\x0b\x44\x65leteSpace\x12\x31\n\x03\x64oc\x18\x01 \x01(\x0b\x32$.fitcheckprotos.dblayer.users.UserId\x12\x12\n\nspace_name\x18\x02 \x01(\t\"h\n\x0e\x41\x64\x64ItemToSpace\x12\x31\n\x03\x64oc\x18\x01 \x01(\x0b\x32$.fitcheckprotos.dblayer.users.UserId\x12\x12\n\nspace_name\x18\x02 \x01(\t\x12\x0f\n\x07item_id\x18\x03 \x01(\t\"m\n\x13RemoveItemFromSpace\x12\x31\n\x03\x64oc\x18\x01 \x01(\x0b\x32$.fitcheckprotos.dblayer.users.UserId\x12\x12\n\nspace_name\x18\x02 \x01(\t\x12\x0f\n\x07item_id\x18\x03 \x01(\t2\xa6\x03\n\x0fSpaceManagement\x12\x61\n\x08NewSpace\x12,.fitcheckprotos.dblayer.users.CreateNewSpace\x1a\'.fitcheckprotos.dblayer.ActionCompleted\x12`\n\nCloseSpace\x12).fitcheckprotos.dblayer.users.DeleteSpace\x1a\'.fitcheckprotos.dblayer.ActionCompleted\x12\x63\n\x07PutItem\x12,.fitcheckprotos.dblayer.users.AddItemToSpace\x1a*.fitcheckprotos.dblayer.CollectionModified\x12i\n\x08TakeItem\x12\x31.fitcheckprotos.dblayer.users.RemoveItemFromSpace\x1a*.fitcheckprotos.dblayer.CollectionModifiedb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fitcheckprotos.dblayer.users.spaces_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CREATENEWSPACE']._serialized_start=162
  _globals['_CREATENEWSPACE']._serialized_end=249
  _globals['_DELETESPACE']._serialized_start=251
  _globals['_DELETESPACE']._serialized_end=335
  _globals['_ADDITEMTOSPACE']._serialized_start=337
  _globals['_ADDITEMTOSPACE']._serialized_end=441
  _globals['_REMOVEITEMFROMSPACE']._serialized_start=443
  _globals['_REMOVEITEMFROMSPACE']._serialized_end=552
  _globals['_SPACEMANAGEMENT']._serialized_start=555
  _globals['_SPACEMANAGEMENT']._serialized_end=977
# @@protoc_insertion_point(module_scope)
