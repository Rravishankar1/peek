from protos.responseBuilder import responseBuilder

import requests
import os
from dotenv import load_dotenv
from collections import defaultdict
from compute.ml.openai import organize_topics, summarize



def fetch(userID):
    print("Fetching Reddit data for user: " + str(userID))
    response = responseBuilder()
    messages = []
    organizeGPTInput = []
    # JSON endpoint URL
    url1 = "https://www.reddit.com/r/berkeley/new.json"
    url2 = "https://www.reddit.com/r/internships/new.json"
    url3 = "https://www.reddit.com/r/premed/new.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    resp = requests.get(url1, headers=headers)
    data = resp.json()
    posts = data["data"]["children"][:10]

    for i in range(len(posts)):
        messages.append({
                        "subreddit": posts[i]["data"]["subreddit"],
                        "timestamp": posts[i]["data"]["created_utc"],
                        "author": posts[i]["data"]["author"],
                        "content": posts[i]["data"]["selftext"],
                        "uri": f"https://www.reddit.com{posts[i]['data']['permalink']}"
                    })
        organizeGPTInput.append(f"Subreddit: {posts[i]['data']['subreddit']} | {posts[i]['data']['author']}: {posts[i]['data']['selftext']}")

    resp = requests.get(url2, headers=headers)
    data = resp.json()
    posts = data["data"]["children"][:10]

    for i in range(len(posts)):
        messages.append({
                        "subreddit": posts[i]["data"]["subreddit"],
                        "timestamp": posts[i]["data"]["created_utc"],
                        "author": posts[i]["data"]["author"],
                        "content": posts[i]["data"]["selftext"],
                        "uri": f"https://www.reddit.com{posts[i]['data']['permalink']}"
        })
        organizeGPTInput.append(f"Subreddit: {posts[i]['data']['subreddit']} | {posts[i]['data']['author']}: {posts[i]['data']['selftext']}")

    resp = requests.get(url3, headers=headers)
    data = resp.json()
    posts = data["data"]["children"][:10]

    for i in range(len(posts)):
        messages.append({
                        "subreddit": posts[i]["data"]["subreddit"],
                        "timestamp": posts[i]["data"]["created_utc"],
                        "author": posts[i]["data"]["author"],
                        "content": posts[i]["data"]["selftext"],
                        "uri": f"https://www.reddit.com{posts[i]['data']['permalink']}"
        })
        organizeGPTInput.append(f"Subreddit: {posts[i]['data']['subreddit']} | {posts[i]['data']['author']}: {posts[i]['data']['selftext']}")

    print("Organizing with GPT...")
    responseString = organize_topics(organizeGPTInput, "Reddit")
    print(responseString)
    for topic in responseString:
        summarizeGPTInput = []
        notifs = []
        for i in responseString[topic]:
            summarizeGPTInput.append(f"Subreddit: {messages[i]['subreddit']} | {messages[i]['author']}: {messages[i]['content']}")
            notifs.append({
                "title": f"#{messages[i]['subreddit']} | {messages[i]['author']}: {messages[i]['content']}",
                "uri": messages[i]["uri"]
            })
        summarized = summarize(summarizeGPTInput, topic, "Reddit")
        print(summarized)
        response.addTopic(
            name=topic,
            highlight=summarized["highlight"],
            summary=summarized["summary"],
            notifs=notifs
        )

    return response.build()

