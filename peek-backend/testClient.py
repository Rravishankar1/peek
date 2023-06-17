import grpc

from protos.peek_pb2 import (
    userRequest,
    userResponse,
    peekRequest,
    peekResponse,
    topic,
    notif
)
from protos.peek_pb2_grpc import peekServiceStub

def testClient():
    # create a gRPC channel + stub
    channel = grpc.insecure_channel('localhost:50051')
    stub = peekServiceStub(channel)

    # create a valid request message
    request = peekRequest(userID=123, appID=456)

    # make the call
    response = stub.getNewData(request)

    # et voila
    print(response)

if __name__ == '__main__':
    testClient()