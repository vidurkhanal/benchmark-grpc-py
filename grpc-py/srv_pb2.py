# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: srv.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tsrv.proto\x12\x06protos\"\x19\n\tFileChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x12\n\x10SimpleSrvRequest\"4\n\x11SimpleSrvRepsonse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t2\xd1\x01\n\x03Srv\x12=\n\x04Ping\x12\x18.protos.SimpleSrvRequest\x1a\x19.protos.SimpleSrvRepsonse\"\x00\x12>\n\nUploadFile\x12\x11.protos.FileChunk\x1a\x19.protos.SimpleSrvRepsonse\"\x00(\x01\x12K\n\x12\x44\x61tabaseStressTest\x12\x18.protos.SimpleSrvRequest\x1a\x19.protos.SimpleSrvRepsonse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'srv_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_FILECHUNK']._serialized_start=21
  _globals['_FILECHUNK']._serialized_end=46
  _globals['_SIMPLESRVREQUEST']._serialized_start=48
  _globals['_SIMPLESRVREQUEST']._serialized_end=66
  _globals['_SIMPLESRVREPSONSE']._serialized_start=68
  _globals['_SIMPLESRVREPSONSE']._serialized_end=120
  _globals['_SRV']._serialized_start=123
  _globals['_SRV']._serialized_end=332
# @@protoc_insertion_point(module_scope)
