# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: content.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'content.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcontent.proto\x12\x07\x63ontent\"5\n\x0fRegisterRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"E\n\x10RegisterResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\"$\n\x11SubmissionRequest\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\"6\n\rReviewRequest\x12\x15\n\rsubmission_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"\xb2\x01\n\nSubmission\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x12\n\ncreated_at\x18\x05 \x01(\t\x12\x18\n\x0breviewed_by\x18\x06 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0breviewed_at\x18\x07 \x01(\tH\x01\x88\x01\x01\x42\x0e\n\x0c_reviewed_byB\x0e\n\x0c_reviewed_at2\xdb\x01\n\x0e\x43ontentService\x12\x43\n\x0cRegisterUser\x12\x18.content.RegisterRequest\x1a\x19.content.RegisterResponse\x12\x43\n\x10\x43reateSubmission\x12\x1a.content.SubmissionRequest\x1a\x13.content.Submission\x12?\n\x10ReviewSubmission\x12\x16.content.ReviewRequest\x1a\x13.content.Submissionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'content_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REGISTERREQUEST']._serialized_start=26
  _globals['_REGISTERREQUEST']._serialized_end=79
  _globals['_REGISTERRESPONSE']._serialized_start=81
  _globals['_REGISTERRESPONSE']._serialized_end=150
  _globals['_SUBMISSIONREQUEST']._serialized_start=152
  _globals['_SUBMISSIONREQUEST']._serialized_end=188
  _globals['_REVIEWREQUEST']._serialized_start=190
  _globals['_REVIEWREQUEST']._serialized_end=244
  _globals['_SUBMISSION']._serialized_start=247
  _globals['_SUBMISSION']._serialized_end=425
  _globals['_CONTENTSERVICE']._serialized_start=428
  _globals['_CONTENTSERVICE']._serialized_end=647
# @@protoc_insertion_point(module_scope)
