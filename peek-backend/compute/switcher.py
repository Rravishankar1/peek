import grpc
from protos.peek_pb2 import (
    peekRequest,
    peekResponse
)

import os
from google.cloud import firestore
from google.protobuf.json_format import MessageToDict, ParseDict

current_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = "../keys/peek-credentials.json"
KEY_PATH = os.path.join(current_dir, relative_path)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = KEY_PATH
print("Setting up Firestore client...")
db = firestore.Client()
print("Firestore client setup complete!")

import compute.fetchers.gmail as gmail
import compute.fetchers.instagram as instagram
import compute.fetchers.discord as discord
import compute.fetchers.whatsapp as whatsapp
import compute.fetchers.messenger as messenger
import compute.fetchers.twitter as twitter
import compute.fetchers.reddit as reddit
import compute.fetchers.slack as slack

def direct(request, context, cache):
    response = None
    app = peekRequest.app.Name(request.appID)
    doc_ref = db.collection(app).document(str(request.userID))
    doc = doc_ref.get()

    if cache and doc.exists:
        return ParseDict(doc.to_dict(), peekResponse())
    else:
        cache = False
        match request.appID:
            case peekRequest.GMAIL:
                print("Directing to Gmail fetcher")
                response = gmail.fetch(request.userID, request.token1, request.token2, request.token3, request.token4)
            case peekRequest.INSTAGRAM:
                print("Directing to Instagram fetcher")
                response = instagram.fetch(request.userID)
            case peekRequest.DISCORD:
                print("Directing to Discord fetcher")
                response = discord.fetch(request.userID)
            case peekRequest.WHATSAPP:
                print("Directing to WhatsApp fetcher")
                response = whatsapp.fetch(request.userID)
            case peekRequest.MESSENGER:
                print("Directing to Messenger fetcher")
                response = messenger.fetch(request.userID)
            case peekRequest.TWITTER:
                print("Directing to Twitter fetcher")
                response = twitter.fetch(request.userID)
            case peekRequest.REDDIT:
                print("Directing to Reddit fetcher")
                response = reddit.fetch(request.userID)
            case peekRequest.SLACK:
                print("Directing to Slack fetcher")
                response = slack.fetch(request.userID)
            case _:
                print("Invalid App")

    if response is None:
        context.abort(grpc.StatusCode.INTERNAL, "Could not fetch data for app")
        return None
    
    if not cache:
        doc_ref.delete()
        doc_ref.set(MessageToDict(response))
        print("Response data cached to Firestore")

    return response
