# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto_acdfg.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto_acdfg.proto',
  package='edu.colorado.plv.fixr.protobuf',
  syntax='proto2',
  serialized_pb=_b('\n\x11proto_acdfg.proto\x12\x1e\x65\x64u.colorado.plv.fixr.protobuf\"\xf5\x0e\n\x05\x41\x63\x64\x66g\x12\x41\n\tdata_node\x18\x01 \x03(\x0b\x32..edu.colorado.plv.fixr.protobuf.Acdfg.DataNode\x12\x41\n\tmisc_node\x18\x02 \x03(\x0b\x32..edu.colorado.plv.fixr.protobuf.Acdfg.MiscNode\x12\x45\n\x0bmethod_node\x18\x03 \x03(\x0b\x32\x30.edu.colorado.plv.fixr.protobuf.Acdfg.MethodNode\x12G\n\x0c\x63ontrol_edge\x18\x04 \x03(\x0b\x32\x31.edu.colorado.plv.fixr.protobuf.Acdfg.ControlEdge\x12?\n\x08\x64\x65\x66_edge\x18\x05 \x03(\x0b\x32-.edu.colorado.plv.fixr.protobuf.Acdfg.DefEdge\x12?\n\x08use_edge\x18\x06 \x03(\x0b\x32-.edu.colorado.plv.fixr.protobuf.Acdfg.UseEdge\x12\x43\n\ntrans_edge\x18\x07 \x03(\x0b\x32/.edu.colorado.plv.fixr.protobuf.Acdfg.TransEdge\x12V\n\x10\x65xceptional_edge\x18\x0c \x03(\x0b\x32<.edu.colorado.plv.fixr.protobuf.Acdfg.ExceptionalControlEdge\x12\x43\n\x0b\x65\x64ge_labels\x18\x0b \x03(\x0b\x32..edu.colorado.plv.fixr.protobuf.Acdfg.LabelMap\x12?\n\x08repo_tag\x18\x08 \x01(\x0b\x32-.edu.colorado.plv.fixr.protobuf.Acdfg.RepoTag\x12\x45\n\x0bsource_info\x18\n \x01(\x0b\x32\x30.edu.colorado.plv.fixr.protobuf.Acdfg.SourceInfo\x12\x17\n\x0fprovenance_path\x18\r \x01(\t\x12\x43\n\nmethod_bag\x18\t \x01(\x0b\x32/.edu.colorado.plv.fixr.protobuf.Acdfg.MethodBag\x1a\xa8\x01\n\x08\x44\x61taNode\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x0c\n\x04type\x18\x03 \x02(\t\x12J\n\tdata_type\x18\x04 \x01(\x0e\x32\x37.edu.colorado.plv.fixr.protobuf.Acdfg.DataNode.DataType\"(\n\x08\x44\x61taType\x12\x0c\n\x08\x44\x41TA_VAR\x10\x00\x12\x0e\n\nDATA_CONST\x10\x01\x1a\x16\n\x08MiscNode\x12\n\n\x02id\x18\x01 \x02(\x04\x1a[\n\nMethodNode\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x10\n\x08\x61ssignee\x18\x05 \x01(\x04\x12\x0f\n\x07invokee\x18\x02 \x01(\x04\x12\x0c\n\x04name\x18\x03 \x02(\t\x12\x10\n\x08\x61rgument\x18\x04 \x03(\x04\x1a\x33\n\x0b\x43ontrolEdge\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x0c\n\x04\x66rom\x18\x02 \x02(\x04\x12\n\n\x02to\x18\x03 \x02(\x04\x1a/\n\x07\x44\x65\x66\x45\x64ge\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x0c\n\x04\x66rom\x18\x02 \x02(\x04\x12\n\n\x02to\x18\x03 \x02(\x04\x1a/\n\x07UseEdge\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x0c\n\x04\x66rom\x18\x02 \x02(\x04\x12\n\n\x02to\x18\x03 \x02(\x04\x1a\x31\n\tTransEdge\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x0c\n\x04\x66rom\x18\x02 \x02(\x04\x12\n\n\x02to\x18\x03 \x02(\x04\x1aR\n\x16\x45xceptionalControlEdge\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x0c\n\x04\x66rom\x18\x02 \x02(\x04\x12\n\n\x02to\x18\x03 \x02(\x04\x12\x12\n\nexceptions\x18\x04 \x03(\t\x1a\\\n\x08LabelMap\x12\x0f\n\x07\x65\x64ge_id\x18\x01 \x02(\x04\x12?\n\x06labels\x18\x02 \x03(\x0e\x32/.edu.colorado.plv.fixr.protobuf.Acdfg.EdgeLabel\x1a\x66\n\x07RepoTag\x12\x11\n\trepo_name\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x13\n\x0b\x63ommit_hash\x18\x04 \x01(\t\x12\x13\n\x0b\x63ommit_date\x18\x05 \x01(\t\x1a\x1b\n\tMethodBag\x12\x0e\n\x06method\x18\x01 \x03(\t\x1a\xbc\x01\n\nSourceInfo\x12\x14\n\x0cpackage_name\x18\x01 \x01(\t\x12\x12\n\nclass_name\x18\x02 \x01(\t\x12\x13\n\x0bmethod_name\x18\x03 \x01(\t\x12\x19\n\x11\x63lass_line_number\x18\x04 \x01(\r\x12\x1a\n\x12method_line_number\x18\x05 \x01(\r\x12\x19\n\x11source_class_name\x18\x06 \x01(\t\x12\x1d\n\x15\x61\x62s_source_class_name\x18\x07 \x01(\t\",\n\tEdgeLabel\x12\x0c\n\x08\x44OMINATE\x10\x00\x12\x11\n\rPOSTDOMINATED\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ACDFG_DATANODE_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='edu.colorado.plv.fixr.protobuf.Acdfg.DataNode.DataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DATA_VAR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_CONST', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1056,
  serialized_end=1096,
)
_sym_db.RegisterEnumDescriptor(_ACDFG_DATANODE_DATATYPE)

