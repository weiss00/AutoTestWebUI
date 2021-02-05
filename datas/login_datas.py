#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 08:53
# @Author  : weiss
# @File    : login_datas.py
# @Software: PyCharm

success_data = {
    ("13133334444", "123456")
}

fail_data = {
    "error_password": ("13133334444", "1111111"),
    "error_data_no_user": ("", "123456"),
    "error_data_no_all" : ("", ""),
    "error_data_no_password": ("13133334444", ""),
    "error_data_user_low": ("1313333444", "123456"),
    "error_data_user_long": ("131333344444", "123456"),
    "error_data_password_low": ("13133334444", "12345"),
    "error_data_password_long": ("13133334444", "123456789012345678901234567890")
}
