#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 14:45
# @Author  : weiss
# @File    : test_05_product_tail.py
# @Software: PyCharm
import time

import pytest
import allure

from tools.do_common import DoCommon
from page_objects.product_tail_page import ProductTailPage
from page_objects.user_center_page import UserCenterPage
from page_locator.index_page_locator import IndexPageLocator as index_loc
from page_locator.user_center_locator import UserCenterLocator as user_center_loc
from page_locator.product_tail_page_locator import ProductTailPageLocator as product_tail_loc

@pytest.mark.smoke
@pytest.mark.usefixtures("init_test_product_tail_page_class")
class TestProductTail():

    # 测试商品详情页面
    @allure.title("商品详情页模块 -- 测试加入购物车元素")
    @pytest.mark.usefixtures("init_test_product_add_to_cart_func")
    def test_product_tail_page(self, init_test_product_add_to_cart_func):
        # 切换窗口
        windows = init_test_product_add_to_cart_func[0].window_handles
        # 转换到最新打开的窗口
        init_test_product_add_to_cart_func[0].switch_to.window(windows[-1])
        status = DoCommon(init_test_product_add_to_cart_func[0], init_test_product_add_to_cart_func[1]).is_exists_element(product_tail_loc.panic_buy_loc, "商品详情页面定位绿色抢购元素")
        assert status != None

    # 测试商品详情模块 -- 商品加入购物车
    @allure.title("测试商品详情模块 -- 商品加入购物车")
    @pytest.mark.usefixtures("init_test_product_add_to_cart_func")
    def test_product_add_to_cart(self, init_test_product_add_to_cart_func):
        # 点击加入购物车按钮
        product_tail_page = ProductTailPage(init_test_product_add_to_cart_func[0], init_test_product_add_to_cart_func[1])
        product_tail_page.click_add_to_cart(product_tail_loc.add_to_cart_loc)
        # 查看去结算按钮元素
        status = DoCommon(init_test_product_add_to_cart_func[0], init_test_product_add_to_cart_func[1]).is_exists_element(product_tail_loc.calc_amount_btn_loc)
        assert status != None

    @allure.title("测试商品详情模块 -- 商品收藏元素")
    @pytest.mark.usefixtures("init_test_product_add_to_cart_func")
    def test_product_collect(self, init_test_product_add_to_cart_func):
        doc = "商品详情页面商品收藏元素"
        # 点击收藏按钮
        product_tail_page = ProductTailPage(init_test_product_add_to_cart_func[0], init_test_product_add_to_cart_func[1])
        product_tail_page.click_collect_btn(product_tail_loc.collect_btn_loc, doc)
        # 处理alert框
        product_tail_page.deal_alert_elem(doc)
        # 查看已收藏按钮元素
        status = DoCommon(init_test_product_add_to_cart_func[0], init_test_product_add_to_cart_func[1]).is_exists_element(product_tail_loc.collected_btn_loc, "商品详情页面商品已收藏元素")
        assert status != None

    @allure.title("测试商品详情页面 -- 测试我的收藏操作过程")
    @pytest.mark.usefixtures("init_test_product_collect_func")
    def test_my_collect_operator(self, init_test_product_collect_func):
        # 选中商品加入收藏
        doc = "商品详情页面商品收藏元素"
        user_center = UserCenterPage(init_test_product_collect_func[0], init_test_product_collect_func[1])
        # 点击用户中心的我的收藏
        user_center.move_to_hold_element(index_loc.more_menu_loc)
        user_center.click_element(index_loc.my_collect_loc)
        init_test_product_collect_func[0].refresh()
        time.sleep(2)
        # 查看是否有特定元素
        status = DoCommon(init_test_product_collect_func[0], init_test_product_collect_func[1]).is_exists_element(user_center_loc.product_delete_1_loc, doc)
        assert status != None


if __name__ == '__main__':
    pytest.main(["-m smoke"])