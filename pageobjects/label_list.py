# _*_ coding: utf-8 _*_
from framework.base_page import BasePage
import random
import sys
class LabelList(BasePage):
    #点击标签
    def click_label(self):
        num = random.randint(1,7)
        cLabel = 'xpath=>/html/body/div[1]/div/div[1]/div[4]/ul[2]/li[' + bytes(num) + ']/p'
        sLabel = self.find_element(cLabel).text
        self.click(cLabel)
        return sLabel
    #得到征稿令列表标签
    def get_label(self):
        self.sleep(1)
        for num in range(1, 6):
            gLabel = 'xpath=>//*[@id="app"]/div/div[2]/div[1]/ul/li[' + bytes(num) + ']/div[1]/a/ul'
            aLabel = self.find_element(gLabel).text
        return aLabel
    def Contrast_label(self):
        LabelClick = LabelList(self.driver)
        a = LabelClick.click_label()
        b = LabelClick.get_label()
        reload(sys)
        sys.setdefaultencoding('UTF-8')
        results = str(b).find(str(a))
        if results < 0:
            print u'标签不匹配'
        else:
            print u'标签匹配'