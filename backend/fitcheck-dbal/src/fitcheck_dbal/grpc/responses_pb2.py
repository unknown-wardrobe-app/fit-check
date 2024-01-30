# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: responses.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import userdoc_pb2 as userdoc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fresponses.proto\x1a\ruserdoc.proto\"\x87\x01\n\nQueryError\x12)\n\nerror_type\x18\x01 \x01(\x0e\x32\x15.QueryError.ErrorType\x12\x0e\n\x06\x64\x65tail\x18\x02 \x01(\t\">\n\tErrorType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x10\n\x0cNO_SUCH_USER\x10\x01\x12\x0e\n\nINVALID_ID\x10\x02\"\x86\x01\n\x08PutError\x12\'\n\nerror_type\x18\x01 \x01(\x0e\x32\x13.PutError.ErrorType\x12\x0e\n\x06\x64\x65tail\x18\x02 \x01(\t\"A\n\tErrorType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0f\n\x0bSCHEMA_FAIL\x10\x01\x12\x12\n\x0e\x41LREADY_EXISTS\x10\x02\"N\n\x07GetUser\x12\x1d\n\x04user\x18\x01 \x01(\x0b\x32\r.UserDocumentH\x00\x12\x1a\n\x03\x65rr\x18\x02 \x01(\x0b\x32\x0b.QueryErrorH\x00\x42\x08\n\x06result\"T\n\x0b\x43reatedUser\x12!\n\x08new_user\x18\x01 \x01(\x0b\x32\r.UserDocumentH\x00\x12\x18\n\x03\x65rr\x18\x02 \x01(\x0b\x32\t.PutErrorH\x00\x42\x08\n\x06resultb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'responses_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_QUERYERROR']._serialized_start=35
  _globals['_QUERYERROR']._serialized_end=170
  _globals['_QUERYERROR_ERRORTYPE']._serialized_start=108
  _globals['_QUERYERROR_ERRORTYPE']._serialized_end=170
  _globals['_PUTERROR']._serialized_start=173
  _globals['_PUTERROR']._serialized_end=307
  _globals['_PUTERROR_ERRORTYPE']._serialized_start=242
  _globals['_PUTERROR_ERRORTYPE']._serialized_end=307
  _globals['_GETUSER']._serialized_start=309
  _globals['_GETUSER']._serialized_end=387
  _globals['_CREATEDUSER']._serialized_start=389
  _globals['_CREATEDUSER']._serialized_end=473
# @@protoc_insertion_point(module_scope)