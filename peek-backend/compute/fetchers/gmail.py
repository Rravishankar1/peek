from protos.responseBuilder import responseBuilder
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import time

def fetch(userID, token1):
    print("Fetching Gmail data for user: " + str(userID))
    response = responseBuilder()

    # TODO FETCH DATA HERE AND ADD TO RESPONSE
    recent_messages = get_unopened_emails_last_2_hours(token1)
    return recent_messages

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


def get_gmail_service(access_token):
    creds = Credentials.from_authorized_user_info(info={"access_token": access_token})
    service = build('gmail', 'v1', credentials=creds)
    return service

def get_unopened_emails_last_2_hours(access_token, user_id='me'):
    service = get_gmail_service(access_token)
    two_hours_ago_ms = int((time.time() - 2 * 60 * 60) * 1000)  # Convert to milliseconds
    query = f'is:unread after:{two_hours_ago_ms}'
    results = service.users().messages().list(userId=user_id, q=query).execute()
    message_ids = results.get('messages', [])
    
    messages = []  # Create a list to store message details
    for message_id in message_ids:
        message = service.users().messages().get(userId=user_id, id=message_id['id']).execute()
        messages.append(message)  # Append each message's details to the list
    
    return messages
