import slack as sl
import os
from dotenv import load_dotenv
from compute.ml.openai import organize_topics, summarize
from protos.responseBuilder import responseBuilder

load_dotenv()
slack_token = os.getenv("SLACK_API_KEY")
print("Setting up Slack client...")
client = sl.WebClient(token=slack_token)
print("Slack client setup complete!")

workspace_url = "https://peek-3kq7477.slack.com"


def get_username(user_id):
    response = client.users_info(user=user_id)
    
    if response["ok"]:
        return response['user']['name']
    else:
        print(f"Could not get user info: {response['error']}")
        return None

def fetch(userID):
    print("Fetching Slack data for user: " + str(userID))

    messages = []
    organizeGPTInput = []

    response = responseBuilder()

    slackResponse = client.conversations_list()
    for channel in slackResponse['channels']:
        channelId = channel['id']
        channelName = channel['name']
        print(f'Channel: {channelName}')
        
        history = client.conversations_history(channel=channelId, limit=10)
        msgs = history['messages']
        for i, msg in enumerate(msgs, start=1):
            author = get_username(msg['user'])
            timestamp = msg['ts']
            content = msg["text"]
            uri = f"{workspace_url}.slack.com/archives/{channelId}/p{timestamp.replace('.', '')}"

            messages.append({
                "channel": channelName,
                "timestamp": timestamp,
                "author": author,
                "content": content,
                "uri": uri
            })
            organizeGPTInput.append(f"Channel: {channelName} | {author}: {content}")
    print("Organizing with GPT...")
    responseString = organize_topics(organizeGPTInput, "Slack")
    print(responseString)
    for topic in responseString:
        print("Summarizing with GPT...")
        summarizeGPTInput = []
        notifs = []
        for i in responseString[topic]:
            summarizeGPTInput.append(f"Channel: {messages[i]['channel']} | {messages[i]['author']}: {messages[i]['content']}")
            notifs.append({
                "title": f"#{messages[i]['channel']} | {messages[i]['author']}: {messages[i]['content']}",
                "uri": messages[i]["uri"]
            })
        summarized = summarize(summarizeGPTInput, topic, "Discord")
        print(summarized)
        response.addTopic(
            name=topic,
            highlight=summarized["highlight"],
            summary=summarized["summary"],
            notifs=notifs
        )

    return response.build()