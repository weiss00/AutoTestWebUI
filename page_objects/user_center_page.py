#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/30 11:16
# @Author  : weiss
# @File    : user_center_page.py
# @Software: PyCharm

from base.base import Base
from page_locator.user_center_locator import UserCenterLocator as user_center_loc

class UserCenterPage(Base):

    # 查看是否有我的订单元素
    def is_exists_my_order(self):
        try:
            elem = self.find_elem(user_center_loc.order_loc)
            if elem:
                return elem
        except Exception:
            self.save_screen_shots("用户中心页面_我的订单元素出错")
            return None

    # 查看是否有我的收藏元素
    def is_exists_my_collect(self):
        try:
            elem = self.find_elem(user_center_loc.collect_loc)
            if elem:
                return elem
        except Exception:
            self.save_screen_shots("用户中心页面_我的收藏元素出错")
            return None

    # 查看是否有我的收货地址元素
    def is_exists_my_delivery_address(self):
        try:
            elem = self.find_elem(user_center_loc.receiver_info_loc)
            if elem:
                return elem
        except Exception:
            self.save_screen_shots("用户中心页面_我的收货地址元素出错")
            return None
