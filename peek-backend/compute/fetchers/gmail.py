from protos.responseBuilder import responseBuilder
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import time
import mindsdb_sdk
import email
import base64
from pyairtable import Api, Base, Table
import os 
from dotenv import load_dotenv
from compute.ml.openai import organize_topics, summarize
import re

load_dotenv()
AIRTABLE_KEY = os.getenv('AIRTABLE_API_KEY')
MINDSDB_PW = os.getenv('MINDSDB_PASSWORD')
GMAIL_ACCESS = os.getenv('GMAIL_ACCESS_TOKEN')
GMAIL_REFRESH = os.getenv('GMAIL_REFRESH_TOKEN')
GMAIL_CLIENTID = os.getenv('GMAIL_CLIENT_ID')
GMAIL_SECRET = os.getenv('GMAIL_CLIENT_SECRET')

table = Table(AIRTABLE_KEY, 'app94elbP4BNe2dsY', 'tbltPSysCiL0KdC48')

print("Setting up Gmail client...")
#server = mindsdb_sdk.connect('https://cloud.mindsdb.com', login='thomasychen@berkeley.edu', password=MINDSDB_PW)
#mindsdb_airtable = server.get_database('airtable_datasource')
#project = server.get_project()
#my_table = mindsdb_airtable.get_table('Emails')
#my_model = project.get_model("peek_gpt_model_4")
clean = re.compile('<.*?>')
bs = re.compile('\\\\.?')
print("Gmail client setup complete!")

def fetch(userID, token1, token2, token3, token4):
    print("Fetching Gmail data for user: " + str(userID))
    #response = responseBuilder()

    # TODO FETCH DATA HERE AND ADD TO RESPONSE
    recent_messages, ids = get_unopened_emails_last_2_hours(GMAIL_ACCESS, GMAIL_REFRESH, GMAIL_CLIENTID, GMAIL_SECRET)
    if len(recent_messages) == 0:
        return None
    subjects = []
    cleaned_email_bodies = []
    for raw_message, content in recent_messages:
        email_meta = email.message_from_bytes(
            base64.urlsafe_b64decode(raw_message['raw'])
        )
        subject = email_meta["Subject"]
        address = email_meta["To"]
        sender = email_meta["From"]
        subjects.append(f"From:{sender}, To: {address} -- Subject: " + str(subject))
        no_html = re.sub(clean, "", str(content))
        no_bs = re.sub(bs, "", no_html)
        no_space = re.sub(" +", " ", no_bs)
        no_long_strings = re.sub('\S{20,}', '',no_space)
        cleaned_email_bodies.append(no_long_strings)
    #     table.create({"Sender": str(sender), "Address": str(address), "Subject": str(subject), "Body": str(content), "UserID": str(userID)})
    # cleaned_email_bodies = my_model.predict(my_table.limit(10))
    # for records in table.iterate(page_size=10, max_records=1000):
    #     ids = [record["id"] for record in records]
    #     table.batch_delete(ids)
    
    topicResponse = organize_topics(subjects, "Gmail")
    for topic in topicResponse: 
        summarizeGPTInput = []
        notifs = []
        for i in topicResponse[topic]:
            summarizeGPTInput.append(f"{subjects[int(i)]} | {cleaned_email_bodies[int(i)]}")
            notifs.append({
                "title": f"{subjects[int(i)]}",
                "uri": f"https://mail.google.com/mail/u/0/#label/all/{ids[int(i)]}" #link might not work LOL
            })
        summarized = summarize(summarizeGPTInput, topic, "Gmail")
        print(topic, summarized["highlight"], summarized["summary"], notifs)
        response.addTopic(
            name=topic,
            highlight=summarized["highlight"],
            summary=summarized["summary"],
            notifs=notifs
        )

    return response.build()


def get_gmail_service(access_token, refresh_token, client_id, client_secret):
    creds = Credentials.from_authorized_user_info(info={"access_token": access_token, "client_secret": client_secret, 
    "client_id":client_id, "refresh_token":refresh_token}, scopes=["https://www.googleapis.com/auth/gmail.readonly"])
    service = build('gmail', 'v1', credentials=creds)
    return service

def get_unopened_emails_last_2_hours(access_token, refresh_token, client_id, client_secret, user_id='me'):
    service = get_gmail_service(access_token, refresh_token, client_id, client_secret)
    query = f'is:unread newer_than:5h to:me'
    results = service.users().messages().list(userId=user_id, q = query).execute()
    message_ids = results.get('messages', [])
    messages = []  # Create a list to store message details
    ids = []
    for message_id in message_ids:
        ids.append(message_id["id"])
        raw_message = service.users().messages().get(userId=user_id, id=message_id['id'], format="raw", metadataHeaders=None).execute()
        message_full = service.users().messages().get(userId=user_id, id=message_id['id']).execute()
        email_content = ""
        if 'data' in message_full['payload']['body'].keys():
            email_content += message_full['payload']['body']['data']
        else: 
            for part in message_full['payload']['parts']:
                email_content = email_content + part['body']['data'] 
        test = bytes(str(email_content),encoding='utf-8')
        email_content = base64.urlsafe_b64decode(test)
        messages.append((raw_message, email_content))  # Append each message's details to the list
    
    return messages, ids