_ACDFG_EDGELABEL = _descriptor.EnumDescriptor(
  name='EdgeLabel',
  full_name='edu.colorado.plv.fixr.protobuf.Acdfg.EdgeLabel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DOMINATE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSTDOMINATED', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1919,
  serialized_end=1963,
)
_sym_db.RegisterEnumDescriptor(_ACDFG_EDGELABEL)


_ACDFG_DATANODE = _descriptor.Descriptor(
  name='DataNode',
  full_name='edu.colorado.plv.fixr.protobuf.Acdfg.DataNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.DataNode.id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.DataNode.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.DataNode.type', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.DataNode.data_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACDFG_DATANODE_DATATYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=928,
  serialized_end=1096,
)

_ACDFG_MISCNODE = _descriptor.Descriptor(
  name='MiscNode',
  full_name='edu.colorado.plv.fixr.protobuf.Acdfg.MiscNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.MiscNode.id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1098,
  serialized_end=1120,
)

_ACDFG_METHODNODE = _descriptor.Descriptor(
  name='MethodNode',
  full_name='edu.colorado.plv.fixr.protobuf.Acdfg.MethodNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.MethodNode.id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assignee', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.MethodNode.assignee', index=1,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='invokee', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.MethodNode.invokee', index=2,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.MethodNode.name', index=3,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='argument', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.MethodNode.argument', index=4,
      number=4, type=4, cpp_type=4, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1122,
  serialized_end=1213,
)

_ACDFG_CONTROLEDGE = _descriptor.Descriptor(
  name='ControlEdge',
  full_name='edu.colorado.plv.fixr.protobuf.Acdfg.ControlEdge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.ControlEdge.id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.ControlEdge.from', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.ControlEdge.to', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1215,
  serialized_end=1266,
)

_ACDFG_DEFEDGE = _descriptor.Descriptor(
  name='DefEdge',
  full_name='edu.colorado.plv.fixr.protobuf.Acdfg.DefEdge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.DefEdge.id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.DefEdge.from', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.DefEdge.to', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1268,
  serialized_end=1315,
)

