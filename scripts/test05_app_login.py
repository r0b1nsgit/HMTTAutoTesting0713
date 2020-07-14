import pytest

from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog().get_logger()


class TestAppLogin:
    def setup_class(self):
        driver = GetDriver.get_app_driver()
        self.app = PageIn(driver).page_get_PageAppLogin()

    def teardown_class(self):
        GetDriver.quit_app_driver()

    @pytest.mark.parametrize('phone,code', read_yaml("app_login.yaml"))
    def test_app_login(self, phone, code):
        self.app.page_app_login(phone, code)
        try:
            assert self.app.page_is_login_success()

        except Exception as e:
            log.error("断言失败:{}".format(e))
            self.app.base_get_img()
            raise
