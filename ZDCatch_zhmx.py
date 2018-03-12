#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup
import re

def zd_catch():
    driver = webdriver.Firefox()
    driver.get("https://custodian.chinaclear.cn/login.jsp")
    pingtai = driver.find_element_by_id('ptzh')
    username = driver.find_element_by_id('userCode')
    password = driver.find_element_by_id('pwd')
    login_button = driver.find_element_by_xpath(".//*[@id='loginForm']/div/div/div/a[1]")
    pingtai.send_keys("foundersc")
    username.send_keys("xiaohonghong")
    password.send_keys("123456")
    login_button.click()
    driver.implicitly_wait(10)
    time.sleep(5)
    login_button1 = driver.find_element_by_xpath(".//*[@id='J_ui-layout-left_list']/ul/li[2]/span")  # 账户资金查询
    login_button1.click()
    time.sleep(1)
    login_button2 = driver.find_element_by_xpath(".//*[@id='faZhyemxcx']")  # 账户明细查询
    login_button2.click()
    time.sleep(5)
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'faZhyemxcx')]"))
    login_button4 = driver.find_element_by_xpath("html/body/div[1]/div[6]/div/img[1]")  #账户
    login_button4.click()
    time.sleep(5)
    js = "var q=document.getElementById('szhhaccount-combolist').scrollTop=10000"
    driver.execute_script(js) #滚动下拉框
    time.sleep(5)
    login_button5 = driver.find_element_by_id("f-combo-szhhaccount-list-20")  #
    login_button5.click()
    time.sleep(5)
    login_button6 = driver.find_element_by_xpath(".//*[@id='btn_search']/div")  # 查询
    login_button6.click()
    time.sleep(5)
    htm_const = driver.page_source
    soup = BeautifulSoup(htm_const, 'html.parser', from_encoding='utf-8')
    soup_row=soup.find_all(class_='ui-widget-content jqgrow ui-row-ltr')
    zhmx={'shiyou':[],'fukuan':[],'shoukuan':[],'yue':[]}
    for i in range(0,len(soup_row)):
        shiyou = soup_row[i].find(attrs={"aria-describedby": "gridTable_vc_sm"}).string
        fukuan = soup_row[i].find(attrs={"aria-describedby": "gridTable_en_fkje"}).string
        shoukuan = soup_row[i].find(attrs={"aria-describedby": "gridTable_en_skje"}).string
        yue = soup_row[i].find(attrs={"aria-describedby": "gridTable_en_zhye"}).string
        print shiyou,fukuan,shoukuan,yue
        zhmx['shiyou'].append(shiyou)
        zhmx['fukuan'].append(fukuan)
        zhmx['shoukuan'].append(shoukuan)
        zhmx['yue'].append(yue)
    return zhmx

def hhf_sum(zhmx):
    hhf_sum = 0
    pattern_hhf = re.compile(u'汇划费')
    for i in range(0, len(zhmx['shiyou'])):
        if re.search(pattern_hhf, zhmx['shiyou'][i]):
            hhf_sum = hhf_sum + float(zhmx['fukuan'][i])
    return hhf_sum

zhmx=zd_catch()
hhf_sum=hhf_sum(zhmx)
print u'今日汇划费为：'+str(hhf_sum)
print u'今日的账户余额为：'+str(zhmx['yue'][len(zhmx['yue'])-1])
