# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import util_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='partnerCompleteCommitRequest.proto',
  package='',
  serialized_pb='\n\"partnerCompleteCommitRequest.proto\x1a\nutil.proto\"9\n\x1cPartnerCompleteCommitRequest\x12\x19\n\nevent_uuid\x18\x01 \x02(\x0b\x32\x05.UUID')




_PARTNERCOMPLETECOMMITREQUEST = descriptor.Descriptor(
  name='PartnerCompleteCommitRequest',
  full_name='PartnerCompleteCommitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='event_uuid', full_name='PartnerCompleteCommitRequest.event_uuid', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=50,
  serialized_end=107,
)

_PARTNERCOMPLETECOMMITREQUEST.fields_by_name['event_uuid'].message_type = util_pb2._UUID
DESCRIPTOR.message_types_by_name['PartnerCompleteCommitRequest'] = _PARTNERCOMPLETECOMMITREQUEST

class PartnerCompleteCommitRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PARTNERCOMPLETECOMMITREQUEST
  
  # @@protoc_insertion_point(class_scope:PartnerCompleteCommitRequest)

# @@protoc_insertion_point(module_scope)
