#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/30 14:29
# @Author  : weiss
# @File    : test_02_index.py
# @Software: PyCharm
import time

import pytest
import allure

from tools.do_common import DoCommon
from page_objects.index_page import IndexPage
from page_locator.login_page_locator import LoginPageLocator as login_loc
from page_locator.index_page_locator import IndexPageLocator as index_loc
from page_locator.calc_amount_locator import CalcAmountLocator as calc_amount_loc
from page_locator.product_list_page_locator import ProductListPageLocator as product_list_loc

@pytest.mark.usefixtures("init_test_user_center_class")
class TestIndex():

    # 主页模块 -- 首页全部商品分类
    @allure.title("主页模块 -- 首页全部商品分类")
    @pytest.mark.usefixtures("init_test_user_center_func")
    def test_product_menu_all(self, init_test_user_center_func):
        index_page = IndexPage(init_test_user_center_func[0], init_test_user_center_func[1])
        # 鼠标悬浮  全部商品列表
        index_page.move_to_hold_element(index_loc.menu_all_loc)
        # 向下滚动条
        index_page.scroll_to_visibility_element(index_loc.new_product_price_1_loc)
        # 查看特定元素
        status = DoCommon(init_test_user_center_func[0], init_test_user_center_func[1]).is_exists_element(index_loc.product_elem_loc)
        assert status != None


    @allure.title("登陆首页新出炉商品模块正向用例 -- 测试新出炉商品模块")
    @pytest.mark.usefixtures("init_test_user_center_func")
    def test_new_product(self, init_test_user_center_func):
        index_page = IndexPage(init_test_user_center_func[0], init_test_user_center_func[1])
        # 查看用户中心页面中我的收藏元素
        assert index_page.new_product_exists() != None

    @allure.title("主页模块 -- 测试退出功能")
    @pytest.mark.usefixtures("init_test_quit_element_func")
    def test_quit_element(self, init_test_quit_element_func):
        # 登陆后点击退出元素
        index_page = IndexPage(init_test_quit_element_func[0], init_test_quit_element_func[1])
        index_page.click_quit_element()
        # 判断是否有特殊元素
        status = DoCommon(init_test_quit_element_func[0], init_test_quit_element_func[1]).is_exists_element(login_loc.login_btn_loc)
        assert status != None

    # 测试搜索框
    @allure.title("首页搜索框搜索元素 -- 测试搜索元素")
    @pytest.mark.usefixtures("init_test_search_element_func")
    def test_search_element(self, init_test_search_element_func):
        # 向搜索框输入元素
        status = DoCommon(init_test_search_element_func[0], init_test_search_element_func[1]).is_exists_element(product_list_loc.product_list_tail_document_name)
        assert status != None

    @allure.title("首页面加入购物车元素 -- 测试去结算页面")
    @pytest.mark.usefixtures("init_test_calc_amount_btn")
    def test_calc_amount_btn(self, init_test_calc_amount_btn):
        # 切换窗口
        windows = init_test_calc_amount_btn[0].window_handles
        # 转换到最新打开的窗口
        init_test_calc_amount_btn[0].switch_to.window(windows[-1])
        time.sleep(2)
        # 判断元素是否存在
        status = DoCommon(init_test_calc_amount_btn[0], init_test_calc_amount_btn[1]).is_exists_element(calc_amount_loc.calc_amount_page_calc_btn)
        assert status != None


