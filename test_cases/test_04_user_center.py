#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/30 12:42
# @Author  : weiss
# @File    : test_04_user_center.py
# @Software: PyCharm

import pytest
import allure
from page_objects.user_center_page import UserCenterPage
from page_locator.index_page_locator import IndexPageLocator as index_loc

@pytest.mark.usefixtures("init_test_user_center_class")
@pytest.mark.usefixtures("init_test_user_center_func")
class TestUserCenter():

    @allure.title("用户中心模块正向用例 -- 测试我的订单")
    def test_my_order(self, init_test_user_center_func):
        user_center = UserCenterPage(init_test_user_center_func[0], init_test_user_center_func[1])
        # 点击用户中心的我的订单
        user_center.move_to_hold_element(index_loc.more_menu_loc)
        user_center.click_element(index_loc.my_order_loc)
        # 查看用户中心页面中我的订单元素
        assert user_center.is_exists_my_order() != None


    @allure.title("用户中心模块正向用例 -- 测试我的收藏")
    def test_my_collect(self, init_test_user_center_func):
        user_center = UserCenterPage(init_test_user_center_func[0], init_test_user_center_func[1])
        # 点击用户中心的我的收藏
        user_center.move_to_hold_element(index_loc.more_menu_loc)
        user_center.click_element(index_loc.my_collect_loc)
        # 查看用户中心页面中我的收藏元素
        assert user_center.is_exists_my_collect() != None


    @allure.title("用户中心模块正向用例 -- 测试我的收货地址")
    def test_my_delivery_address(self, init_test_user_center_func):
        user_center = UserCenterPage(init_test_user_center_func[0], init_test_user_center_func[1])
        # 点击用户中心的我的收藏
        user_center.move_to_hold_element(index_loc.more_menu_loc)
        user_center.click_element(index_loc.my_delivery_address)
        # 查看用户中心页面中我的收藏元素
        assert user_center.is_exists_my_delivery_address() != None
