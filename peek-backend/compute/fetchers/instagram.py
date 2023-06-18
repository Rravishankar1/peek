from protos.responseBuilder import responseBuilder

def fetch(userID):
    print("Fetching Instagram data for user: " + str(userID))
    response = responseBuilder()

    # TODO FETCH DATA HERE AND ADD TO RESPONSE

    response.addTopic(
        name="work",
        highlight="testHighlight",
        summary="You suck dick",
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
    ).addTopic(
        name="work",
        highlight="testHighlight",
        summary="Once upon a time, in a world brimming with vibrant colors and joyous melodies, there existed a place where happiness overflowed like a cascading waterfall, spreading its warmth to every corner of existence. In this idyllic realm, where laughter danced upon the air and smiles were as plentiful as the stars, a profound sense of bliss enveloped the hearts of its inhabitants.",
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