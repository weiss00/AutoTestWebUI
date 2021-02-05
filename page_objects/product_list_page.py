#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 09:28
# @Author  : weiss
# @File    : product_list_page.py
# @Software: PyCharm

from base.base import Base

class ProductListPage(Base):

    # 查看商品列表中  是否存在导航条元素
    def navbar_is_exists(self, loc):
        try:
            navbar_elem_1 = self.get_element_text(loc)
            if navbar_elem_1:
                return navbar_elem_1
        except Exception:
            self.save_screen_shots(f"商品列表导航条元素{loc[0]}")
            return None
