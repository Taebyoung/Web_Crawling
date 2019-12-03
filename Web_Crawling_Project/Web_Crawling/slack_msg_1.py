
import requests
import json

def send_msg_1(msg):
    WEBHOOK_URL = "<your_slack_url>"
    payload = {
        "channel" : "#data",
        "username" : "AI_[ jupyter ]",
        "text" : msg,
    }
    requests.post(WEBHOOK_URL, json.dumps(payload))
