#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 15:34
# @Author  : weiss
# @File    : login_page.py
# @Software: PyCharm

"""
    登陆页面
"""

from base.base import Base
from page_locator.login_page_locator import LoginPageLocator as login_loc

class LoginPage(Base):

    # 登陆操作
    def login(self, username, password):
        try:
            self.send_word_element(login_loc.username_loc, username)
            self.send_word_element(login_loc.password_loc, password)
            self.click_element(login_loc.login_btn_loc)
        except Exception:
            self.save_screen_shots("登陆页面_登陆操作")

    # 获取用户名框错误提示 -- 该字段不能为空
    def get_error_user_info(self):
        try:
            elem = self.find_elem(login_loc.username_filed_null_loc)
            if elem:
                return elem
        except Exception:
            self.save_screen_shots("登陆页面_获取用户名提示该字段不能为空提示")
            return None


    # 获取密码框错误提示 -- 该字段不能为空
    def get_error_pwd_info(self):
        try:
            elem = self.find_elem(login_loc.password_filed_null_loc)
            if elem:
                return elem
        except Exception:
            self.save_screen_shots("登陆页面_获取密码提示该字段不能为空提示")
            return None


    # 获取无法使用提供的认证信息登录。提示是否存在
    def get_error_auth_info(self):
        """
        :param loc: 定位元组
        :return:  element
        """
        try:
            elem = self.find_elem(login_loc.auth_info_msg_loc)
            if elem:
                return elem
        except Exception:
            self.save_screen_shots("登陆页面_获取无法认证信息提示")
            return None

