# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from protobufs import usuario_pb2 as usuario__pb2

GRPC_GENERATED_VERSION = "1.64.1"
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = "1.65.0"
SCHEDULED_RELEASE_DATE = "June 25, 2024"
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(
        GRPC_VERSION, GRPC_GENERATED_VERSION
    )
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + f" but the generated code in usuario_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
        + f" This warning will become an error in {EXPECTED_ERROR_RELEASE},"
        + f" scheduled for release on {SCHEDULED_RELEASE_DATE}.",
        RuntimeWarning,
    )


class UsuarioServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CriarUsuario = channel.unary_unary(
            "/usuario.UsuarioService/CriarUsuario",
            request_serializer=usuario__pb2.Usuario.SerializeToString,
            response_deserializer=usuario__pb2.Resposta.FromString,
            _registered_method=True,
        )
        self.LerUsuario = channel.unary_unary(
            "/usuario.UsuarioService/LerUsuario",
            request_serializer=usuario__pb2.UsuarioID.SerializeToString,
            response_deserializer=usuario__pb2.Usuario.FromString,
            _registered_method=True,
        )
        self.AtualizarUsuario = channel.unary_unary(
            "/usuario.UsuarioService/AtualizarUsuario",
            request_serializer=usuario__pb2.Usuario.SerializeToString,
            response_deserializer=usuario__pb2.Resposta.FromString,
            _registered_method=True,
        )
        self.DeletarUsuario = channel.unary_unary(
            "/usuario.UsuarioService/DeletarUsuario",
            request_serializer=usuario__pb2.UsuarioID.SerializeToString,
            response_deserializer=usuario__pb2.Resposta.FromString,
            _registered_method=True,
        )
        self.LerUsuarios = channel.unary_unary(
            "/usuario.UsuarioService/LerUsuarios",
            request_serializer=usuario__pb2.Empty.SerializeToString,
            response_deserializer=usuario__pb2.UsuarioList.FromString,
            _registered_method=True,
        )


class UsuarioServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CriarUsuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def LerUsuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AtualizarUsuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeletarUsuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def LerUsuarios(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_UsuarioServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CriarUsuario": grpc.unary_unary_rpc_method_handler(
            servicer.CriarUsuario,
            request_deserializer=usuario__pb2.Usuario.FromString,
            response_serializer=usuario__pb2.Resposta.SerializeToString,
        ),
        "LerUsuario": grpc.unary_unary_rpc_method_handler(
            servicer.LerUsuario,
            request_deserializer=usuario__pb2.UsuarioID.FromString,
            response_serializer=usuario__pb2.Usuario.SerializeToString,
        ),
        "AtualizarUsuario": grpc.unary_unary_rpc_method_handler(
            servicer.AtualizarUsuario,
            request_deserializer=usuario__pb2.Usuario.FromString,
            response_serializer=usuario__pb2.Resposta.SerializeToString,
        ),
        "DeletarUsuario": grpc.unary_unary_rpc_method_handler(
            servicer.DeletarUsuario,
            request_deserializer=usuario__pb2.UsuarioID.FromString,
            response_serializer=usuario__pb2.Resposta.SerializeToString,
        ),
        "LerUsuarios": grpc.unary_unary_rpc_method_handler(
            servicer.LerUsuarios,
            request_deserializer=usuario__pb2.Empty.FromString,
            response_serializer=usuario__pb2.UsuarioList.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "usuario.UsuarioService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers("usuario.UsuarioService", rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class UsuarioService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CriarUsuario(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/usuario.UsuarioService/CriarUsuario",
            usuario__pb2.Usuario.SerializeToString,
            usuario__pb2.Resposta.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def LerUsuario(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/usuario.UsuarioService/LerUsuario",
            usuario__pb2.UsuarioID.SerializeToString,
            usuario__pb2.Usuario.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def AtualizarUsuario(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/usuario.UsuarioService/AtualizarUsuario",
            usuario__pb2.Usuario.SerializeToString,
            usuario__pb2.Resposta.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def DeletarUsuario(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/usuario.UsuarioService/DeletarUsuario",
            usuario__pb2.UsuarioID.SerializeToString,
            usuario__pb2.Resposta.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def LerUsuarios(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/usuario.UsuarioService/LerUsuarios",
            usuario__pb2.Empty.SerializeToString,
            usuario__pb2.UsuarioList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )