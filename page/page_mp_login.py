# 创建页面类
from base.base import Base
import page
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMpLogin(WebBase):
    # 输入 用户名
    def page_input_username(self, username):
        # 调用父类的输入方法, 操作 page用户名元素
        self.base_input(page.mp_username, username)

    # 输入 验证码
    def page_input_code(self, code):
        # 调用父类的输入方法, 操作 page验证码元素
        self.base_input(page.mp_code, code)

    # 点击 登陆按钮
    def page_click_login_btn(self):
        # 调用父类的点击方法, 操作 page登陆按钮元素
        self.base_click(page.mp_login_btn)

    # 获取 昵称
    def page_get_nickname(self):
        # 调用父类的获取文本方法, 操作 page昵称元素
        nickname = self.base_get_text(page.mp_nickname)
        # 返回昵称
        return nickname

    # 组合业务方法 登陆业务
    def page_mp_login(self, username, code):
        # 调用页面的输入用户名, 输入验证码, 点击登陆按钮
        log.info("正在进行登陆,用户名:{}, 验证码:{} ...".format(username, code))
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()

    # 组合业务方法 登陆业务
    def page_mp_login_success(self, username='13812345678', code="246810"):
        # 调用页面的输入用户名, 输入验证码, 点击登陆按钮
        log.info("正在进行登陆,用户名:{}, 验证码:{} ...".format(username, code))
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()
