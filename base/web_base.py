import time

from selenium.webdriver.common.by import By

from base.base import Base


class WebBase(Base):
    # web页面公共操作

    def web_base_click_element(self, palceholder_text, click_text):
        time.sleep(1)
        # 点击父级框
        loc = By.CSS_SELECTOR, "[placeholder='{}']".format(palceholder_text)
        self.base_click(loc)
        time.sleep(1)
        # 点击选项
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        self.base_click(loc)

    def web_base_is_exist(self, text):
        # 通过xpath 定位指定文本内容
        loc = By.XPATH, "//*[contains(text(),'{}')]".format(text)
        # 进行元素定位 - 定位成功 返回True 定位失败返回False
        try:
            self.base_find(loc, timeout=3)
            print("在页面中查找到:{}".format(loc))
            return True
        except:
            print("在页面中未查找到:{}".format(loc))
            return False
