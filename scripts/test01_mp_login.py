# 创建测试类
import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMpLogin:

    # 获取驱动和页面对象
    def setup_class(self):
        # 1. 获取驱动
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2. 获取页面对象(通过统一入口类PageIn)
        self.mp = PageIn(driver).page_get_PageMpLogin()
        pass

    # 销毁浏览器驱动对象
    def teardown_class(self):
        # 销毁浏览器
        GetDriver.quit_web_driver()

    # 实现用例方法业务断言
    @pytest.mark.parametrize("username,code,expect", read_yaml("mp_login.yaml"))
    def test_mp_login(self, username, code, expect):
        # 通过登陆页面对象调用登陆业务方法
        self.mp.page_mp_login(username=username, code=code)
        # 断言
        try:

            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            print("断言失败:", e)
            log.error("断言失败,问题是:{}...".format(e))
            # 截图
            self.mp.base_get_img()
            # 抛出
            raise
