import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
API_KEY = os.getenv('OPENAI_API_KEY')

def organize_topics(topics, app_name):
    #returns {"topic1": [1, 2, ...], "topic2":[3,..]} etc.
    ask= f"Please group the following id numbers of each subject line from {app_name} into up to 5 topic names in a json format (like this: 'topic1: [int(id1), int(id2),...]| topic 2: [int(id3), ...]') in order of decreasing priority by group. Use less groups if it fits better:\n"
    system_message = {"role": "system", "content": "You are a categorizer of short messages."}
    enumerated_topics = [f"id: {i} - " + topics[i] for i in range(len(topics))]
    info = "\n".join(enumerated_topics)
    user_message = {"role": "user", "content": ask + info}
    response = generate_chat_completion([system_message, user_message], model="gpt-4", temperature=0.3)
    return json.loads(response)

def summarize(topic, messages, app_name):
    ask= f"Given a list of notification messages from {app_name} that all have to do with {topic}, return a summary and highlight of the most extreme aspect (highlight must be around 10 words) in a json format: (like this: 'summary: longer text, highlight: shorter text')\n"
    system_message = {"role": "system", "content": "You are a concise and informative summarizer. If given a notification from email, try to disregard html tags."}
    info = "\n".join(messages)
    user_message = {"role": "user", "content": ask + info}
    response = generate_chat_completion([system_message, user_message], model="gpt-4", temperature = 0.7)
    return json.loads(response)

# def sort_priority(topics, summaries):
#     ...

def generate_chat_completion(messages, model="gpt-4", temperature=1, max_tokens = None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

#responseString = organize_topics(["9 new jobs for 'software intern fall 2023 - Jun 17", "Are Ivy Leagues better than state schools?", "2 new jobs for 'software engineer intern'", "Codeforces Round 880", "Stay cool and safe this summer"], "gmail")
#print(responseString)


