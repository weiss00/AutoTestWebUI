#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 14:37
# @Author  : weiss
# @File    : do_common.py
# @Software: PyCharm

from base.base import Base

class DoCommon(Base):

    # 判断元素是否存在
    def is_exists_element(self, loc, doc=""):
        try:
            element = self.find_elem(loc, doc)
            if element:
                return element
        except Exception:
            self.save_screen_shots(doc)
            return None