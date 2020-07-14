# 驱动工具类
from selenium import webdriver
import appium.webdriver

import page


class GetDriver:
    # 驱动保存
    __web_driver = None

    __app_driver = None

    # 驱动获取
    @classmethod
    def get_web_driver(cls, url):
        # 如果__web_driver为空,需要先创建
        if cls.__web_driver is None:
            cls.__web_driver = webdriver.Chrome()
            cls.__web_driver.maximize_window()
            cls.__web_driver.get(url)
        # 返回驱动
        return cls.__web_driver

    # 驱动销毁
    @classmethod
    def quit_web_driver(cls):
        # 如果__web_driver为空, 不需要退出置空
        if cls.__web_driver:
            cls.__web_driver.quit()
            cls.__web_driver = None

    # 获取app应用driver
    @classmethod
    def get_app_driver(cls):
        # 判断 __app_driver 为空
        if cls.__app_driver is None:
            # 设置启动
            desired_caps = {}
            # 必填-且正确
            desired_caps['platformName'] = 'Android'
            # 必填-且正确
            desired_caps['platformVersion'] = '5.1'
            # 必填
            desired_caps['deviceName'] = 'emulator-5554'
            # APP包名
            desired_caps['appPackage'] = page.appPackage
            # 启动名
            desired_caps['appActivity'] = page.appActivity

            # windows注意输入键盘编码
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True

            # 设置driver
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 返回cls.__app_driver
        return cls.__app_driver

    # 退出app应用driver
    @classmethod
    def quit_app_driver(cls):
        # 判断不为空
        if cls.__app_driver:
            # 退出操作
            cls.__app_driver.quit()
            # 置空操作
            cls.__app_driver = None


if __name__ == '__main__':
    GetDriver.get_app_driver()
    GetDriver.quit_app_driver()
