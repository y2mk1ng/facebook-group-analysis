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

## crawling member information
for index in addr_list:
    group_id = index.split('/')[4]
    a = driver.get(group_addr)
    print(a)
    time.sleep(2)
    wait = WebDriverWait(driver, 10)
    ## search the contents of a specific group member
    #button = driver.find_element(By.XPATH, '//div[@class="n00je7tq arfg74bv qs9ysxi8 k77z8yql i09qtzwb n7fi1qx3 b5wmifdl hzruof5a pmk7jnqg j9ispegn kr520xx4 c5ndavph art1omkt ot9fgl3s rnr61an3"]')
    #button = driver.find_element(By.CLASS_NAME, 'l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv tdjehn4e tv7at329 hv4rvrfc dati1w0a') ### still not yet working though
    button = driver.find_element(By.CSS_SELECTOR, '.transform')
    button.click()
    #frame = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type = "search"]')))
    search = driver.find_element(By.XPATH, '//input[@placeholder="Search Facebook"]') ## This should lead to the overall search on Facebook. So try "Search this group instead. It might work.
    #search = driver.switch_to.frame(frame)
    search.send_keys('朱玟希')
    search.send_keys(Keys.ENTER)
