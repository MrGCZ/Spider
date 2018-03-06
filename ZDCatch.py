#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
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
    login_button1 = driver.find_element_by_xpath(".//*[@id='J_ui-layout-left_list']/ul/li[1]/span")  # 划款业务
    login_button1.click()
    time.sleep(1)
    login_button2 = driver.find_element_by_xpath(".//*[@id='faHkzlcx']")  # 划款业务查询
    login_button2.click()
    time.sleep(5)
    login_button3 = driver.find_element_by_xpath("html/body/div[1]/div[4]/div/div[2]/span")  # 划款业务查询
    login_button3.click()
    time.sleep(10)
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'faHkzlcx')]"))
    chakanzhiling = driver.find_element_by_xpath(".//*[@id='btn_view']/div/span")
    zhilingleibie = driver.find_elements_by_css_selector("[aria-describedby=gridTable_hklbname]")
    huakuanzhiling = []
    for zllb in zhilingleibie:
        zllb.click()
        chakanzhiling.click()
        htm_const1 = driver.page_source
        soup = BeautifulSoup(htm_const1, 'html.parser', from_encoding='utf-8')
        zhilingzhuangtai = soup.find(id="v_zllc").string  # 指令状态
        huankuanleibie = soup.find(id="v_hklb").string  # 划款类别
        shiyou = soup.find(id="v_hksy").string  # 事由
        huoqizhanghukahuhang = soup.find(id="v_skkhhqc").string  # 活期账户开户行
        jine = soup.find(id="v_je").string  # 金额
        huakuanzhiling.append(
            [zhilingzhuangtai, huankuanleibie, shiyou, huoqizhanghukahuhang, jine])  # 指令状态、划款类别、事由、活期账户开户行、金额
        print zhilingzhuangtai, huankuanleibie, shiyou, huoqizhanghukahuhang, jine
        guanbi = driver.find_element_by_xpath(".//*[@id='qshksq-view']/div[2]/div[2]/div/div/div/button")
        guanbi.click()
    return huakuanzhiling


