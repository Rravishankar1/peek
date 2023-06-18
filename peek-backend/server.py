import grpc
from concurrent import futures

from protos.peek_pb2_grpc import (
    peekServiceServicer,
    add_peekServiceServicer_to_server
)

import compute.switcher as switcher

class PeekService(peekServiceServicer):
    def __init__(self):
        pass

    def addUser(self, request, context):
        print("Adding user: " + request.username + " with password: " + request.password)
        print("NOT YET IMPLEMENTED!")
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not yet implemented!")

    def getCachedData(self, request, context):
        print("Getting cached data for user: " + str(request.userID))
        return switcher.direct(request, context, True)

    def getNewData(self, request, context):
        print("Getting new data for user: " + str(request.userID))
        return switcher.direct(request, context, False)  

def serve():
    print("Starting server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_peekServiceServicer_to_server(
        PeekService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()


# Start the server
if __name__ == '__main__':
    serve()