# 创建类大驼峰
import os

import allure
from selenium.webdriver.support.wait import WebDriverWait

from config import BASE_PATH
from tools.get_log import GetLog

log = GetLog.get_logger()


class Base:
    # 初始化方法
    def __init__(self, driver):
        # 获取浏览器驱动
        self.driver = driver

    # 查找 方法封装  -- (策略, 依据)
    def base_find(self, loc, timeout=30, poll=0.5):
        # 元素定位 -- 元素等待(显式等待)  self.driver.find_element(*loc)
        log.info("元素{}正在进行定位操作...".format(loc))
        element = WebDriverWait(self.driver,
                                timeout=timeout,
                                poll_frequency=poll).until(lambda d: d.find_element(*loc))
        # 返回元素对象
        return element

    # 输入 方法封装
    def base_input(self, loc, value):
        """
        指定元素完成输入操作
        :param loc: 元素定位信息
        :param value: 输入内容
        :return: 无
        """
        # 1. 定位元素
        el = self.base_find(loc)
        # 2. 元素清空
        log.info("元素{}正在进行清空操作...".format(loc))
        el.clear()
        # 3. 元素输入
        log.info("元素{}正在进行输入操作,内容是{}...".format(loc, value))
        el.send_keys(value)

    # 点击 方法封装
    def base_click(self, loc):
        """
        定位元素完成定位操作
        :param loc: 元素定位信息
        :return: 无
        """
        # 定位元素
        log.info("元素{}正在进行点击操作...".format(loc))
        el = self.base_find(loc)
        # 元素点击
        el.click()

    # 获取 文本封装
    def base_get_text(self, loc):
        """
        定位元素获取文本
        :param loc: 元素定位信息
        :return: 元素文本信息
        """
        # 定位元素
        el = self.base_find(loc)
        # 获取文本
        t = el.text
        log.info("元素{}正在进行获取文本操作,文本是:{}...".format(loc, t))
        return t

    # 截图方法
    def base_get_img(self):
        imgname = BASE_PATH + os.sep + "image" + os.sep + "err.png"
        # 保存截图 error日志
        log.error("断言失败,正在截图...")
        self.driver.get_screenshot_as_file(imgname)

        # 写入报告
        self.__base_write_img()

    # 附加报告方法
    def __base_write_img(self):
        # 读取图片
        log.error("断言失败,日志正在附加截图...")
        imgname = BASE_PATH + os.sep + "image" + os.sep + "err.png"
        with open(imgname, 'rb') as f:
            # 附加报告
            allure.attach("断言失败:", f.read(), allure.attach_type.PNG)
