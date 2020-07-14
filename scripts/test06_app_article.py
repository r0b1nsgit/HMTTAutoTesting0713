import time

import pytest

from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestAppArticle:
    def setup_class(self):
        # 驱动
        driver = GetDriver.get_app_driver()
        # 入口
        page_in = PageIn(driver)
        # 登陆
        page_in.page_get_PageAppLogin().page_app_login_success()
        # 页面
        self.article = page_in.page_get_PageAppArticle()

    def teardown_class(self):
        GetDriver.quit_app_driver()

    @pytest.mark.parametrize("channel,article", read_yaml('app_article.yaml'))
    def test_app_article(self, channel, article):
        try:
            self.article.page_app_article(channel, article),
        except Exception as e:
            log.error("未找到")
            self.article.base_get_img()
            raise
