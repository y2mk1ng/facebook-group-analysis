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

## user and browser information
username = input('Your Facebook account (email): ')
passwd = input('Your Facebook password: ')
page_list = list()
driver_path = '/home/y2mk1ng/geckodriver-v0.30.0-linux64/geckodriver'
#s = Service(driver_path)
browser = '/usr/bin/firefox'
options = Options()
options.binary_location = browser
service = Service(driver_path)
driver = webdriver.Firefox(service = service, options = options)
driver.get('https://www.facebook.com')
usn = driver.find_element(By.NAME, 'email')
pwd = driver.find_element(By.NAME, 'pass')
submit = driver.find_element(By.NAME, 'login')
usn.send_keys(username)
pwd.send_keys(passwd)
submit.click()

## group information
group_addr = input('The address of the Facebook group you want: ')
