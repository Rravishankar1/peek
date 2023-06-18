import graphene
from flask import Flask
from flask_graphql import GraphQLView
import grpc
import peek_pb2
import peek_pb2_grpc

class Notif(graphene.ObjectType):
    title = graphene.String()
    uri = graphene.String()

class Topic(graphene.ObjectType):
    name = graphene.String()
    emoji = graphene.Int()
    highlight = graphene.String()
    summary = graphene.String()
    notifs = graphene.List(Notif)

class PeekResponse(graphene.ObjectType):
    topics = graphene.List(Topic)

class PeekRequest(graphene.InputObjectType):
    user_id = graphene.Int()
    app_id = graphene.Int()

class UserResponse(graphene.ObjectType):
    user_id = graphene.Int()

class UserRequest(graphene.InputObjectType):
    username = graphene.String()
    password = graphene.String()

class Query(graphene.ObjectType):
    get_cached_data = graphene.Field(PeekResponse, request=graphene.Argument(PeekRequest))
    get_new_data = graphene.Field(PeekResponse, request=graphene.Argument(PeekRequest))

    def resolve_get_cached_data(self, info, request):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = peek_pb2_grpc.peekServiceStub(channel)
            response = stub.getCachedData(peek_pb2.peekRequest(userID=request.user_id, appID=request.app_id))
        return convert_to_graphql(response)

    def resolve_get_new_data(self, info, request):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = peek_pb2_grpc.peekServiceStub(channel)
            response = stub.getNewData(peek_pb2.peekRequest(userID=request.user_id, appID=request.app_id))
        return convert_to_graphql(response)

class Mutation(graphene.ObjectType):
    add_user = graphene.Field(UserResponse, request=graphene.Argument(UserRequest))
    login_user = graphene.Field(UserResponse, request=graphene.Argument(UserRequest))

    def resolve_add_user(self, info, request):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = peek_pb2_grpc.peekServiceStub(channel)
            response = stub.addUser(peek_pb2.userRequest(username=request.username, password=request.password))
        return UserResponse(user_id=response.userID)

    def resolve_login_user(self, info, request):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = peek_pb2_grpc.peekServiceStub(channel)
            response = stub.loginUser(peek_pb2.userRequest(username=request.username, password=request.password))
        return UserResponse(user_id=response.userID)

def convert_to_graphql(response):
    topics = []
    for t in response.topics:
        notifs = []
        for n in t.notifs:
            notifs.append(Notif(title=n.title, uri=n.uri))
        topic = Topic(name=t.name, emoji=t.emoji, highlight=t.highlight, summary=t.summary, notifs=notifs)
        topics.append(topic)
    return PeekResponse(topics=topics)

schema = graphene.Schema(query=Query, mutation=Mutation)

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run()