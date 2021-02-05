#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 14:26
# @Author  : weiss
# @File    : product_tail_page_locator.py
# @Software: PyCharm

from selenium.webdriver.common.by import By

class ProductTailPageLocator():

    # 商品详情页 -- 加入购物车元素
    # shopping_cart_loc = (By.XPATH, '//ul[@class="sku"]//li[@class="add_cart_li"]//a[@id="buy_btn" and contains(text(), "加入购物车")]')
    # product_tail_info_loc = (By.XPATH ,'//div[@class="spxq_main"]//td[@class="th"]')

    # 商品详情页 -- 抢购绿色元素
    panic_buy_loc = (By.XPATH, '//dl[@class="loaded"]//li/span[@class="icon_promo"]')

    # 商品详情页 -- 加入购物车按钮元素
    add_to_cart_loc = (By.XPATH, '//ul[@class="sku"]//a[@id="buy_btn"]')

    # 商品详情页 -- 收藏按钮元素
    collect_btn_loc = (By.XPATH, '//ul[@class="sku"]//a[@class="graybtn"]')

    # 商品详情页 -- 已收藏按钮元素
    collected_btn_loc = (By.XPATH, '//ul[@class="sku"]//a[@id="fav-btn"]')

    # 商品详情页 -- 加入购物车成功 -- 去结算元素
    calc_amount_btn_loc = (By.XPATH, '//div[@id="cart_show"]//a[@class="btn" and contains(text(), "去结算")]')