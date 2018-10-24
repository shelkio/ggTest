# _*_ coding: utf-8 _*_
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.label_list import LabelList
class LabelClick(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()
    def test_click_label(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法
        :return:
        """
        CLabel = LabelList(self.driver)
        CLabel.Contrast_label()

if __name__ == '__main__':
    unittest.main()
