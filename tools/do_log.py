#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/30 09:33
# @Author  : weiss
# @File    : do_log.py
# @Software: PyCharm


import logging

class DoLog(logging.Logger):
    """
           1. 日志收集器： logger: 日记本
           2. 日志收集器级别 level
           3. 日志收集器准备 handler
           4. 日志处理器级别设置
           5. 设置日志格式 format  日期： 重要程度： 分类(工作， 生活)
           6. 添加日志处理器
    """

    def __init__(self, name='root', log_level="DEBUG", file_name=None):
        super().__init__(name)
        self.setLevel(log_level)
        fmt = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        if file_name:
            # 将日志写入文件
            file_handler = logging.FileHandler(file_name, 'a', encoding="utf-8")
            file_handler.setLevel(log_level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
        # 默认方式  日志显示在控制台上
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(fmt)
        self.addHandler(console_handler)

if __name__ == '__main__':
    pass
