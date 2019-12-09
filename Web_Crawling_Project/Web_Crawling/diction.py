
import os
import pandas as pd

from selenium import webdriver

def open_driver(driver, name):
    driver.find_element_by_css_selector("#q").clear()
    driver.find_element_by_css_selector("#q").send_keys(name)
    driver.find_element_by_css_selector("#daumBtnSearch > span").click()
    try:
        driver.find_element_by_css_selector("#mArticle > div.search_cont > div:nth-child(3) > div:nth-child(2) > div.cleanword_type.kuek_type > div.search_cleanword > strong > a > span").click()
        many_means = True
    except:
        many_means = False

def find_dic(driver, dic):
    ## 단어 명, 단어 뜻
    name = driver.find_element_by_css_selector("#mSub > div > div.clean_word > h3 > span.txt_cleanword").text
    means = driver.find_elements_by_css_selector("#mSub > div > ul > li")

    mean_ls = []
    for mean in means:
        mean_ls.append(mean.text)

    ## 문법
    try:
        mmss = driver.find_elements_by_css_selector("#mArticle > div.detail_cont > div.cont_left > div.card_word.card_sort.card_furigana > div > div")
        m = []
        for mmsl in mmss:
            m_c = mmsl.find_element_by_css_selector("div > strong").text
            m.append(m_c)
            mms = mmsl.find_elements_by_css_selector("ul > li")
            for mm in mms:
                mml = mm.find_element_by_css_selector("span").text
                num = len(mml)
                mmt = mm.text[num:]
                m.append(str(mml) + " : " + str(mmt))
    except:
        m = -1

    dic.update({
        "단어" : name,
        "뜻" : mean_ls,
        "문법" : m,
    }) 
    
    #mArticle > div.detail_cont > div.cont_left > div.card_word.card_relation.card_furigana > div:nth-child(1)
    anothers = driver.find_elements_by_css_selector("#mArticle > div.detail_cont > div.cont_left > div.card_word.card_relation.card_furigana > div")
    for another in anothers:
        another_title = another.find_element_by_css_selector("div > strong").text
        key = another.find_element_by_css_selector("div > span").text
        if int(key[:-1]) > 5:
            key = 5
        else :
            key = int(key[:-1])

        another_ls = []
        another_exs = another.find_elements_by_css_selector("ul > li")
        for i in range(key):
            another_ls.append(another_exs[i].text.replace("\n", ' '))

        dic.update({
            another_title : another_ls
        })
    
    btns = driver.find_elements_by_css_selector("a.btn_ex")
    for btn in btns:
        btn.click()
    
    #mArticle > div.detail_cont > div.cont_left > div:nth-child(3) > div.box_word.fold_open > div:nth-child(4) > ul:nth-child(4) > li:nth-child(2) > p:nth-child(1)
    dirs = driver.find_elements_by_css_selector("p.desc_ex")
    
    exams = []
    count = 0
    for dirt in dirs:
        if count == 40:
            break
        count += 1
        
        dir_text = dirt.text
        if dir_text[-2:] == "듣기":
            dir_text = dir_text[:-3]
        exams.append(dir_text)

    dic.update({
        "문장예시" : exams
    })