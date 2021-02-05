#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 09:14
# @Author  : weiss
# @File    : test_03_index_navbar.py
# @Software: PyCharm

import allure
import pytest
from page_objects.index_page import IndexPage
from page_objects.product_list_page import ProductListPage
from page_locator.index_page_locator import IndexPageLocator as index_loc
from page_locator.product_list_page_locator import ProductListPageLocator as plp_loc

@pytest.mark.usefixtures("init_test_user_center_class")
@pytest.mark.usefixtures("init_test_user_center_func")
class TestIndexNavbar():

    @allure.title("商品列表模块 -- 导航栏第一个")
    def test_navbar_1(self, init_test_user_center_func):
        index_ele = IndexPage(init_test_user_center_func[0], init_test_user_center_func[1])
        index_ele.click_element(index_loc.index_navbar_1_loc)
        plp = ProductListPage(init_test_user_center_func[0], init_test_user_center_func[1])
        status = plp.navbar_is_exists(plp_loc.product_type_1)
        assert status != None

    @allure.title("商品列表模块 -- 导航栏第二个")
    def test_navbar_2(self, init_test_user_center_func):
        index_ele = IndexPage(init_test_user_center_func[0], init_test_user_center_func[1])
        index_ele.click_element(index_loc.index_navbar_2_loc)
        plp = ProductListPage(init_test_user_center_func[0], init_test_user_center_func[1])
        status = plp.navbar_is_exists(plp_loc.product_type_2)
        assert status != None

    @allure.title("商品列表模块 -- 导航栏第三个")
    def test_navbar_3(self, init_test_user_center_func):
        index_ele = IndexPage(init_test_user_center_func[0], init_test_user_center_func[1])
        index_ele.click_element(index_loc.index_navbar_3_loc)
        plp = ProductListPage(init_test_user_center_func[0], init_test_user_center_func[1])
        status = plp.navbar_is_exists(plp_loc.product_type_3)
        assert status != None