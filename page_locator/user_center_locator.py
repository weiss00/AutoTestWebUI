#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/30 11:20
# @Author  : weiss
# @File    : user_center_locator.py
# @Software: PyCharm

from selenium.webdriver.common.by import By

class UserCenterLocator():

    order_loc = (By.XPATH, '//div[@class="box_1"]//h5/span[text()="我的订单"]')

    collect_loc = (By.XPATH, '//div[@class="box_1"]//h5/span[text()="我的收藏"]')

    receiver_info_loc = (By.XPATH, '//div[@class="box_1"]//h5/span[text()="收货人信息"]')

    # 用户中心  -- 我的收藏  -- 第一个商品删除元素
    product_delete_1_loc = (By.XPATH, '//table//td[3]//a[@class="f6"]')