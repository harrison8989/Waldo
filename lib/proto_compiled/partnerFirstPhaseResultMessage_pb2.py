# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import util_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='partnerFirstPhaseResultMessage.proto',
  package='',
  serialized_pb='\n$partnerFirstPhaseResultMessage.proto\x1a\nutil.proto\"\xa3\x01\n\x1ePartnerFirstPhaseResultMessage\x12\x19\n\nevent_uuid\x18\x01 \x02(\x0b\x32\x05.UUID\x12$\n\x15sending_endpoint_uuid\x18\x02 \x02(\x0b\x32\x05.UUID\x12\x12\n\nsuccessful\x18\x03 \x02(\x08\x12,\n\x1d\x63hildren_event_endpoint_uuids\x18\x04 \x03(\x0b\x32\x05.UUID')




_PARTNERFIRSTPHASERESULTMESSAGE = descriptor.Descriptor(
  name='PartnerFirstPhaseResultMessage',
  full_name='PartnerFirstPhaseResultMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='event_uuid', full_name='PartnerFirstPhaseResultMessage.event_uuid', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sending_endpoint_uuid', full_name='PartnerFirstPhaseResultMessage.sending_endpoint_uuid', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='successful', full_name='PartnerFirstPhaseResultMessage.successful', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='children_event_endpoint_uuids', full_name='PartnerFirstPhaseResultMessage.children_event_endpoint_uuids', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=53,
  serialized_end=216,
)

_PARTNERFIRSTPHASERESULTMESSAGE.fields_by_name['event_uuid'].message_type = util_pb2._UUID
_PARTNERFIRSTPHASERESULTMESSAGE.fields_by_name['sending_endpoint_uuid'].message_type = util_pb2._UUID
_PARTNERFIRSTPHASERESULTMESSAGE.fields_by_name['children_event_endpoint_uuids'].message_type = util_pb2._UUID
DESCRIPTOR.message_types_by_name['PartnerFirstPhaseResultMessage'] = _PARTNERFIRSTPHASERESULTMESSAGE

class PartnerFirstPhaseResultMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PARTNERFIRSTPHASERESULTMESSAGE
  
  # @@protoc_insertion_point(class_scope:PartnerFirstPhaseResultMessage)

# @@protoc_insertion_point(module_scope)
