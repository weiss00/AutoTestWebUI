#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 09:34
# @Author  : weiss
# @File    : product_list_page_locator.py
# @Software: PyCharm

from selenium.webdriver.common.by import By

class ProductListPageLocator():

    product_type_1 = (By.XPATH, '//div[@id="cate-menu"]//a/strong[text()="澳洲大龙虾"]')

    product_type_2 = (By.XPATH, '//div[@id="cate-menu"]//a/strong[text()="精选茗茶"]')

    product_type_3 = (By.XPATH, '//div[@id="cate-menu"]//a/strong[text()="酒水饮料"]')

    product_list_tail_document_name = (By.XPATH, '//div[@class="productlist"]//ul[@class="cle"]//li[1]//span[@class="productname"]')
