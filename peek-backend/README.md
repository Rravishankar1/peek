Starting the server:
python3 server.py

Testing a client request to the server:
python3 testClient.py

server.py implements the gRPC endpoints, and calls compute/switcher.py
switcher directs the call based on the app into the proper fetcher

TODO: Implement fetchers

proto/responseBuilder.py is a wrapper over the gRPC generated classes to generate server responses
Make a responseBuilder(), .addTopic() to add topics, and .build() to create the peekResponse proto

To compile changes to peek.proto:
python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. peek.proto
Then, go into peek_pb2_grpc.py and change line 5 to import protos.peek_pb2 as peek__pb2

npx protoc --ts_out . --proto_path . ./peek.proto
