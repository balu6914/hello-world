# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tendermint/crypto/proof.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database


# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="tendermint/crypto/proof.proto",
    package="tendermint.crypto",
    syntax="proto3",
    serialized_options=b"Z8github.com/tendermint/tendermint/proto/tendermint/crypto",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1dtendermint/crypto/proof.proto\x12\x11tendermint.crypto\x1a\x14gogoproto/gogo.proto"G\n\x05Proof\x12\r\n\x05total\x18\x01 \x01(\x03\x12\r\n\x05index\x18\x02 \x01(\x03\x12\x11\n\tleaf_hash\x18\x03 \x01(\x0c\x12\r\n\x05\x61unts\x18\x04 \x03(\x0c"?\n\x07ValueOp\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\'\n\x05proof\x18\x02 \x01(\x0b\x32\x18.tendermint.crypto.Proof"6\n\x08\x44ominoOp\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05input\x18\x02 \x01(\t\x12\x0e\n\x06output\x18\x03 \x01(\t"2\n\x07ProofOp\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c"9\n\x08ProofOps\x12-\n\x03ops\x18\x01 \x03(\x0b\x32\x1a.tendermint.crypto.ProofOpB\x04\xc8\xde\x1f\x00\x42:Z8github.com/tendermint/tendermint/proto/tendermint/cryptob\x06proto3',
    dependencies=[
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
    ],
)


_PROOF = _descriptor.Descriptor(
    name="Proof",
    full_name="tendermint.crypto.Proof",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="total",
            full_name="tendermint.crypto.Proof.total",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="index",
            full_name="tendermint.crypto.Proof.index",
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="leaf_hash",
            full_name="tendermint.crypto.Proof.leaf_hash",
            index=2,
            number=3,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="aunts",
            full_name="tendermint.crypto.Proof.aunts",
            index=3,
            number=4,
            type=12,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=74,
    serialized_end=145,
)


_VALUEOP = _descriptor.Descriptor(
    name="ValueOp",
    full_name="tendermint.crypto.ValueOp",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="tendermint.crypto.ValueOp.key",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="proof",
            full_name="tendermint.crypto.ValueOp.proof",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=147,
    serialized_end=210,
)


_DOMINOOP = _descriptor.Descriptor(
    name="DominoOp",
    full_name="tendermint.crypto.DominoOp",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="tendermint.crypto.DominoOp.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="input",
            full_name="tendermint.crypto.DominoOp.input",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="output",
            full_name="tendermint.crypto.DominoOp.output",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=212,
    serialized_end=266,
)


_PROOFOP = _descriptor.Descriptor(
    name="ProofOp",
    full_name="tendermint.crypto.ProofOp",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="tendermint.crypto.ProofOp.type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="key",
            full_name="tendermint.crypto.ProofOp.key",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="data",
            full_name="tendermint.crypto.ProofOp.data",
            index=2,
            number=3,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=268,
    serialized_end=318,
)


_PROOFOPS = _descriptor.Descriptor(
    name="ProofOps",
    full_name="tendermint.crypto.ProofOps",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="ops",
            full_name="tendermint.crypto.ProofOps.ops",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=320,
    serialized_end=377,
)

_VALUEOP.fields_by_name["proof"].message_type = _PROOF
_PROOFOPS.fields_by_name["ops"].message_type = _PROOFOP
DESCRIPTOR.message_types_by_name["Proof"] = _PROOF
DESCRIPTOR.message_types_by_name["ValueOp"] = _VALUEOP
DESCRIPTOR.message_types_by_name["DominoOp"] = _DOMINOOP
DESCRIPTOR.message_types_by_name["ProofOp"] = _PROOFOP
DESCRIPTOR.message_types_by_name["ProofOps"] = _PROOFOPS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Proof = _reflection.GeneratedProtocolMessageType(
    "Proof",
    (_message.Message,),
    {
        "DESCRIPTOR": _PROOF,
        "__module__": "tendermint.crypto.proof_pb2"
        # @@protoc_insertion_point(class_scope:tendermint.crypto.Proof)
    },
)
_sym_db.RegisterMessage(Proof)

ValueOp = _reflection.GeneratedProtocolMessageType(
    "ValueOp",
    (_message.Message,),
    {
        "DESCRIPTOR": _VALUEOP,
        "__module__": "tendermint.crypto.proof_pb2"
        # @@protoc_insertion_point(class_scope:tendermint.crypto.ValueOp)
    },
)
_sym_db.RegisterMessage(ValueOp)

DominoOp = _reflection.GeneratedProtocolMessageType(
    "DominoOp",
    (_message.Message,),
    {
        "DESCRIPTOR": _DOMINOOP,
        "__module__": "tendermint.crypto.proof_pb2"
        # @@protoc_insertion_point(class_scope:tendermint.crypto.DominoOp)
    },
)
_sym_db.RegisterMessage(DominoOp)

ProofOp = _reflection.GeneratedProtocolMessageType(
    "ProofOp",
    (_message.Message,),
    {
        "DESCRIPTOR": _PROOFOP,
        "__module__": "tendermint.crypto.proof_pb2"
        # @@protoc_insertion_point(class_scope:tendermint.crypto.ProofOp)
    },
)
_sym_db.RegisterMessage(ProofOp)

ProofOps = _reflection.GeneratedProtocolMessageType(
    "ProofOps",
    (_message.Message,),
    {
        "DESCRIPTOR": _PROOFOPS,
        "__module__": "tendermint.crypto.proof_pb2"
        # @@protoc_insertion_point(class_scope:tendermint.crypto.ProofOps)
    },
)
_sym_db.RegisterMessage(ProofOps)


DESCRIPTOR._options = None
_PROOFOPS.fields_by_name["ops"]._options = None
# @@protoc_insertion_point(module_scope)
