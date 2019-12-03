
from selenium import webdriver
from PIL import Image as pil
import time
import os

def weather():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=800x960")
    driver = webdriver.Chrome(options=options)

    driver.get("http://www.kweather.co.kr/forecast/forecast_lifestyle_detail.html?main_map=1&area1=area0&area2=11140000_108")
    driver.execute_script("window.scrollTo(220,317)")
    time.sleep(10)
    print("save")
    path = os.path.dirname(os.path.realpath(__file__))
    driver.save_screenshot("{}/weather.png".format(path))
    driver.quit()
