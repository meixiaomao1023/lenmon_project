# -*- coding: utf-8 -*-
# @Time :2020/10/27 12:20
# @AUthor :meixiaomao
# @Email :
# @File :run.py
# @Software: PyCharm

from qcb_python import def_login   #导入封装函数的文件
from test_data import test_date     #导入测试数据的文件
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

#调用函数   1、先把参数取出来   2、再把参数传到函数调用里
url = test_date.url["url"]  #取值URL参数
username = test_date.login_date["username"]  #取值登录用户名
password = test_date.login_date["password"]  #取值登录密码
s_key = test_date.s_key["s_key"]    #取值  取搜索的关键字

#函数的调用 以及 传参
#给函数定义了一个返回值，在调用的时候 用一个变量接受返回值
result = def_login.search_key(url,driver,username,password,s_key)   #调用函数


if s_key in result:
    print("搜索结果是正确的")
else:
    print("用例测试不通过！")