#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 09:47
# @Author  : weiss
# @File    : index_page_locator.py
# @Software: PyCharm

from selenium.webdriver.common.by import By

class IndexPageLocator():

    quit_elem_loc = (By.XPATH, '//div[@class="hd_bar"]//li[@id="ECS_MEMBERZONE"]/a[2]')

    # 会员中心
    more_menu_loc = (By.XPATH, '//li[@class="more-menu"]/a[text()="会员中心"]')

    # 会员中心 -- 我的订单
    my_order_loc = (By.XPATH, '//div[@class="more-bd show"]//div[@class="list"]//a[text()="我的订单"]')

    # 会员中心 -- 我的收藏
    my_collect_loc = (By.XPATH, '//div[@class="more-bd show"]//div[@class="list"]//a[text()="我的收藏"]')

    # 会员中心 -- 我的收货地址
    my_delivery_address = (By.XPATH, '//div[@class="more-bd show"]//div[@class="list"]//a[text()="我的收货地址"]')

    # 搜索框
    search_element_loc = (By.XPATH, '//div[@class="search_box"]//input[@id="keyword"]')

    # 搜索框 -- 搜索按钮
    search_element_btn_loc = (By.XPATH, '//div[@class="search_box"]//button[@class="sea_submit"]')

    # 首页主页面 -- 刚出炉的新品
    new_product_loc = (By.XPATH, '//div[@id="warp-box"]//h2/em[text()="刚出炉新品"]')

    # # 首页主页面 -- 刚出炉新品 -- 打折价格
    new_product_price_1_loc = (By.XPATH, '//ul[@class="newgoods_fastbuy"]//li[1]//span[@class="p-price"]//em[@class="fastbuy_price"]')

    # 首页主页面 -- 全部商品分类
    menu_all_loc = (By.XPATH, '//div[@class="main_nav_link"]//a[@class="meunAll"]')

    # 首页主页面 -- 商品特定元素
    product_elem_loc = (By.XPATH, '//div[@id="J_mainCata"]//li[@class="first"]/h3//a[text()="酸奶"]')

    # 首页主页面 -- 导航栏1
    index_navbar_1_loc = (By.XPATH, '//ul[@id="sub_nav"]//a[contains(text(), "澳洲大龙虾")]')

    # 首页主页面 -- 导航栏2
    index_navbar_2_loc = (By.XPATH, '//ul[@id="sub_nav"]//a[contains(text(), "精选茗茶")]')

    # 首页主页面 -- 导航栏3
    index_navbar_3_loc = (By.XPATH, '//ul[@id="sub_nav"]//a[contains(text(), "酒水饮料")]')

    # ==================================================================================================================

    # 首页主页面 -- 去购物车结算按钮元素
    shopping_cart_btn_loc = (By.XPATH, '//div[@id="ECS_CARTINFO"]//a[@class="tit"]')

    # 首页主页面 -- 去购物车结算按钮 -- 去结算按钮
    calc_amount_btn = (By.XPATH, '//div[@class="list"]//div[@class="count"]//a[@class="btn" and contains(text(), "去结算")]')

    # 首页主页面 -- 新商品图片
    newgoods_fastbuy_1_img_loc = (By.XPATH, '//ul[@class="newgoods_fastbuy"]//a[@class="imgBox"]/img')

    # 首页主页面 -- 第一个标签元素
    first_tab_loc = (By.XPATH, '//div[@class="series_name name_hufu"]/h2')