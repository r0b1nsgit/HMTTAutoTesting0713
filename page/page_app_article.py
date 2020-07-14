import page
from base.app_base import AppBase


class PageAppArticle(AppBase):
    # 查找频道
    def page_click_channel(self, click_text):
        self.app_base_right_wipe_left(page.app_channel_area, click_text)

    # 查找文章
    def page_click_article(self, click_text):
        self.app_base_down_wipe_up(page.app_artical_area, click_text)

    # 查找文章
    def page_app_article(self, channel, article):
        self.page_click_channel(channel)
        self.page_click_article(article)
