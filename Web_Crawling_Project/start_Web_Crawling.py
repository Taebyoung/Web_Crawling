
import pandas as pd
import time
import os

from Web_Crawling import *

path = os.path.dirname(os.path.realpath(__file__))


df = pd.read_csv("{}/Web_Crawling/news/news.csv".format(path))
msg = ""
for i in range(6):
    msg += "==============================\n{} :\n1. {} :\n{}\n2. {} :\n{}\n3. {} :\n{}\n4. {} :\n{}\n5. {} :\n{}\n".format(
        df["category"][i], df["title1"][i], df["link1"][i],
        df["title2"][i], df["link2"][i],
        df["title3"][i], df["link3"][i],
        df["title4"][i], df["link4"][i],
        df["title5"][i], df["link5"][i],
    )
slack_msg_1.send_msg_1(msg)
time.sleep(2)
weather.weather()
time.sleep(2)
slack_file.send_file()