_ACDFG_USEEDGE = _descriptor.Descriptor(
  name='UseEdge',
  full_name='edu.colorado.plv.fixr.protobuf.Acdfg.UseEdge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.UseEdge.id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.UseEdge.from', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.UseEdge.to', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1317,
  serialized_end=1364,
)

_ACDFG_TRANSEDGE = _descriptor.Descriptor(
  name='TransEdge',
  full_name='edu.colorado.plv.fixr.protobuf.Acdfg.TransEdge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.TransEdge.id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.TransEdge.from', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.TransEdge.to', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1366,
  serialized_end=1415,
)

_ACDFG_EXCEPTIONALCONTROLEDGE = _descriptor.Descriptor(
  name='ExceptionalControlEdge',
  full_name='edu.colorado.plv.fixr.protobuf.Acdfg.ExceptionalControlEdge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.ExceptionalControlEdge.id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.ExceptionalControlEdge.from', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.ExceptionalControlEdge.to', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exceptions', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.ExceptionalControlEdge.exceptions', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1417,
  serialized_end=1499,
)

_ACDFG_LABELMAP = _descriptor.Descriptor(
  name='LabelMap',
  full_name='edu.colorado.plv.fixr.protobuf.Acdfg.LabelMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='edge_id', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.LabelMap.edge_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labels', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.LabelMap.labels', index=1,
      number=2, type=14, cpp_type=8, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1501,
  serialized_end=1593,
)

_ACDFG_REPOTAG = _descriptor.Descriptor(
  name='RepoTag',
  full_name='edu.colorado.plv.fixr.protobuf.Acdfg.RepoTag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repo_name', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.RepoTag.repo_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.RepoTag.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.RepoTag.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commit_hash', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.RepoTag.commit_hash', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commit_date', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.RepoTag.commit_date', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1595,
  serialized_end=1697,
)

_ACDFG_METHODBAG = _descriptor.Descriptor(
  name='MethodBag',
  full_name='edu.colorado.plv.fixr.protobuf.Acdfg.MethodBag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.MethodBag.method', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1699,
  serialized_end=1726,
)

_ACDFG_SOURCEINFO = _descriptor.Descriptor(
  name='SourceInfo',
  full_name='edu.colorado.plv.fixr.protobuf.Acdfg.SourceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_name', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.SourceInfo.package_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='class_name', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.SourceInfo.class_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method_name', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.SourceInfo.method_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='class_line_number', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.SourceInfo.class_line_number', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method_line_number', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.SourceInfo.method_line_number', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_class_name', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.SourceInfo.source_class_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='abs_source_class_name', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.SourceInfo.abs_source_class_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1729,
  serialized_end=1917,
)

_ACDFG = _descriptor.Descriptor(
  name='Acdfg',
  full_name='edu.colorado.plv.fixr.protobuf.Acdfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_node', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.data_node', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='misc_node', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.misc_node', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method_node', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.method_node', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='control_edge', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.control_edge', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='def_edge', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.def_edge', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_edge', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.use_edge', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trans_edge', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.trans_edge', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exceptional_edge', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.exceptional_edge', index=7,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='edge_labels', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.edge_labels', index=8,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repo_tag', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.repo_tag', index=9,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_info', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.source_info', index=10,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provenance_path', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.provenance_path', index=11,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method_bag', full_name='edu.colorado.plv.fixr.protobuf.Acdfg.method_bag', index=12,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ACDFG_DATANODE, _ACDFG_MISCNODE, _ACDFG_METHODNODE, _ACDFG_CONTROLEDGE, _ACDFG_DEFEDGE, _ACDFG_USEEDGE, _ACDFG_TRANSEDGE, _ACDFG_EXCEPTIONALCONTROLEDGE, _ACDFG_LABELMAP, _ACDFG_REPOTAG, _ACDFG_METHODBAG, _ACDFG_SOURCEINFO, ],
  enum_types=[
    _ACDFG_EDGELABEL,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=1963,
)

