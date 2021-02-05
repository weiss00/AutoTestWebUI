#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 10:15
# @Author  : weiss
# @File    : path_config.py
# @Software: PyCharm
import datetime
import pathlib

class PathConfig():

    __base_url = pathlib.Path(__file__).parent.parent

    @staticmethod
    def get_screenshots_path(file_name):
        screenshots_path = PathConfig.__base_url / 'output' / 'screenshots' / f'{file_name}.png'
        return str(screenshots_path)

    @staticmethod
    def get_allure_path():
        allure_path = PathConfig.__base_url / 'output' / 'allure_report'
        return str(allure_path)

    @staticmethod
    def get_html_report():
        html_report = PathConfig.__base_url / 'output' / 'html_report' / 'test_report.html'
        return str(html_report)

    @staticmethod
    def get_log_path():
        time_format = datetime.datetime.now().strftime("%Y%m%d_%H%M_")
        log_path = PathConfig.__base_url / 'output' / 'logs' / time_format
        return str(log_path) + "log.txt"

if __name__ == '__main__':
    data = PathConfig.get_html_report()
    print(data)