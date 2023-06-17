import grpc
from concurrent import futures

from  protos.peek_pb2 import (
    userRequest,
    userResponse,
    peekRequest,
    peekResponse,
    topic,
    notif
)
from protos.peek_pb2_grpc import (
    peekServiceServicer,
    add_peekServiceServicer_to_server
)

from compute import (
    compute
)

class PeekService(peekServiceServicer):
    def __init__(self):
        pass

    def addUser(self, request, context):
        print("Adding user: " + request.username + " with password: " + request.password)
        return None

    def getCachedData(self, request, context):
        print("Getting cached data for user: " + str(request.userID) + " and app: " + str(request.appID))
        return None

    def getNewData(self, request, context):
        print("Getting new data for user: " + str(request.userID) + " and app: " + str(request.appID))
        #compute()
        return peekResponse(
            topics=[
                topic(
                    name="testTopic",
                    emoji=123,
                    highlight="testHighlight",
                    summary="testSummary",
                    notifs=[
                        notif(
                            title="testTitle",
                            uri="testURI"
                        ),
                        notif(
                            title="testTitle2",
                            uri="testURI2"
                        )
                    ]
                )
            ]
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_peekServiceServicer_to_server(
        PeekService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()


# if run as main, start the server
if __name__ == '__main__':
    serve()