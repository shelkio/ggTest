# _*_ coding: utf-8 _*_
from framework.browser_engine import BrowserEngine
from pageobjects.login_process import LoginProcess
import unittest
class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def login(self):
        login = LoginProcess(self.driver)
        login.click_login()
        login.unm_pwd_login(u'友2','333333')

if __name__ == '__main__':
    unittest.main()