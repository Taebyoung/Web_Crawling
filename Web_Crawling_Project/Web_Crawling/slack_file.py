
import os
import slack

def send_file():
    path = os.path.dirname(os.path.realpath(__file__))
    client = slack.WebClient(token="<your_slack_token>")
    client.files_upload(channels = '#data', file = "{}/weather.png".format(path))
