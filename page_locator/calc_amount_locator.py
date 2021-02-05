#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 09:30
# @Author  : weiss
# @File    : calc_amount_locator.py
# @Software: PyCharm

from selenium.webdriver.common.by import By

class CalcAmountLocator():

    calc_amount_page_calc_btn = (By.XPATH, '//p[@class="sumup"]//a[@class="btn" and contains(text(), "去结算")]')