#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 15:38
# @Author  : weiss
# @File    : conftest.py
# @Software: PyCharm
import time

import pytest
from base.base import Base
from tools.do_log import DoLog
from selenium import webdriver
import datas.common_datas as data
from tools.path_config import PathConfig
from page_objects.login_page import LoginPage
from page_objects.index_page import IndexPage
from selenium.webdriver.chrome.options import Options
from page_objects.calc_amount_page import CalcAmountPage
from page_objects.product_tail_page import ProductTailPage
from page_locator.login_page_locator import LoginPageLocator as login_loc
from page_locator.index_page_locator import IndexPageLocator as index_loc
from page_locator.product_tail_page_locator import ProductTailPageLocator as product_tail_loc

driver = None
log = DoLog(file_name=PathConfig.get_log_path())
@pytest.fixture(scope="class")
def init_class_test():
    global driver
    driver = webdriver.Chrome()
    yield
    driver.quit()

@pytest.fixture(scope="function")
def init_func_test():
    global driver, log
    driver.get(data.base_url)
    driver.maximize_window()
    Base(driver, log).wait_element(login_loc.username_loc)
    # 访问需要登陆的页面
    yield driver, log

# 用户中心初始化类
@pytest.fixture(scope="class")
def init_test_user_center_class():
    global driver, log
    driver = webdriver.Chrome()
    driver.get(data.base_url)
    driver.maximize_window()
    Base(driver, log).wait_element(login_loc.username_loc)
    lp = LoginPage(driver, log)
    lp.login("13133334444", "123456")
    time.sleep(3)
    driver.refresh()
    yield
    driver.quit()

# 用户中心初始方法
@pytest.fixture(scope="function")
def init_test_user_center_func():
    global driver, log
    yield driver, log
    driver.refresh()

# 测试退出功能方法
@pytest.fixture(scope="function")
def init_test_quit_element_func():
    global driver, log
    yield driver, log
    driver.get(data.base_url)
    driver.maximize_window()
    Base(driver, log).wait_element(login_loc.username_loc)
    lp = LoginPage(driver, log)
    lp.login("13133334444", "123456")
    time.sleep(3)
    driver.refresh()

# 初始化搜索框方法
@pytest.fixture(scope="function")
def init_test_search_element_func():
    global driver, log
    index_page = IndexPage(driver, log)
    index_page.search_element()
    current_handle = driver.current_window_handle
    yield driver, log
    driver.switch_to.window(current_handle)
    driver.refresh()

# 商品详情页初始化类
@pytest.fixture(scope="class")
def init_test_product_tail_page_class():
    global driver, log
    driver = webdriver.Chrome()
    driver.get(data.base_url)
    driver.maximize_window()
    Base(driver, log).wait_element(login_loc.username_loc)
    lp = LoginPage(driver, log)
    lp.login("13133334444", "123456")
    time.sleep(3)
    driver.refresh()
    index = IndexPage(driver, log)
    index.click_element(index_loc.newgoods_fastbuy_1_img_loc)
    time.sleep(2)
    # # 切换窗口
    # windows = driver.window_handles
    # # 转换到最新打开的窗口
    # driver.switch_to.window(windows[-1])
    yield
    driver.quit()

# 商品详情页初始化方法
@pytest.fixture(scope="function")
def init_test_product_tail_page_func():
    global driver
    yield driver
    driver.refresh()

# 商品加入购物车初始化方法
@pytest.fixture(scope="function")
def init_test_product_add_to_cart_func():
    global driver, log
    # 切换窗口
    windows = driver.window_handles
    # 转换到最新打开的窗口
    driver.switch_to.window(windows[-1])
    yield driver, log
    driver.refresh()

# 商品收藏初始化方法
@pytest.fixture(scope="function")
def init_test_product_collect_func():
    global driver, log
    yield driver, log
    # page = ProductTailPage(driver)
    # page.click_element(product_tail_loc.collected_btn_loc)

# 商品收藏初始化方法
@pytest.fixture(scope="function")
def init_test_product_collect_func():
    global driver, log
    yield  driver, log
    driver = webdriver.Chrome()
    driver.get(data.base_url)
    driver.maximize_window()
    Base(driver, log).wait_element(login_loc.username_loc)
    lp = LoginPage(driver, log)
    lp.login("13133334444", "123456")
    time.sleep(3)
    driver.refresh()
    index = IndexPage(driver, log)
    index.click_element(index_loc.newgoods_fastbuy_1_img_loc)
    time.sleep(2)
    # 切换窗口
    windows = driver.window_handles
    # 转换到最新打开的窗口
    driver.switch_to.window(windows[-1])
    page = ProductTailPage(driver, log)
    page.click_element(product_tail_loc.collected_btn_loc)

# 测试点击去结算按钮 -- 跳转去结算页面
@pytest.fixture(scope="function")
def init_test_calc_amount_btn():
    global driver, log
    index_page = IndexPage(driver, log)
    index_page.click_calc_amount_btn()
    yield driver, log
    driver.refresh()
