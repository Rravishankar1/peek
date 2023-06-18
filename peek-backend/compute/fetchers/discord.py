from protos.responseBuilder import responseBuilder

import requests

API_TOKEN = "MTExOTc5NTIyMTQ3NjE2Nzc2MA.GQhHWk.JjXVNt4pRK5tNMM29rCqhIEpZGZY52ug1YtK68"
base_url = "https://discord.com/api"
guild_id = "1119794281054482473"
channels_url = f"{base_url}/guilds/{guild_id}/channels"


def fetch(userID):
    print("Fetching Discord data for user: " + str(userID))

    headers = {
        "Authorization": f"Bot {API_TOKEN}"
    }

    channels = requests.get(channels_url, headers=headers).json()
    for channel in channels:
        if (channel["type"] == 0):
            print(channel["name"])
            messages = requests.get(f"{base_url}/channels/{channel['id']}/messages?limit=10", headers=headers).json()
            for message in messages:
                content = message["content"]
                if (content == ""):
                    continue
                timestamp = message["timestamp"]
                author = message["author"]["username"]
                print(f"{timestamp} - {author}: {content}")
            print("")


    response = responseBuilder()

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
    return response.getTestResponse()