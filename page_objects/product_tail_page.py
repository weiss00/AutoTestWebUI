#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 14:26
# @Author  : weiss
# @File    : product_tail_page.py
# @Software: PyCharm

import time
from base.base import Base

class ProductTailPage(Base):

    # 点击加入购物车
    def click_add_to_cart(self, loc, doc=""):
        doc = "商品详情页面加入购物车元素"
        try:
            self.click_element(loc, doc)
            time.sleep(2)
        except Exception:
            self.save_screen_shots(doc)
            raise

    # 点击收藏按钮
    def click_collect_btn(self, loc, doc=""):
        doc = "商品详情页面收藏元素"
        try:
            self.click_element(loc, doc)
            time.sleep(2)
        except Exception:
            self.save_screen_shots(doc)
            raise