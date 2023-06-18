To run: npm start

In https://studio.apollographql.com/sandbox/explorer

Example Request:

Operation:
query getNewData($request: peekRequest) {
  getNewData(request: $request) {
    topics {
      name
      emoji
      highlight
      summary
      notifs {
        title
        uri
      }
    }
  }
}

Variable:
{
  "request": {
    "userID": 21,
    "appID": "INSTAGRAM"
  }
}