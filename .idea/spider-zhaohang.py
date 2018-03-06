#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
import time
from bs4 import BeautifulSoup

driver = webdriver.Ie()
driver.get("https://custody.ebank.cmbchina.com/ccss/default.aspx")