_ACDFG_DATANODE.fields_by_name['data_type'].enum_type = _ACDFG_DATANODE_DATATYPE
_ACDFG_DATANODE.containing_type = _ACDFG
_ACDFG_DATANODE_DATATYPE.containing_type = _ACDFG_DATANODE
_ACDFG_MISCNODE.containing_type = _ACDFG
_ACDFG_METHODNODE.containing_type = _ACDFG
_ACDFG_CONTROLEDGE.containing_type = _ACDFG
_ACDFG_DEFEDGE.containing_type = _ACDFG
_ACDFG_USEEDGE.containing_type = _ACDFG
_ACDFG_TRANSEDGE.containing_type = _ACDFG
_ACDFG_EXCEPTIONALCONTROLEDGE.containing_type = _ACDFG
_ACDFG_LABELMAP.fields_by_name['labels'].enum_type = _ACDFG_EDGELABEL
_ACDFG_LABELMAP.containing_type = _ACDFG
_ACDFG_REPOTAG.containing_type = _ACDFG
_ACDFG_METHODBAG.containing_type = _ACDFG
_ACDFG_SOURCEINFO.containing_type = _ACDFG
_ACDFG.fields_by_name['data_node'].message_type = _ACDFG_DATANODE
_ACDFG.fields_by_name['misc_node'].message_type = _ACDFG_MISCNODE
_ACDFG.fields_by_name['method_node'].message_type = _ACDFG_METHODNODE
_ACDFG.fields_by_name['control_edge'].message_type = _ACDFG_CONTROLEDGE
_ACDFG.fields_by_name['def_edge'].message_type = _ACDFG_DEFEDGE
_ACDFG.fields_by_name['use_edge'].message_type = _ACDFG_USEEDGE
_ACDFG.fields_by_name['trans_edge'].message_type = _ACDFG_TRANSEDGE
_ACDFG.fields_by_name['exceptional_edge'].message_type = _ACDFG_EXCEPTIONALCONTROLEDGE
_ACDFG.fields_by_name['edge_labels'].message_type = _ACDFG_LABELMAP
_ACDFG.fields_by_name['repo_tag'].message_type = _ACDFG_REPOTAG
_ACDFG.fields_by_name['source_info'].message_type = _ACDFG_SOURCEINFO
_ACDFG.fields_by_name['method_bag'].message_type = _ACDFG_METHODBAG
_ACDFG_EDGELABEL.containing_type = _ACDFG
DESCRIPTOR.message_types_by_name['Acdfg'] = _ACDFG

