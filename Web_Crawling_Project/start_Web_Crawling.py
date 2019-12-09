
# !./run.sh

import numpy as np
import pandas as pd
import time

from Web_Crawling import *

diction = mongodb.client.diction.english

QUERY = {}
items = diction.find(QUERY)
dfs = pd.DataFrame(items)
list = np.random.choice(range(len(dfs)), 3)
for i in list:
    df = dfs.loc[i]
    
    msg1 = make_msg.make_msg(df, "단어")
    msg2 = make_msg.make_msg(df, "뜻")
    msg3 = make_msg.make_msg(df, "문법")
    msg4 = make_msg.make_msg(df, "문장예시")
    msg5 = make_msg.make_msg(df, "반의어")
    msg6 = make_msg.make_msg(df, "복합어・숙어")
    msg7 = make_msg.make_msg(df, "유의어")
    msg8 = make_msg.make_msg(df, "테마 단어")
    msg9 = make_msg.make_msg(df, "파생어")
    msg = msg1 + msg2 + msg3 + msg4 + msg5 + msg6 + msg7 + msg8 + msg9
    slack_msg.send_msg(msg)

df = pd.read_csv("Web_Crawling/news/news.csv")
msg = ""
for i in range(6):
    msg += "==============================\n{} :\n1. {} :\n{}\n2. {} :\n{}\n3. {} :\n{}\n4. {} :\n{}\n5. {} :\n{}\n".format(
        df["category"][i], df["title1"][i], df["link1"][i],
        df["title2"][i], df["link2"][i],
        df["title3"][i], df["link3"][i],
        df["title4"][i], df["link4"][i],
        df["title5"][i], df["link5"][i],
    )
slack_msg.send_msg(msg)
time.sleep(2)
weather.weather()
time.sleep(2)
slack_file.send_file()
