import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMisLogin:
    def setup_class(self):
        driver = GetDriver.get_web_driver(page.url_mis)
        self.login = PageIn(driver).page_get_PageMisLogin()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("username,password,expect", read_yaml('mis_login.yaml'))
    def test_mis_login(self, username, password, expect):
        self.login.page_mis_login(username, password)

        try:
            assert expect in self.login.page_get_nickname()
        except Exception as e:
            log.error("断言失败:{}".format(e))
            self.login.base_get_img()
            raise
