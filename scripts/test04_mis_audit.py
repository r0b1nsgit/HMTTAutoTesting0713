import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

log = GetLog.get_logger()


class TestMidAudit:

    def setup_class(self):
        # 驱动
        driver = GetDriver.get_web_driver(page.url_mis)
        # 入口
        page_in = PageIn(driver)
        # 登陆
        page_in.page_get_PageMisLogin().page_mis_login_success()
        # 审核
        self.audit = page_in.page_get_PageMisAudit()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    def test_mis_audit(self, title=page.title, channel=page.channel):
        self.audit.page_mis_audit(title, channel)

        try:
            assert self.audit.page_assert_audit()
        except:
            log.error("断言失败")
            self.audit.base_get_img()
            raise
