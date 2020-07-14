import time

import page
from base.web_base import WebBase


class PageMisAudit(WebBase):
    # 1.点击信息管理
    def page_click_info_manage(self):
        # 等待
        time.sleep(1)
        # 点击
        self.base_click(page.mis_info_manage)

    # 2.点击内容审核
    def page_click_content_audit(self):
        # 等待
        time.sleep(1)
        # 点击
        self.base_click(page.mis_content_audit)

    # 3.输入文章标题
    def page_input_title(self, title):
        # 输入内容
        self.base_input(page.mis_title, title)

    # 4.输入文章频道
    def page_input_channel(self, channel):
        # 输入内容
        self.base_input(page.mis_channel, channel)

    # 5.选择状态
    def page_click_status(self, palceholder_text="请选择状态", click_text='待审核'):
        # 点击
        self.web_base_click_element(palceholder_text, click_text)

    # 6.点击查询按钮
    def page_click_find(self):
        # 点击
        self.base_click(page.mis_find)
        # 等待
        time.sleep(1)

    # 7.获取文章id
    def page_get_article_id(self):
        return self.base_get_text(page.mis_article_id)

    # 8.点击通过
    def page_click_pass_btn(self):
        # 点击
        self.base_click(page.mis_pass)

    # 9.点击确认
    def page_click_confirm_pass(self):
        # 点击
        time.sleep(1)
        # 等待
        self.base_click(page.mis_confirm_pass)

    # 10.组合发布业务方法
    def page_mis_audit(self, title, channel):
        self.page_click_info_manage()
        self.page_click_content_audit()
        self.page_input_title(title)
        self.page_input_channel(channel)
        self.page_click_status()
        self.page_click_find()
        self.article_id = self.page_get_article_id()
        print("获取文章id:{}".format(self.article_id))
        self.page_click_pass_btn()
        self.page_click_confirm_pass()

    def page_assert_audit(self):
        time.sleep(1)
        # 查看审核通过文章
        self.page_click_status(click_text="审核通过")
        self.page_click_find()
        # 判断是否存在
        return self.web_base_is_exist(self.article_id)
