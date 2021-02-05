#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 13:44
# @Author  : weiss
# @File    : base.py
# @Software: PyCharm

"""
    封装基类
"""
import time
# from tools.do_log import DoLog
from tools.path_config import PathConfig
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class Base(object):

    def __init__(self, driver:WebDriver, log):
        self.driver = driver
        self.log = log

    # 等待
    # driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None
    def wait_element(self, loc, timeout=20):
        self.log.info(f"等待{loc}元素可见")
        doc = f"等待{loc}元素可见"
        start_time = time.time()
        try:
            WebDriverWait(self.driver, timeout=timeout).until(EC.visibility_of_element_located(loc))
            end_time = time.time()
            self.log.info("等待元素时间为{:.3f}s".format((end_time - start_time)))
        except Exception as e:
            self.log.error(e)
            self.save_screen_shots(doc)
            raise

    # 定位元素
    def find_elem(self, loc, doc=""):
        try:
            self.wait_element(loc)
            element = self.driver.find_element(*loc)
            # print(f"element is {element}")
            return element
        except Exception as e:
            self.save_screen_shots(doc)
            raise e

    # 操作元素 -- 点击元素
    def click_element(self, loc, doc=""):
        try:
            self.wait_element(loc)
            element = self.find_elem(loc)
            element.click()
        except Exception as e:
            self.save_screen_shots(doc)

    # 操作元素 -- 向特定元素传值
    def send_word_element(self, loc, word, doc=""):
        try:
            self.wait_element(loc)
            element = self.find_elem(loc)
            element.send_keys(word)
        except Exception as e:
            self.save_screen_shots(doc)

    # 操作元素 -- 获取元素文本值
    def get_element_text(self, loc, doc=""):
        self.wait_element(loc)
        elem = self.find_elem(loc, doc)
        try:
            return elem.text
        except Exception:
            self.save_screen_shots(doc)

    # 鼠标操作 - 移动悬浮操作元素
    def move_to_hold_element(self, loc, doc=""):
        self.wait_element(loc)
        ac = ActionChains(self.driver)
        ac.move_to_element(self.find_elem(loc, doc))
        ac.perform()

    # 处理alert框
    def deal_alert_elem(self,doc=""):
        try:
            self.driver.switch_to.alert.accept()
            time.sleep(2)
        except Exception:
            self.save_screen_shots(doc)

    # 滚动至元素可见
    def scroll_to_visibility_element(self, loc, doc=""):
        try:
            elem = self.find_elem(loc, doc)
            self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        except Exception:
            self.save_screen_shots(doc)

    # 截图
    def save_screen_shots(self, doc=""):
        if doc == "":
            self.save_screen_shots(doc)
        else:
            screen_path = PathConfig.get_screenshots_path(doc)
            self.driver.save_screenshot(screen_path)

