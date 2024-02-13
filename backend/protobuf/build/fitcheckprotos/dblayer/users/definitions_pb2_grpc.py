# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fitcheckprotos.dblayer import confirmation_pb2 as fitcheckprotos_dot_dblayer_dot_confirmation__pb2
from fitcheckprotos.dblayer import resource_pb2 as fitcheckprotos_dot_dblayer_dot_resource__pb2
from fitcheckprotos.dblayer.users import definitions_pb2 as fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2


class UserDefinitionManagementStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateCustomSize = channel.unary_unary(
                '/fitcheckprotos.dblayer.users.UserDefinitionManagement/CreateCustomSize',
                request_serializer=fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.UserDefinedSize.SerializeToString,
                response_deserializer=fitcheckprotos_dot_dblayer_dot_confirmation__pb2.CollectionModified.FromString,
                )
        self.CreateCustomFabric = channel.unary_unary(
                '/fitcheckprotos.dblayer.users.UserDefinitionManagement/CreateCustomFabric',
                request_serializer=fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.UserDefinedFabric.SerializeToString,
                response_deserializer=fitcheckprotos_dot_dblayer_dot_confirmation__pb2.CollectionModified.FromString,
                )
        self.DeleteCustomSize = channel.unary_unary(
                '/fitcheckprotos.dblayer.users.UserDefinitionManagement/DeleteCustomSize',
                request_serializer=fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.UserDefinedSize.SerializeToString,
                response_deserializer=fitcheckprotos_dot_dblayer_dot_confirmation__pb2.CollectionModified.FromString,
                )
        self.DeleteCustomFabric = channel.unary_unary(
                '/fitcheckprotos.dblayer.users.UserDefinitionManagement/DeleteCustomFabric',
                request_serializer=fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.UserDefinedFabric.SerializeToString,
                response_deserializer=fitcheckprotos_dot_dblayer_dot_confirmation__pb2.CollectionModified.FromString,
                )
        self.GetUserFabrics = channel.unary_unary(
                '/fitcheckprotos.dblayer.users.UserDefinitionManagement/GetUserFabrics',
                request_serializer=fitcheckprotos_dot_dblayer_dot_resource__pb2.DocumentIdentifier.SerializeToString,
                response_deserializer=fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.ListUserFabrics.FromString,
                )
        self.GetUserSizes = channel.unary_unary(
                '/fitcheckprotos.dblayer.users.UserDefinitionManagement/GetUserSizes',
                request_serializer=fitcheckprotos_dot_dblayer_dot_resource__pb2.DocumentIdentifier.SerializeToString,
                response_deserializer=fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.ListUserSizes.FromString,
                )


class UserDefinitionManagementServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateCustomSize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCustomFabric(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCustomSize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCustomFabric(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserFabrics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserSizes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserDefinitionManagementServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateCustomSize': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCustomSize,
                    request_deserializer=fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.UserDefinedSize.FromString,
                    response_serializer=fitcheckprotos_dot_dblayer_dot_confirmation__pb2.CollectionModified.SerializeToString,
            ),
            'CreateCustomFabric': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCustomFabric,
                    request_deserializer=fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.UserDefinedFabric.FromString,
                    response_serializer=fitcheckprotos_dot_dblayer_dot_confirmation__pb2.CollectionModified.SerializeToString,
            ),
            'DeleteCustomSize': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCustomSize,
                    request_deserializer=fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.UserDefinedSize.FromString,
                    response_serializer=fitcheckprotos_dot_dblayer_dot_confirmation__pb2.CollectionModified.SerializeToString,
            ),
            'DeleteCustomFabric': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCustomFabric,
                    request_deserializer=fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.UserDefinedFabric.FromString,
                    response_serializer=fitcheckprotos_dot_dblayer_dot_confirmation__pb2.CollectionModified.SerializeToString,
            ),
            'GetUserFabrics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserFabrics,
                    request_deserializer=fitcheckprotos_dot_dblayer_dot_resource__pb2.DocumentIdentifier.FromString,
                    response_serializer=fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.ListUserFabrics.SerializeToString,
            ),
            'GetUserSizes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserSizes,
                    request_deserializer=fitcheckprotos_dot_dblayer_dot_resource__pb2.DocumentIdentifier.FromString,
                    response_serializer=fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.ListUserSizes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fitcheckprotos.dblayer.users.UserDefinitionManagement', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserDefinitionManagement(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateCustomSize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fitcheckprotos.dblayer.users.UserDefinitionManagement/CreateCustomSize',
            fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.UserDefinedSize.SerializeToString,
            fitcheckprotos_dot_dblayer_dot_confirmation__pb2.CollectionModified.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCustomFabric(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fitcheckprotos.dblayer.users.UserDefinitionManagement/CreateCustomFabric',
            fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.UserDefinedFabric.SerializeToString,
            fitcheckprotos_dot_dblayer_dot_confirmation__pb2.CollectionModified.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCustomSize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fitcheckprotos.dblayer.users.UserDefinitionManagement/DeleteCustomSize',
            fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.UserDefinedSize.SerializeToString,
            fitcheckprotos_dot_dblayer_dot_confirmation__pb2.CollectionModified.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCustomFabric(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fitcheckprotos.dblayer.users.UserDefinitionManagement/DeleteCustomFabric',
            fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.UserDefinedFabric.SerializeToString,
            fitcheckprotos_dot_dblayer_dot_confirmation__pb2.CollectionModified.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserFabrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fitcheckprotos.dblayer.users.UserDefinitionManagement/GetUserFabrics',
            fitcheckprotos_dot_dblayer_dot_resource__pb2.DocumentIdentifier.SerializeToString,
            fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.ListUserFabrics.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserSizes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fitcheckprotos.dblayer.users.UserDefinitionManagement/GetUserSizes',
            fitcheckprotos_dot_dblayer_dot_resource__pb2.DocumentIdentifier.SerializeToString,
            fitcheckprotos_dot_dblayer_dot_users_dot_definitions__pb2.ListUserSizes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
