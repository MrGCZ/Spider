#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
import time
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.get("https://custodian.chinaclear.cn/login.jsp")
pingtai=driver.find_element_by_id('ptzh')
username=driver.find_element_by_id('userCode')
password=driver.find_element_by_id('pwd')
login_button=driver.find_element_by_xpath(".//*[@id='loginForm']/div/div/div/a[1]")
pingtai.send_keys("foundersc")
username.send_keys("xiaohonghong")
password.send_keys("123456")
login_button.click()
driver.implicitly_wait(10)
time.sleep(5)
login_button1=driver.find_element_by_xpath(".//*[@id='J_ui-layout-left_list']/ul/li[2]/span/b") #账户资金查询
login_button1.click()
time.sleep(1)
login_button2=driver.find_element_by_xpath(".//*[@id='faZhyemxcx']") #账户明细查询
login_button2.click()
time.sleep(5)
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'faZhyemxcx')]"))


'''
htm_const=driver.page_source
soup=BeautifulSoup(htm_const,'html.parser',from_encoding='utf-8')

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'faHkzlcx')]"))


htm_const1=driver.page_source
soup=BeautifulSoup(htm_const1,'html.parser',from_encoding='utf-8')
infos=soup.find_all(class_="ui-widget-content jqgrow ui-row-ltr")
print infos
data1=[]
for info in infos:
    data1.append(info.find(attrs={"aria-describedby":"gridTable_hklbname"}).string)
print data1
'''


