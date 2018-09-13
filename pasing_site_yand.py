# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 17:18:14 2018
Парсинг всех страниц сайта с получением алиасов и title страниц из индекса Яндекс
@author: @specmihey
"""
#url_site = 'ваш_сайт'
url_site = 'https://delfi32.ru'
emailYandex = 'estetm2014@yandex.ru'
passYand = 'tr5c7Fg3xP'

import os
os.chdir('C:\\Users\\user\\Desktop\\Python\\Парсинг сайта алиасы') 
import urllib.request
import requests
import re
import openpyxl
import csv
from pandas import ExcelWriter
from pandas import ExcelFile
import xlwt
import pandas as pd
import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
base_url = (('https://www.yandex.ru/search/?lr=19&text=site%3A'))
baseU = base_url+url_site

#=============== Login
browser = webdriver.Chrome('C:\\Users\\user\\Desktop\\Python\\Парсинг сайта алиасы\\chromedriver_win32\\chromedriver.exe')
browser.implicitly_wait(2)
browser.get('https://www.yandex.ru/')
enterYandex = browser.find_element_by_link_text('Войти в почту')
enterYandex.click()
loginYand = browser.find_element_by_name('login')
loginYand.click()
loginYand.send_keys(emailYandex)
passS = browser.find_element_by_name('passwd')
passS.click()
passS.send_keys(passYand, Keys.ENTER)
time.sleep(5)

browser.get(baseU)
amountValues = browser.find_element_by_class_name('serp-adv__found')
amountValues = amountValues.text
amountPages = int(re.search(r'\d+', amountValues).group())
#amountValues.split( )
#Out[39]: ['Нашлось', '757', 'результатов']

#amountValues_v.isnumeric()
amountPages15 = amountPages/15
Pages = int(amountPages15)
NumberPages = [] # list
if Pages > 0:
    for i in range(0,Pages+1):
        NumberPages.append(i)
else:
    NumberPages = 0
    
baseURL = baseU + '&p='
PagesAll = []
for i in NumberPages:
    PagesAll.append(baseURL+str(i))
    
#============================= selenium
rase = []   
titlePages = []   
for i in PagesAll:
    browser.get(i)
    time.sleep(1)
    urlNum = browser.find_elements_by_class_name('organic__url') #len(urlNum)
    titleP = browser.find_elements_by_class_name('organic__url-text') #len(titleP)
    for p in urlNum:
        rase.append(p.get_attribute('href'))
    for l in titleP:
        titlePages.append(l.text)    
url_set = pd.DataFrame(rase)        
title_set = pd.DataFrame(titlePages)
browser.quit() 
UT = pd.DataFrame()
UT = pd.concat([title_set,url_set],sort=False,axis=1)
UT.columns = ['Title','URL']
UT.to_excel('site.xls', index=False)  
import winsound
winsound.MessageBeep()



#browser.text
#urlNum = browser.find_elements_by_class_name('organic__url')
#rase = urlNum[1].get_attribute('href')
#browser.quit()














   