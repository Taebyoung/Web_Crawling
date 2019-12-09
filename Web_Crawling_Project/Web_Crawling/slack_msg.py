
import requests
import json

def send_msg(msg):
    WEBHOOK_URL = "<slack url>"
    payload = {
        "channel" : "#data",
        "username" : "AI_[ jupyter ]",
        "text" : msg,
    }
    requests.post(WEBHOOK_URL, json.dumps(payload))
