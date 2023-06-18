const { ApolloServer, gql } = require('apollo-server');
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

const PROTO_PATH = __dirname + "/../peek-backend/protos/peek.proto";

const protoOptions = {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true
}

const packageDefinition = protoLoader.loadSync(PROTO_PATH, protoOptions);
const peekService = grpc.loadPackageDefinition(packageDefinition).peek.peekService;

const client = new peekService('localhost:50051', grpc.credentials.createInsecure());

const typeDefs = gql`
  enum app {
    GMAIL
    INSTAGRAM
    DISCORD
    WHATSAPP
    MESSENGER
    TWITTER
    REDDIT
  }

  type notif {
    title: String
    uri: String
  }

  type topic {
    name: String
    emoji: String
    highlight: String
    summary: String
    notifs: [notif]
  }

  type peekResponse {
    topics: [topic]
  }

  type userResponse {
    userID: Int
  }

  input peekRequest {
    userID: Int
    appID: app
    token1: String
    token2: String
    token3: String
    token4: String
    token5: String
  }

  input userRequest {
    username: String
    password: String
  }

  type Query {
    getCachedData(request: peekRequest): peekResponse
    getNewData(request: peekRequest): peekResponse
  }

  type Mutation {
    addUser(request: userRequest): userResponse
    loginUser(request: userRequest): userResponse
  }
`;

const resolvers = {
  Query: {
    getCachedData: (_, { request }) => {
      return new Promise((resolve, reject) => {
        client.getCachedData(request, (error, response) => {
          if (error) {
            reject(error);
          } else {
            resolve(response);
          }
        });
      });
    },
    getNewData: (_, { request }) => {
      return new Promise((resolve, reject) => {
        client.getNewData(request, (error, response) => {
          if (error) {
            reject(error);
          } else {
            resolve(response);
          }
        });
      });
    }
  },
  Mutation: {
    addUser: (_, { request }) => {
      return new Promise((resolve, reject) => {
        client.addUser(request, (error, response) => {
          if (error) {
            reject(error);
          } else {
            resolve(response);
          }
        });
      });
    },
    loginUser: (_, { request }) => {
      return new Promise((resolve, reject) => {
        client.loginUser(request, (error, response) => {
          if (error) {
            reject(error);
          } else {
            resolve(response);
          }
        });
      });
    }
  }
};

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});