from protos.responseBuilder import responseBuilder
import os
from dotenv import load_dotenv

import tweepy

load_dotenv()
API_KEY = os.getenv('TWITTER_API_KEY')
SECRET_KEY = os.getenv('TWITTER_SECRET_KEY')
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

client = tweepy.Client(bearer_token=BEARER_TOKEN)


def fetch(userID):
    print("Fetching Twitter data for user: " + str(userID))
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