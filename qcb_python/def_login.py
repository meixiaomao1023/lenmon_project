# -*- coding: utf-8 -*-
# @Time :2020/10/27 13:45
# @AUthor :meixiaomao
# @Email :
# @File :def_login.py
# @Software: PyCharm

import time

def login_page(username,password,driver):     #形参  参数化
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()

def open_url(url,driver):     #打开网页
    driver.get(url)
    driver.maximize_window()
    # driver.find_element_by_xpath("//span[text()='零售出库']").click()


def search_key(url,driver,username,password,s_key):
    open_url(url,driver)
    login_page(username,password,driver)
    # login_user = driver.find_element_by_xpath("//p[text()='测试用户']").text

    driver.find_element_by_xpath("//span[text()='零售出库']").click()

    idInfo = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
    iframeId = idInfo + "-frame"
    # print("iframeId = " + iframeId)
    driver.switch_to.frame(iframeId)
    driver.find_element_by_xpath("//input[@id='searchNumber']").send_keys(s_key)
    driver.find_element_by_xpath("//*[@id='searchBtn']").click()
    time.sleep(2)
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']/td[@field='number']/div").text

    return num  #返回值


