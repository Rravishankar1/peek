from protos.responseBuilder import responseBuilder

def fetch(userID):
    print("Fetching WhatsApp data for user: " + str(userID))
    response = responseBuilder()
    

    # TODO FETCH DATA HERE AND ADD TO RESPONSE

    response.addTopic(
        name="testTopic",
        highlight="testHighlight",
        summary="testSummary",
        notifs=[
            {
                "title": "testTitle1",
                "uri": "testURI1"
            },
            {
                "title": "testTitle2",
                "uri": "testURI2"
            }
        ]
    )
    return response.build()