Acdfg = _reflection.GeneratedProtocolMessageType('Acdfg', (_message.Message,), dict(

  DataNode = _reflection.GeneratedProtocolMessageType('DataNode', (_message.Message,), dict(
    DESCRIPTOR = _ACDFG_DATANODE,
    __module__ = 'proto_acdfg_pb2'
    # @@protoc_insertion_point(class_scope:edu.colorado.plv.fixr.protobuf.Acdfg.DataNode)
    ))
  ,

  MiscNode = _reflection.GeneratedProtocolMessageType('MiscNode', (_message.Message,), dict(
    DESCRIPTOR = _ACDFG_MISCNODE,
    __module__ = 'proto_acdfg_pb2'
    # @@protoc_insertion_point(class_scope:edu.colorado.plv.fixr.protobuf.Acdfg.MiscNode)
    ))
  ,

  MethodNode = _reflection.GeneratedProtocolMessageType('MethodNode', (_message.Message,), dict(
    DESCRIPTOR = _ACDFG_METHODNODE,
    __module__ = 'proto_acdfg_pb2'
    # @@protoc_insertion_point(class_scope:edu.colorado.plv.fixr.protobuf.Acdfg.MethodNode)
    ))
  ,

  ControlEdge = _reflection.GeneratedProtocolMessageType('ControlEdge', (_message.Message,), dict(
    DESCRIPTOR = _ACDFG_CONTROLEDGE,
    __module__ = 'proto_acdfg_pb2'
    # @@protoc_insertion_point(class_scope:edu.colorado.plv.fixr.protobuf.Acdfg.ControlEdge)
    ))
  ,

  DefEdge = _reflection.GeneratedProtocolMessageType('DefEdge', (_message.Message,), dict(
    DESCRIPTOR = _ACDFG_DEFEDGE,
    __module__ = 'proto_acdfg_pb2'
    # @@protoc_insertion_point(class_scope:edu.colorado.plv.fixr.protobuf.Acdfg.DefEdge)
    ))
  ,

  UseEdge = _reflection.GeneratedProtocolMessageType('UseEdge', (_message.Message,), dict(
    DESCRIPTOR = _ACDFG_USEEDGE,
    __module__ = 'proto_acdfg_pb2'
    # @@protoc_insertion_point(class_scope:edu.colorado.plv.fixr.protobuf.Acdfg.UseEdge)
    ))
  ,

  TransEdge = _reflection.GeneratedProtocolMessageType('TransEdge', (_message.Message,), dict(
    DESCRIPTOR = _ACDFG_TRANSEDGE,
    __module__ = 'proto_acdfg_pb2'
    # @@protoc_insertion_point(class_scope:edu.colorado.plv.fixr.protobuf.Acdfg.TransEdge)
    ))
  ,

  ExceptionalControlEdge = _reflection.GeneratedProtocolMessageType('ExceptionalControlEdge', (_message.Message,), dict(
    DESCRIPTOR = _ACDFG_EXCEPTIONALCONTROLEDGE,
    __module__ = 'proto_acdfg_pb2'
    # @@protoc_insertion_point(class_scope:edu.colorado.plv.fixr.protobuf.Acdfg.ExceptionalControlEdge)
    ))
  ,

  LabelMap = _reflection.GeneratedProtocolMessageType('LabelMap', (_message.Message,), dict(
    DESCRIPTOR = _ACDFG_LABELMAP,
    __module__ = 'proto_acdfg_pb2'
    # @@protoc_insertion_point(class_scope:edu.colorado.plv.fixr.protobuf.Acdfg.LabelMap)
    ))
  ,

  RepoTag = _reflection.GeneratedProtocolMessageType('RepoTag', (_message.Message,), dict(
    DESCRIPTOR = _ACDFG_REPOTAG,
    __module__ = 'proto_acdfg_pb2'
    # @@protoc_insertion_point(class_scope:edu.colorado.plv.fixr.protobuf.Acdfg.RepoTag)
    ))
  ,

  MethodBag = _reflection.GeneratedProtocolMessageType('MethodBag', (_message.Message,), dict(
    DESCRIPTOR = _ACDFG_METHODBAG,
    __module__ = 'proto_acdfg_pb2'
    # @@protoc_insertion_point(class_scope:edu.colorado.plv.fixr.protobuf.Acdfg.MethodBag)
    ))
  ,

  SourceInfo = _reflection.GeneratedProtocolMessageType('SourceInfo', (_message.Message,), dict(
    DESCRIPTOR = _ACDFG_SOURCEINFO,
    __module__ = 'proto_acdfg_pb2'
    # @@protoc_insertion_point(class_scope:edu.colorado.plv.fixr.protobuf.Acdfg.SourceInfo)
    ))
  ,
  DESCRIPTOR = _ACDFG,
  __module__ = 'proto_acdfg_pb2'
  # @@protoc_insertion_point(class_scope:edu.colorado.plv.fixr.protobuf.Acdfg)
  ))
_sym_db.RegisterMessage(Acdfg)
_sym_db.RegisterMessage(Acdfg.DataNode)
_sym_db.RegisterMessage(Acdfg.MiscNode)
_sym_db.RegisterMessage(Acdfg.MethodNode)
_sym_db.RegisterMessage(Acdfg.ControlEdge)
_sym_db.RegisterMessage(Acdfg.DefEdge)
_sym_db.RegisterMessage(Acdfg.UseEdge)
_sym_db.RegisterMessage(Acdfg.TransEdge)
_sym_db.RegisterMessage(Acdfg.ExceptionalControlEdge)
_sym_db.RegisterMessage(Acdfg.LabelMap)
_sym_db.RegisterMessage(Acdfg.RepoTag)
_sym_db.RegisterMessage(Acdfg.MethodBag)
_sym_db.RegisterMessage(Acdfg.SourceInfo)


# @@protoc_insertion_point(module_scope)
