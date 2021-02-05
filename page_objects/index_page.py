#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 15:34
# @Author  : weiss
# @File    : index_page.py
# @Software: PyCharm

"""
    主页面
"""
import time

from base.base import Base
from page_locator.index_page_locator import IndexPageLocator as index_loc

class IndexPage(Base):

    # 退出元素存在判断
    def quit_elem_exists(self):
        try:
            quit_elem = self.find_elem(index_loc.quit_elem_loc)
            if quit_elem:
                return quit_elem
        except Exception:
            self.save_screen_shots("首页退出元素定位错误")
            return False

    # 点击退出按钮
    def click_quit_element(self):
        self.click_element(index_loc.quit_elem_loc, "主页面点击退出元素")
        time.sleep(2)

    # 向搜索框输入文字点击搜索按钮
    def search_element(self, word="牛肉"):
        # 输入文字
        self.send_word_element(index_loc.search_element_loc, word, "首页搜索框元素输入文字")
        time.sleep(0.5)
        # 点击搜索按钮
        self.click_element(index_loc.search_element_btn_loc, "首页搜索框输入元素点击搜索按钮")
        time.sleep(2)

    # 新出炉商品 -- 销量元素存在判断
    def new_product_exists(self):
        try:
            new_product = self.find_elem(index_loc.new_product_loc)
            if new_product:
                return new_product
        except Exception:
            self.save_screen_shots("首页新出炉商品元素。")
            return None

    # 悬浮加入购物车点击去结算进入结算按钮
    def click_calc_amount_btn(self):
        doc_1 = "主页面悬浮加入购物车页面"
        doc_2 = "主页面悬浮加入购物车元素中的去结算按钮"
        # 悬浮元素
        self.move_to_hold_element(index_loc.shopping_cart_btn_loc, doc_1)
        time.sleep(2)
        # 点击元素
        self.click_element(index_loc.calc_amount_btn, doc_2)
