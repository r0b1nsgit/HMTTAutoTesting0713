import time

import page
from base.web_base import WebBase


class PageMpArticle(WebBase):
    # 点击 内容管理
    def page_click_content_manage(self):
        self.base_click(page.mp_content_manage)

    # 点击 发布文章
    def page_click_public_article(self):
        self.base_click(page.mp_publish_article)

    # 输入 文章标题
    def page_input_title(self, title):
        self.base_input(page.mp_title, title)

    # 输入 文章内容
    def page_input_content(self, content):
        # 切换子页
        iframe = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(iframe)
        # 子页输入内容操作
        self.base_input(page.mp_content, content)
        # 切回主页
        self.driver.switch_to.default_content()

    # 点击 封面
    def page_click_cover(self):
        self.base_click(page.mp_cover)

    # 点击 频道
    def page_click_channel(self):
        # 调用WebBase中的方法
        self.web_base_click_element(palceholder_text="请选择", click_text=page.channel)

    # 点击 发布按钮
    def page_click_submit(self):
        self.base_click(page.mp_submit)

    # 获取 发布结果提示
    def page_get_info(self):
        return self.base_get_text(page.mp_result)

    # 组合 发布文章业务方法
    def page_mp_article(self, title, content):
        time.sleep(1)
        # 1.点击内容管理
        self.page_click_content_manage()
        # 2.点击发布文章
        self.page_click_public_article()
        # 3.输入文章标题
        self.page_input_title(title)
        # 4.输入文章内容
        self.page_input_content(content)
        # 5.选择封面
        self.page_click_cover()
        # 6.选择频道
        self.page_click_channel()
        # 7.点击发表按钮
        self.page_click_submit()
