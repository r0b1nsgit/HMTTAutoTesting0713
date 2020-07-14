from selenium.webdriver.common.by import By

# 自媒体端
from tools.read_yaml import read_yaml

url_mp = "http://ttmp.research.itcast.cn/#/login"

# 用户名
mp_username = (By.CSS_SELECTOR, '[placeholder="请输入手机号"]')
# 验证码
mp_code = (By.CSS_SELECTOR, '[placeholder="验证码"]')
# 登陆按钮
mp_login_btn = (By.CSS_SELECTOR, '.el-button--primary')
# 昵称
mp_nickname = (By.CSS_SELECTOR, '.user-name')

# 内容管理
mp_content_manage = By.XPATH, "//span[text()='内容管理']/.."
# 文章发布"
mp_publish_article = By.XPATH, "//*[contains(text(),'发布文章')]"
# 文章标题
mp_title = By.CSS_SELECTOR, '[placeholder="文章名称"]'
# iframe
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"
# 文章内容
mp_content = By.CSS_SELECTOR, '#tinymce'
# 封面
mp_cover = By.XPATH, "//*[text()='自动']"
# 发表
mp_submit = By.XPATH, '//*[text()="发表"]/..'
# 结果
mp_result = By.XPATH, "//*[contains(text(),'新增文章成功')]"

# 后台管理
url_mis = "http://ttmis.research.itcast.cn/#/"
title = read_yaml("mp_article.yaml")[0][0]
channel = read_yaml("mp_article.yaml")[0][-1]
# 用户名
mis_username = (By.CSS_SELECTOR, '[name="username"]')
# 验证码
mis_password = (By.CSS_SELECTOR, '[name="password"]')
# 登陆按钮
mis_login_btn = (By.CSS_SELECTOR, '#inp1')
# 昵称
mis_nickname = (By.CSS_SELECTOR, '.user_info')

# 信息管理
mis_info_manage = By.XPATH, "//*[text()='信息管理']/.."

# 内容审核
mis_content_audit = By.XPATH, "//*[text()='内容审核']/.."

# 文章标题
mis_title = By.CSS_SELECTOR, "[placeholder='请输入: 文章名称']"
# 文章频道
mis_channel = By.CSS_SELECTOR, "[placeholder='请输入: 频道']"

# 查询
mis_find = By.CSS_SELECTOR, ".find"
# 文章id
mis_article_id = By.CSS_SELECTOR, ".cell>span"
# 通过
mis_pass = By.XPATH, "//*[text()='通过']/.."
# 确认
mis_confirm_pass = By.CSS_SELECTOR, ".el-button--primary"

# --------------------------------------
# app
# 包名
appPackage = "com.itcast.toutiaoApp"
# 启动名
appActivity = ".MainActivity"

# 手机号
app_phone = By.XPATH, "//*[@index='1' and @class='android.widget.EditText']"

# 验证码
app_code = By.XPATH, "//*[@index='2' and @class='android.widget.EditText']"

# 登陆
app_login_btn = By.XPATH, "//*[@text='登录' and @class='android.widget.Button']"

# 我的
app_me = By.XPATH, "//*[@index='3' and contains(@text,'我的')]"

# 文章列表
# 频道
app_channel_area = By.XPATH, "//*[@class='android.widget.HorizontalScrollView']"
# 文章
app_artical_area = By.XPATH, "//*[@index='0' and @bounds='[0,390][1080,1716]']"
