import time

import page
from base.app_base import AppBase


class PageAppLogin(AppBase):
    # 1.输入手机号
    def page_input_phone(self, phone):
        self.base_input(page.app_phone, phone)

    # 2.输入验证码
    def page_input_code(self, code):
        self.base_input(page.app_code, code)

    # 3.点击登陆按钮
    def page_click_login_btn(self):
        time.sleep(1)
        self.base_click(page.app_login_btn)

    # 4.判断页面是否存在 我的
    def page_is_login_success(self):
        return self.app_base_is_exist(page.app_me)

    # 5.组合登陆业务方法
    def page_app_login(self, phone, code):
        self.page_input_phone(phone)
        self.page_input_code(code)
        self.page_click_login_btn()

    # 5.组合登陆业务方法
    def page_app_login_success(self, phone="13812345678", code="246810"):
        self.page_input_phone(phone)
        self.page_input_code(code)
        self.page_click_login_btn()
