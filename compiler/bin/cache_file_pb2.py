# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cache_file.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cache_file.proto',
  package='Caching',
  syntax='proto3',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n\x10\x63\x61\x63he_file.proto\x12\x07\x43\x61\x63hing\"^\n\x06Header\x12\x1b\n\x13tools_major_version\x18\x01 \x01(\r\x12\x1b\n\x13tools_minor_version\x18\x02 \x01(\r\x12\x1a\n\x12linker_script_hash\x18\x03 \x01(\x04\"E\n\nObjectFile\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x11\n\tfile_hash\x18\x02 \x01(\x04\x12\x11\n\tname_hash\x18\x03 \x01(\x04\"8\n\x10LinkerScriptFile\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x11\n\tfile_hash\x18\x02 \x01(\x04\"F\n\x0b\x41rchiveFile\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x11\n\tfile_hash\x18\x02 \x01(\x04\x12\x11\n\tname_hash\x18\x03 \x01(\x04\"S\n\rArchiveMember\x12\x13\n\x0bmember_name\x18\x01 \x01(\t\x12\x13\n\x0bmember_hash\x18\x02 \x01(\x04\x12\x18\n\x10member_name_hash\x18\x03 \x01(\x04\"8\n\x05Input\x12\x16\n\x0eobject_file_id\x18\x01 \x01(\r\x12\x17\n\x0f\x61rchive_file_id\x18\x02 \x01(\r\"J\n\rOutputSection\x12\x14\n\x0csection_name\x18\x01 \x01(\t\x12\x0c\n\x04hash\x18\x02 \x01(\x04\x12\x15\n\rsection_index\x18\x03 \x01(\x04\"\"\n\rRuleContainer\x12\x11\n\trule_hash\x18\x01 \x01(\x04\"w\n\x0cInputSection\x12\x14\n\x0csection_name\x18\x01 \x01(\t\x12\x0c\n\x04hash\x18\x02 \x01(\x04\x12\x16\n\x0eout_section_id\x18\x03 \x01(\r\x12\x10\n\x08input_id\x18\x04 \x01(\r\x12\x19\n\x11rule_container_id\x18\x05 \x01(\r\"}\n\x0c\x43ommonSymbol\x12\x13\n\x0bsymbol_name\x18\x01 \x01(\t\x12\x13\n\x0bsymbol_hash\x18\x02 \x01(\x04\x12\x16\n\x0eout_section_id\x18\x03 \x01(\r\x12\x19\n\x11rule_container_id\x18\x04 \x01(\r\x12\x10\n\x08input_id\x18\x05 \x01(\r\"\xe3\x03\n\x0f\x43\x61\x63hingInfoDict\x12*\n\x11\x64ictionary_header\x18\x01 \x01(\x0b\x32\x0f.Caching.Header\x12-\n\x0einput_sections\x18\x02 \x03(\x0b\x32\x15.Caching.InputSection\x12/\n\x0foutput_sections\x18\x03 \x03(\x0b\x32\x16.Caching.OutputSection\x12)\n\x0cobject_files\x18\x04 \x03(\x0b\x32\x13.Caching.ObjectFile\x12+\n\rarchive_files\x18\x05 \x03(\x0b\x32\x14.Caching.ArchiveFile\x12/\n\x0f\x61rchive_members\x18\x06 \x03(\x0b\x32\x16.Caching.ArchiveMember\x12\x36\n\x13linker_script_files\x18\x07 \x03(\x0b\x32\x19.Caching.LinkerScriptFile\x12#\n\x0binput_files\x18\x08 \x03(\x0b\x32\x0e.Caching.Input\x12/\n\x0frule_containers\x18\t \x03(\x0b\x32\x16.Caching.RuleContainer\x12-\n\x0e\x63ommon_symbols\x18\n \x03(\x0b\x32\x15.Caching.CommonSymbolB\x02H\x03\x62\x06proto3')
)




_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='Caching.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tools_major_version', full_name='Caching.Header.tools_major_version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tools_minor_version', full_name='Caching.Header.tools_minor_version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linker_script_hash', full_name='Caching.Header.linker_script_hash', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=123,
)


_OBJECTFILE = _descriptor.Descriptor(
  name='ObjectFile',
  full_name='Caching.ObjectFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_name', full_name='Caching.ObjectFile.file_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_hash', full_name='Caching.ObjectFile.file_hash', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name_hash', full_name='Caching.ObjectFile.name_hash', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=194,
)


