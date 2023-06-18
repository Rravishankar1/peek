from protos.responseBuilder import responseBuilder

import requests
import os
from dotenv import load_dotenv
from collections import defaultdict
from compute.ml.openai import organize_topics, summarize

load_dotenv()
API_TOKEN = os.getenv('DISCORD_API_TOKEN')
base_url = "https://discord.com/api"
guild_id = "1119794281054482473"
channels_url = f"{base_url}/guilds/{guild_id}/channels"


def fetch(userID):
    print("Fetching Discord data for user: " + str(userID))
    response = responseBuilder()

    headers = {
        "Authorization": f"Bot {API_TOKEN}"
    }

    channels = requests.get(channels_url, headers=headers).json()
    organizeGPTInput = []
    messages = []
    for channel in channels:
        if (channel["type"] == 0):
            channelName = channel["name"]
            channelID = channel["id"]
            msgs = requests.get(f"{base_url}/channels/{channelID}/messages?limit=10", headers=headers)
            if (msgs.status_code != 200):
                return None
            msgs = msgs.json()
            for message in msgs:
                content = message["content"]
                if (content == ""):
                    continue
                timestamp = message["timestamp"]
                author = message["author"]["username"]
                messages.append({
                    "channel": channelName,
                    "timestamp": timestamp,
                    "author": author,
                    "content": content,
                    "uri": f"https://discord.com/channels/{guild_id}/{channelID}/{message['id']}"
                })
                organizeGPTInput.append(f"Channel: {channelName} | {author}: {content}")
    responseString = organize_topics(organizeGPTInput, "Discord")
    for topic in responseString:
        summarizeGPTInput = []
        notifs = []
        for i in responseString[topic]:
            summarizeGPTInput.append(f"Channel: {messages[i]['channel']} | {messages[i]['author']}: {messages[i]['content']}")
            notifs.append({
                "title": f"#{messages[i]['channel']} | {messages[i]['author']}: {messages[i]['content']}",
                "uri": messages[i]["uri"]
            })
        summarized = summarize(summarizeGPTInput, topic, "Discord")
        response.addTopic(
            name=topic,
            highlight=summarized["highlight"],
            summary=summarized["summary"],
            notifs=notifs
        )

    return response.build()