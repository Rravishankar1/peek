import requests
import json
API_KEY = "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"
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

def organize_topics(topics, app_name):
    #returns {"topic1": [1, 2, ...], "topic2":[3,..]} etc.
    ask= f"Please organize the following id numbers of each subject line from {app_name} into up to 5 discernable groups in a json format (like this: 'topic1: [id1, id2,...]| topic 2: [id3, ...]') in order of decreasing priority by group. Use less groups if it fits better:"
    system_message = {"role": "system", "content": "You are a categorizer of short messages."}
    enumerated_topics = [f"id: {i} - " + topics[i] for i in range(len(topics))]
    info = ",".join(enumerated_topics)
    user_message = {"role": "user", "content": ask + info}
    response = generate_chat_completion([system_message, user_message])
    return json.loads(response)

def summarize(topic, messages, app_name):
    ask= f"Given a list of notification messages from {app_name} that all have to do with {topic}, return a summary and highlight of the most extreme aspect (highlight must be around 10 words) in a json format: (like this: 'summary: longer text, highlight: shorter text')"
    system_message = {"role": "system", "content": "You are a concise and informative summarizer."}
    info = ",".join(messages)
    user_message = {"role": "user", "content": ask + info}
    response = generate_chat_completion([system_message, user_message])
    return json.loads(response)

def sort_priority(topics, summaries):
    

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

responseString = organize_topics(["9 new jobs for 'software intern fall 2023 - Jun 17", "Are Ivy Leagues better than state schools?", "2 new jobs for 'software engineer intern'", "Codeforces Round 880", "Stay cool and safe this summer"], "gmail")
print(responseString)


