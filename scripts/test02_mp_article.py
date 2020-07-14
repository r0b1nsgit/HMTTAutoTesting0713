import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMpArticle:
    def setup_class(self):
        # 驱动
        driver = GetDriver.get_web_driver(page.url_mp)
        # 入口
        page_in = PageIn(driver)
        # 登陆
        page_in.page_get_PageMpLogin().page_mp_login_success()
        # 发布
        self.article = page_in.page_get_PageMpArticle()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("title,content,expect,channel", read_yaml("mp_article.yaml"))
    def test_mp_article(self, title, content, expect, channel):
        self.article.page_mp_article(title, content)
        log.info("给{}频道添加文章".format(channel))
        # 断言
        # 断言失败截图 , 记录日志
        # 参数化
        try:
            # 断言
            assert expect == self.article.page_get_info()
        except Exception as e:
            # 断言失败截图 , 记录日志
            log.error("断言失败:{}".format(e))
            self.article.base_get_img()
            # 抛出
            raise
