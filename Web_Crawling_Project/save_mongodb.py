
import pandas as pd
import os

from selenium import webdriver
from Web_Crawling import mongodb as md
from Web_Crawling import diction as dt

path = os.path.dirname(os.path.realpath(__file__))
dic_list = pd.read_csv("{}/Web_Crawling/eng.csv".format(path), encoding = "euc-kr")
dic_ls = list(dic_list["eng"])

ls = []

print("시작 ...")

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(options=options)
driver.get("https://dic.daum.net/word/view.do?wordid=ekw000161766&q=study")

print("오픈 ...")

for name in dic_ls:
    print("{} 단어 찾는중...".format(name))
    dic = {
        "단어" : -1,
        "뜻" : -1,
        "문법" : -1,
        "반의어" : -1,
        "복합어・숙어" : -1,
        "파생어" : -1,
        "유의어" : -1,
        "테마 단어" : -1,
        "문장예시" : -1
    }
    dt.open_driver(driver, name)
    if dic["단어"] == "confirm":
        pass
    else:
        try :
            dt.find_dic(driver, dic)
            md.collection.insert(dic)
            ls.append(dic)
        except:
            pass
    
driver.quit()

df = pd.DataFrame(ls)

df["복합어 숙어"] = df["복합어・숙어"]
df = df.drop(columns = "복합어・숙어")

df.to_csv("{}/diction.csv".format(path), index = False, encoding = "euc-kr")
