# 定义统一入口类, 用于获取页面对象
from page.page_app_article import PageAppArticle
from page.page_app_login import PageAppLogin
from page.page_mis_audit import PageMisAudit
from page.page_mis_login import PageMisLogin
from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin


class PageIn:
    # 获取浏览器驱动
    def __init__(self, driver):
        self.driver = driver

    # 获取自媒体后台登陆页面对象
    def page_get_PageMpLogin(self):
        # 实例化页面对象,传入驱动
        page = PageMpLogin(self.driver)
        # 返回页面对象
        return page

    # 获取自媒体后台发布文章页面对下昂
    def page_get_PageMpArticle(self):
        page = PageMpArticle(self.driver)
        return page

    # 获取后台管理页面对象
    def page_get_PageMisLogin(self):
        page = PageMisLogin(self.driver)
        return page

    # 获取后台管理审核页面对象
    def page_get_PageMisAudit(self):
        page = PageMisAudit(self.driver)
        return page

    # 获取app端登陆页面
    def page_get_PageAppLogin(self):
        page = PageAppLogin(self.driver)
        return page

    # 获取app端文章页面对象
    def page_get_PageAppArticle(self):
        page = PageAppArticle(self.driver)
        return page
