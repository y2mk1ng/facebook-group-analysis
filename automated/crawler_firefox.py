'''
Author: Yanling Guo (y2mk1ng)
Python version 3.8

Warning: This is not yet finished.
'''

import requests
import pandas
import requests
import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup

## user and browser information; we can open a browser with this
username = input('Your Facebook account (email): ')
passwd = input('Your Facebook password: ')
driver_path = '/home/y2mk1ng/geckodriver-v0.30.0-linux64/geckodriver'
service = Service(driver_path)
browser = '/usr/bin/firefox'
options = Options()
options.binary_location = browser
driver = webdriver.Firefox(service = service, options = options)
driver.get('https://www.facebook.com')
usn = driver.find_element(By.NAME, 'email')
pwd = driver.find_element(By.NAME, 'pass')
submit = driver.find_element(By.NAME, 'login')
usn.send_keys(username)
pwd.send_keys(passwd)
submit.click()

## group information
addr_list = []
group_addr = input('The address of the Facebook group (or anything within, e.g. Members) you want: ')
if 'https://www.facebook.com/groups' in group_addr:
    addr_list.append(group_addr)
    #print(addr_list)
else:
    print('This may not be a facebook group. Process terminated.')


## other information (posts, members, etc.)
date_now = dt.datetime.today().date()

## crawling member information
for index in addr_list:
    group_id = index.split('/')[4]
    a = driver.get(group_addr)
    '''
    #while True:
        #for i in driver.find_elements(By.CLASS_NAME, 'b20td4e0 muag1w35'):
    for i in driver.find_elements(By.CLASS_NAME, 'rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t buofh1pr tgvbjcpo muag1w35 enqfppq2'):
        soup = BeautifulSoup(driver.page_source, 'lxml')
        #for j in soup.find_all('div', 'ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi a8c37x1j'):
        #for j in soup.find('span', 'nc684nl6'):
        for j in soup.find('a', "oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 mg4g778l pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb n00je7tq arfg74bv qs9ysxi8 k77z8yql btwxx1t3 abiwlrkh p8dawk7l q9uorilb lzcic4wl")['content']:
            print(j)
    '''
    bm = driver.find_element(By.CLASS_NAME, 'b20td4e0 muag1w35')
    #soup = BeautifulSoup(driver.page_source)
    #print(soup)
    bm.send_keys(Keys.CONTROL)
    bm.send_keys('a')
    bm.send_keys(Keys.CONTROL)
    bm.send_keys('c')
    bm.send_keys(Keys.TAB)
    with open('member_20220322.txt', 'w') as f:
        bm.send_keys(Keys.CONTROL)
        bm.send_keys('v')
