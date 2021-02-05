#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 15:19
# @Author  : weiss
# @File    : login_page_locator.py
# @Software: PyCharm

from selenium.webdriver.common.by import By

class LoginPageLocator():

    username_loc = (By.XPATH, '//input[@id="account_l"]')
    password_loc = (By.XPATH, '//input[@id="password_l"]')
    login_btn_loc = (By.XPATH, '//input[@id="jsLoginBtn"]')

    username_filed_null_loc = (By.XPATH, '//form[@id="jsLoginForm"]//p[1][@class="error-text" and text()="该字段不能为空。"]')
    password_filed_null_loc = (By.XPATH, '//form[@id="jsLoginForm"]//p[2][@class="error-text" and text()="该字段不能为空。"]')
    auth_info_msg_loc = (By.XPATH, '//form[@id="jsLoginForm"]//p[@class="error-text" and text()="无法使用提供的认证信息登录。"]')