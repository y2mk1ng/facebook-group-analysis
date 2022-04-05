'''
Author: Yanling Guo (y2mk1ng)
Python version 3.8

Warning: This is not yet finished.
'''

import requests
import pandas
import requests
import time
import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
group_addr = input('The address of the Facebook group (or anything related) you want: ')
if 'https://www.facebook.com/groups' in group_addr:
    addr_list.append(group_addr)
    #print(addr_list)
else:
    print('This may not be a facebook group. Process terminated.')


## other information (posts, members, etc.)
date_now = dt.datetime.today().date()

## searching for a member and crawling their activities
for index in addr_list:
    group_id = index.split('/')[4]
    a = driver.get(group_addr)
    print(a)
    time.sleep(2)
    wait = WebDriverWait(driver, 10)
    ## search the contents of a specific group member
    button = driver.find_element(By.XPATH, '//div[@aria-label="Search"]')
    button.click()
    search = driver.find_element(By.XPATH, '//input[@aria-label="Search this group"]')
    WebDriverWait(driver, 10)
    member_searched = input('Enter the member you want to search: ')
    search.send_keys(member_searched)
    search.send_keys(Keys.ENTER)
