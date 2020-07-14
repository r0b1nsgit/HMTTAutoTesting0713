import time

import page
from base.web_base import WebBase


class PageMisLogin(WebBase):
    # 输入 用户名
    def page_input_username(self, username):
        self.base_input(page.mis_username, username)

    # 输入 密码
    def page_input_password(self, password):
        self.base_input(page.mis_password, password)

    # 点击 登陆按钮
    def page_click_login_btn(self):
        js = "document.getElementById('inp1').disabled=false"
        self.driver.execute_script(js)
        time.sleep(1)
        self.base_click(page.mis_login_btn)

    # 获取昵称
    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    # 组合后台管理页面的登陆业务方法
    def page_mis_login(self, username, password):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()

    # 组合后台管理页面的登陆业务方法
    def page_mis_login_success(self, username="testid", password="testpwd123"):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()
