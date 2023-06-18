import grpc
from protos.peek_pb2 import (
    peekRequest,
)

import compute.fetchers.gmail as gmail
import compute.fetchers.instagram as instagram
import compute.fetchers.discord as discord
import compute.fetchers.whatsapp as whatsapp
import compute.fetchers.messenger as messenger
import compute.fetchers.twitter as twitter

def direct(request, context):
    response = None
    match request.appID:
        case peekRequest.GMAIL:
            print("Directing to Gmail fetcher")
            response = gmail.fetch(request.userID, request.token1, request.token2, request.token3,)
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
        case _:
            print("Invalid App")

    if response is None:
        context.abort(grpc.StatusCode.INTERNAL, "Could not fetch data for app")
    return response
