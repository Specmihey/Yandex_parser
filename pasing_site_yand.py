# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 11:45:15 2018
Парсинг всех страниц сайта с получением алиасов и title страниц из индекса Яндекс V2.1
Парсится:Title, Description, URL, находящиеся в индексе Яндекса.
@author: @specmihey
"""
url_site = 'https://best-deal.su/' #The test site
base_url = (('https://www.yandex.ru/search/?lr=19&text=site%3A')) 
#Here we use the extended search string
#Change the line operators for your search
#=========== Downloading libraries
import os
os.chdir('C:\\Users\\user\\Desktop\\Python\\Парсинг сайта алиасы') #Your working directory
import urllib.request
import requests
import re
import openpyxl
import csv
import xlwt
import pandas as pd
import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
baseU = base_url+url_site
#=============== Here is your file chromedriver.exe
browser = webdriver.Chrome('C:\\Users\\user\\Desktop\\Python\\Парсинг сайта алиасы\\chromedriver_win32\\chromedriver.exe')
browser.implicitly_wait(2)
#=== Running the program
browser.get(baseU)
page_count = 0
url_pages = []   
titlePages = [] 
descrPages = []
while True:
    page_count += 1
    time.sleep(1)
    urlNum = browser.find_elements_by_class_name('organic__url') #len(urlNum)
    titleP = browser.find_elements_by_class_name('organic__url-text') #len(titleP)
    desPages = browser.find_elements_by_class_name('organic__text')
    for p in urlNum:
        url_pages.append(p.get_attribute('href'))
    for l in titleP:
        titlePages.append(l.text)
    for mi in desPages:
        descrPages.append(mi.text)
    try:
        # Clicking on "2" on pagination on first iteration, "3" on second...
        browser.find_element_by_link_text('дальше').click()
    except NoSuchElementException:
        # Stop loop if no more page available
        break

# ---- Write data to a file
url_set = pd.DataFrame(url_pages)        
title_set = pd.DataFrame(titlePages)
descr_set = pd.DataFrame(descrPages)
browser.quit() 
UT = pd.DataFrame()
UT = pd.concat([title_set,descr_set,url_set],sort=False,axis=1)
UT.columns = ['Title','Description','URL']
UT.to_excel('site.xls', index=False)  
import winsound
winsound.MessageBeep() 




