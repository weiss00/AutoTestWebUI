#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 14:44
# @Author  : weiss
# @File    : test_01_login.py
# @Software: PyCharm

import pytest
import allure
import datas.login_datas as datas
from page_objects.login_page import LoginPage
from page_objects.index_page import IndexPage

# @pytest.mark.smoke
@pytest.mark.usefixtures("init_class_test")
@pytest.mark.usefixtures("init_func_test")
class TestLogin():

    @allure.title("登陆模块正向用例")
    @pytest.mark.parametrize("success_data", datas.success_data)
    def test_login_success(self, init_func_test, success_data):

        # 登陆页面登陆操作
        LoginPage(init_func_test[0], init_func_test[1]).login(success_data[0], success_data[1])
        # 首页特定元素是否存在
        quit_elem_status = IndexPage(init_func_test[0], init_func_test[1]).quit_elem_exists()
        assert quit_elem_status != None

    @allure.title("登陆模块反向用例---不填写用户名")
    def test_login_fail_no_user(self, init_func_test, data=datas.fail_data['error_data_no_user']):
        # 登陆页面登陆操作
        lp = LoginPage(init_func_test[0], init_func_test[1])
        lp.login(data[0], data[1])
        # 查看登陆页面用户名下是否提示该字段不能为空
        elem = lp.get_error_user_info()
        assert elem != None

    @allure.title("登陆模块反向用例---不填写密码")
    def test_login_fail_no_pwd(self, init_func_test, data=datas.fail_data['error_data_no_password']):
        # 登陆页面登陆操作
        lp = LoginPage(init_func_test[0], init_func_test[1])
        lp.login(data[0], data[1])
        # 查看登陆页面密码是否提示该字段不能为空
        elem = lp.get_error_pwd_info()
        assert elem != None

    @allure.title("登陆模块反向用例---不填写用户名密码")
    def test_login_fail_no_all(self, init_func_test, data=datas.fail_data['error_data_no_all']):
        # 登陆页面登陆操作
        lp = LoginPage(init_func_test[0], init_func_test[1])
        lp.login(data[0], data[1])
        # 查看登陆页面密码是否提示该字段不能为空
        user_elem = lp.get_error_user_info()
        pwd_elem = lp.get_error_pwd_info()
        assert user_elem != None and pwd_elem != None

    @allure.title("登陆模块反向用例---填写短用户名")
    def test_login_fail_user_low(self, init_func_test, data=datas.fail_data['error_data_user_low']):
        # 登陆页面登陆操作
        lp = LoginPage(init_func_test[0], init_func_test[1])
        lp.login(data[0], data[1])
        # 查看登陆页面用户名下是否提示该字段不能为空
        elem = lp.get_error_auth_info()
        assert elem != None

    @allure.title("登陆模块反向用例---填写长用户名")
    def test_login_fail_user_long(self, init_func_test, data=datas.fail_data['error_data_user_long']):
        # 登陆页面登陆操作
        lp = LoginPage(init_func_test[0], init_func_test[1])
        lp.login(data[0], data[1])
        elem = lp.get_error_auth_info()
        assert elem != None

    @allure.title("登陆模块反向用例---填写短密码")
    def test_login_fail_pwd_low(self, init_func_test, data=datas.fail_data['error_data_password_low']):
        # 登陆页面登陆操作
        lp = LoginPage(init_func_test[0], init_func_test[1])
        lp.login(data[0], data[1])
        elem = lp.get_error_auth_info()
        assert elem != None

    @allure.title("登陆模块反向用例---填写长密码")
    def test_login_fail_pwd_long(self, init_func_test, data=datas.fail_data['error_data_password_long']):
        # 登陆页面登陆操作
        lp = LoginPage(init_func_test[0], init_func_test[1])
        lp.login(data[0], data[1])
        elem = lp.get_error_auth_info()
        assert elem != None


if __name__ == '__main__':
    pytest.main(["-sv"])