import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from base.base import Base


class AppBase(Base):
    def app_base_is_exist(self, loc):
        # 进行元素定位 - 定位成功 返回True 定位失败返回False
        try:
            self.base_find(loc, timeout=3)
            print("在页面中查找到:{}".format(loc))
            return True
        except:
            print("在页面中未查找到:{}".format(loc))
            return False

    def app_base_right_wipe_left(self, area_loc, click_text):
        # 1.参照物
        ele = self.base_find(area_loc)

        # 2.坐标点
        y = ele.location.get("y")

        # 3.宽高值
        width = ele.size.get("width")
        height = ele.size.get("height")

        # 4.起始点坐标
        start_x = width * 0.8
        start_y = y + height + 0.5
        end_x = width * 0.2
        end_y = y + height + 0.5

        # 目标元素定位信息
        loc = By.XPATH, "//*[@class='android.widget.HorizontalScrollView']//*[contains(@text,'{}')]".format(click_text)

        # 5. 循环操作
        while True:
            # 1. 获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 2. 捕获异常
            try:
                time.sleep(2)
                # 1. 查找元素
                el = self.base_find(loc, timeout=3)
                # 2. 输出提示信息
                print("找到：{} 元素啦！".format(loc))
                time.sleep(2)
                # 3. 点击元素
                el.click()
                # 4. 跳出循环
                break
            # 3. 处理异常
            except:
                # 1. 输出提示信息
                print("未找到：{}元素！".format(loc))
                # 2. 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
            # 4. 判断是否为最后一页
            if page_source == self.driver.page_source:
                # 1. 输出提示信息
                print("滑到最后一屏幕，未到找元素！")
                # 2. 抛出未找到元素异常
                raise NoSuchElementException

    def app_base_down_wipe_up(self, area_loc, click_text):
        # 1.参照物
        ele = self.base_find(area_loc)

        # 2.宽高值
        width = ele.size.get("width")
        height = ele.size.get("height")

        # 3.起始点坐标
        start_x = width * 0.5
        start_y = height * 0.8
        end_x = width * 0.5
        end_y = height * 0.2

        # 目标元素定位信息
        loc = By.XPATH, "//*[@bounds='[0,390][1080,1716]']//*[contains(@text,'{}')]".format(click_text)

        # 4. 循环操作
        while True:
            # 1. 获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 2. 捕获异常
            try:
                time.sleep(2)
                # 1. 查找元素
                time.sleep(1)
                el = self.base_find(loc, timeout=3)
                time.sleep(1)
                # 2. 输出提示信息
                print("文章找到文章：{} 元素啦！".format(loc))
                time.sleep(2)
                # 3. 点击元素
                el.click()
                # 4. 跳出循环
                break
            # 3. 处理异常
            except:
                # 1. 输出提示信息
                print("未找到文章：{}元素！".format(loc))
                # 2. 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
            # 4. 判断是否为最后一页
            if page_source == self.driver.page_source:
                # 1. 输出提示信息
                print("滑到最后一屏幕，未到找元素！")
                # 2. 抛出未找到元素异常
                raise NoSuchElementException