_LINKERSCRIPTFILE = _descriptor.Descriptor(
  name='LinkerScriptFile',
  full_name='Caching.LinkerScriptFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_name', full_name='Caching.LinkerScriptFile.file_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_hash', full_name='Caching.LinkerScriptFile.file_hash', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=252,
)


_ARCHIVEFILE = _descriptor.Descriptor(
  name='ArchiveFile',
  full_name='Caching.ArchiveFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_name', full_name='Caching.ArchiveFile.file_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_hash', full_name='Caching.ArchiveFile.file_hash', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name_hash', full_name='Caching.ArchiveFile.name_hash', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=254,
  serialized_end=324,
)


_ARCHIVEMEMBER = _descriptor.Descriptor(
  name='ArchiveMember',
  full_name='Caching.ArchiveMember',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='member_name', full_name='Caching.ArchiveMember.member_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='member_hash', full_name='Caching.ArchiveMember.member_hash', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='member_name_hash', full_name='Caching.ArchiveMember.member_name_hash', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=326,
  serialized_end=409,
)


_INPUT = _descriptor.Descriptor(
  name='Input',
  full_name='Caching.Input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_file_id', full_name='Caching.Input.object_file_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='archive_file_id', full_name='Caching.Input.archive_file_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=467,
)


_OUTPUTSECTION = _descriptor.Descriptor(
  name='OutputSection',
  full_name='Caching.OutputSection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='section_name', full_name='Caching.OutputSection.section_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='Caching.OutputSection.hash', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='section_index', full_name='Caching.OutputSection.section_index', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=469,
  serialized_end=543,
)


_RULECONTAINER = _descriptor.Descriptor(
  name='RuleContainer',
  full_name='Caching.RuleContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rule_hash', full_name='Caching.RuleContainer.rule_hash', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=545,
  serialized_end=579,
)


_INPUTSECTION = _descriptor.Descriptor(
  name='InputSection',
  full_name='Caching.InputSection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='section_name', full_name='Caching.InputSection.section_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='Caching.InputSection.hash', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out_section_id', full_name='Caching.InputSection.out_section_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_id', full_name='Caching.InputSection.input_id', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule_container_id', full_name='Caching.InputSection.rule_container_id', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=581,
  serialized_end=700,
)


_COMMONSYMBOL = _descriptor.Descriptor(
  name='CommonSymbol',
  full_name='Caching.CommonSymbol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol_name', full_name='Caching.CommonSymbol.symbol_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol_hash', full_name='Caching.CommonSymbol.symbol_hash', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out_section_id', full_name='Caching.CommonSymbol.out_section_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule_container_id', full_name='Caching.CommonSymbol.rule_container_id', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_id', full_name='Caching.CommonSymbol.input_id', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=702,
  serialized_end=827,
)


_CACHINGINFODICT = _descriptor.Descriptor(
  name='CachingInfoDict',
  full_name='Caching.CachingInfoDict',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dictionary_header', full_name='Caching.CachingInfoDict.dictionary_header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_sections', full_name='Caching.CachingInfoDict.input_sections', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_sections', full_name='Caching.CachingInfoDict.output_sections', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_files', full_name='Caching.CachingInfoDict.object_files', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='archive_files', full_name='Caching.CachingInfoDict.archive_files', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='archive_members', full_name='Caching.CachingInfoDict.archive_members', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linker_script_files', full_name='Caching.CachingInfoDict.linker_script_files', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_files', full_name='Caching.CachingInfoDict.input_files', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule_containers', full_name='Caching.CachingInfoDict.rule_containers', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='common_symbols', full_name='Caching.CachingInfoDict.common_symbols', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=830,
  serialized_end=1313,
)

