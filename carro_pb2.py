# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: carro.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x63\x61rro.proto\x12\x05\x63\x61rro\".\n\x0c\x43\x61rroRequest\x12\r\n\x05placa\x18\x01 \x01(\t\x12\x0f\n\x07renavan\x18\x02 \x01(\t\";\n\rCarroResponse\x12\x15\n\rcodigo_barras\x18\x01 \x01(\t\x12\x13\n\x0bvalor_total\x18\x02 \x01(\x02\x32Q\n\x0c\x43\x61rroService\x12\x41\n\x12\x63\x61lcularValorTotal\x12\x13.carro.CarroRequest\x1a\x14.carro.CarroResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'carro_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CARROREQUEST._serialized_start=22
  _CARROREQUEST._serialized_end=68
  _CARRORESPONSE._serialized_start=70
  _CARRORESPONSE._serialized_end=129
  _CARROSERVICE._serialized_start=131
  _CARROSERVICE._serialized_end=212
# @@protoc_insertion_point(module_scope)
