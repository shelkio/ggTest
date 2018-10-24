# _*_ coding: utf-8 _*_
from framework.base_page import BasePage

class LoginProcess(BasePage):
    #首页登录按钮
    login_link = u"link_text=>登录"
    #切换手机号登录按钮
    phone_login = r'xpath=>//*[@id="app"]/div/div/div/div/div/div/div[3]/a'
    #用户名输入框
    unm = r"class_name=>login-f-i-uname"
    #密码输入框
    pwd = r"class_name=>login-f-i-pwd"
    #登录页面登录按钮
    login_btn = r"class_name=>login-btn"
    def click_login(self):
        self.click(self.login_link)
    def unm_pwd_login(self,unm,pwd):
        self.click(self.phone_login)
        self.type(self.unm,unm)
        self.type(self.pwd,pwd)
        self.click(self.login_btn)