_CACHINGINFODICT.fields_by_name['dictionary_header'].message_type = _HEADER
_CACHINGINFODICT.fields_by_name['input_sections'].message_type = _INPUTSECTION
_CACHINGINFODICT.fields_by_name['output_sections'].message_type = _OUTPUTSECTION
_CACHINGINFODICT.fields_by_name['object_files'].message_type = _OBJECTFILE
_CACHINGINFODICT.fields_by_name['archive_files'].message_type = _ARCHIVEFILE
_CACHINGINFODICT.fields_by_name['archive_members'].message_type = _ARCHIVEMEMBER
_CACHINGINFODICT.fields_by_name['linker_script_files'].message_type = _LINKERSCRIPTFILE
_CACHINGINFODICT.fields_by_name['input_files'].message_type = _INPUT
_CACHINGINFODICT.fields_by_name['rule_containers'].message_type = _RULECONTAINER
_CACHINGINFODICT.fields_by_name['common_symbols'].message_type = _COMMONSYMBOL
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['ObjectFile'] = _OBJECTFILE
DESCRIPTOR.message_types_by_name['LinkerScriptFile'] = _LINKERSCRIPTFILE
DESCRIPTOR.message_types_by_name['ArchiveFile'] = _ARCHIVEFILE
DESCRIPTOR.message_types_by_name['ArchiveMember'] = _ARCHIVEMEMBER
DESCRIPTOR.message_types_by_name['Input'] = _INPUT
DESCRIPTOR.message_types_by_name['OutputSection'] = _OUTPUTSECTION
DESCRIPTOR.message_types_by_name['RuleContainer'] = _RULECONTAINER
DESCRIPTOR.message_types_by_name['InputSection'] = _INPUTSECTION
DESCRIPTOR.message_types_by_name['CommonSymbol'] = _COMMONSYMBOL
DESCRIPTOR.message_types_by_name['CachingInfoDict'] = _CACHINGINFODICT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'cache_file_pb2'
  # @@protoc_insertion_point(class_scope:Caching.Header)
  })
_sym_db.RegisterMessage(Header)

ObjectFile = _reflection.GeneratedProtocolMessageType('ObjectFile', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTFILE,
  '__module__' : 'cache_file_pb2'
  # @@protoc_insertion_point(class_scope:Caching.ObjectFile)
  })
_sym_db.RegisterMessage(ObjectFile)

LinkerScriptFile = _reflection.GeneratedProtocolMessageType('LinkerScriptFile', (_message.Message,), {
  'DESCRIPTOR' : _LINKERSCRIPTFILE,
  '__module__' : 'cache_file_pb2'
  # @@protoc_insertion_point(class_scope:Caching.LinkerScriptFile)
  })
_sym_db.RegisterMessage(LinkerScriptFile)

ArchiveFile = _reflection.GeneratedProtocolMessageType('ArchiveFile', (_message.Message,), {
  'DESCRIPTOR' : _ARCHIVEFILE,
  '__module__' : 'cache_file_pb2'
  # @@protoc_insertion_point(class_scope:Caching.ArchiveFile)
  })
_sym_db.RegisterMessage(ArchiveFile)

ArchiveMember = _reflection.GeneratedProtocolMessageType('ArchiveMember', (_message.Message,), {
  'DESCRIPTOR' : _ARCHIVEMEMBER,
  '__module__' : 'cache_file_pb2'
  # @@protoc_insertion_point(class_scope:Caching.ArchiveMember)
  })
_sym_db.RegisterMessage(ArchiveMember)

Input = _reflection.GeneratedProtocolMessageType('Input', (_message.Message,), {
  'DESCRIPTOR' : _INPUT,
  '__module__' : 'cache_file_pb2'
  # @@protoc_insertion_point(class_scope:Caching.Input)
  })
_sym_db.RegisterMessage(Input)

OutputSection = _reflection.GeneratedProtocolMessageType('OutputSection', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUTSECTION,
  '__module__' : 'cache_file_pb2'
  # @@protoc_insertion_point(class_scope:Caching.OutputSection)
  })
_sym_db.RegisterMessage(OutputSection)

RuleContainer = _reflection.GeneratedProtocolMessageType('RuleContainer', (_message.Message,), {
  'DESCRIPTOR' : _RULECONTAINER,
  '__module__' : 'cache_file_pb2'
  # @@protoc_insertion_point(class_scope:Caching.RuleContainer)
  })
_sym_db.RegisterMessage(RuleContainer)

InputSection = _reflection.GeneratedProtocolMessageType('InputSection', (_message.Message,), {
  'DESCRIPTOR' : _INPUTSECTION,
  '__module__' : 'cache_file_pb2'
  # @@protoc_insertion_point(class_scope:Caching.InputSection)
  })
_sym_db.RegisterMessage(InputSection)

CommonSymbol = _reflection.GeneratedProtocolMessageType('CommonSymbol', (_message.Message,), {
  'DESCRIPTOR' : _COMMONSYMBOL,
  '__module__' : 'cache_file_pb2'
  # @@protoc_insertion_point(class_scope:Caching.CommonSymbol)
  })
_sym_db.RegisterMessage(CommonSymbol)

CachingInfoDict = _reflection.GeneratedProtocolMessageType('CachingInfoDict', (_message.Message,), {
  'DESCRIPTOR' : _CACHINGINFODICT,
  '__module__' : 'cache_file_pb2'
  # @@protoc_insertion_point(class_scope:Caching.CachingInfoDict)
  })
_sym_db.RegisterMessage(CachingInfoDict)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)