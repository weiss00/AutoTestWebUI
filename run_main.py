#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 16:37
# @Author  : weiss
# @File    : run_main.py
# @Software: PyCharm

import os
import time

from tools.path_config import PathConfig

cmd = f"pytest -sv --html={PathConfig.get_html_report()} --alluredir={PathConfig.get_allure_path()} --reruns 2 --clean-alluredir --reruns-delay 3 --durations=0"

cmd_2 = r"allure serve C:\Users\weiss\Desktop\PayDemo\AutoTestWebUI\output\allure_report"
if __name__ == '__main__':
    os.system(cmd)
    time.sleep(2)
    os.system(cmd_2)