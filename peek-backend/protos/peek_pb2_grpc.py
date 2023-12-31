# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import protos.peek_pb2 as peek__pb2


class peekServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.addUser = channel.unary_unary(
                '/peek.peekService/addUser',
                request_serializer=peek__pb2.userRequest.SerializeToString,
                response_deserializer=peek__pb2.userResponse.FromString,
                )
        self.loginUser = channel.unary_unary(
                '/peek.peekService/loginUser',
                request_serializer=peek__pb2.userRequest.SerializeToString,
                response_deserializer=peek__pb2.userResponse.FromString,
                )
        self.getCachedData = channel.unary_unary(
                '/peek.peekService/getCachedData',
                request_serializer=peek__pb2.peekRequest.SerializeToString,
                response_deserializer=peek__pb2.peekResponse.FromString,
                )
        self.getNewData = channel.unary_unary(
                '/peek.peekService/getNewData',
                request_serializer=peek__pb2.peekRequest.SerializeToString,
                response_deserializer=peek__pb2.peekResponse.FromString,
                )


class peekServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def addUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def loginUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getCachedData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getNewData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_peekServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'addUser': grpc.unary_unary_rpc_method_handler(
                    servicer.addUser,
                    request_deserializer=peek__pb2.userRequest.FromString,
                    response_serializer=peek__pb2.userResponse.SerializeToString,
            ),
            'loginUser': grpc.unary_unary_rpc_method_handler(
                    servicer.loginUser,
                    request_deserializer=peek__pb2.userRequest.FromString,
                    response_serializer=peek__pb2.userResponse.SerializeToString,
            ),
            'getCachedData': grpc.unary_unary_rpc_method_handler(
                    servicer.getCachedData,
                    request_deserializer=peek__pb2.peekRequest.FromString,
                    response_serializer=peek__pb2.peekResponse.SerializeToString,
            ),
            'getNewData': grpc.unary_unary_rpc_method_handler(
                    servicer.getNewData,
                    request_deserializer=peek__pb2.peekRequest.FromString,
                    response_serializer=peek__pb2.peekResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'peek.peekService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class peekService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def addUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/peek.peekService/addUser',
            peek__pb2.userRequest.SerializeToString,
            peek__pb2.userResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def loginUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/peek.peekService/loginUser',
            peek__pb2.userRequest.SerializeToString,
            peek__pb2.userResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getCachedData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/peek.peekService/getCachedData',
            peek__pb2.peekRequest.SerializeToString,
            peek__pb2.peekResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getNewData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/peek.peekService/getNewData',
            peek__pb2.peekRequest.SerializeToString,
            peek__pb2.peekResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
