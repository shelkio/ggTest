# # _*_ coding: utf-8 _*_
# from selenium import webdriver
# webdriver = webdriver.Chrome()
# webdriver.get('https://www.baidu.com')
# i = 1
# j=np
# for i in range(100):
#     webdriver.find_element_by_id('kw').send_keys(i)
#     screen_name = 'C:\\Users\\lishuhang\\Desktop\\png\\' + str(i) + '.png'
#     webdriver.get_screenshot_as_file(screen_name)
#     webdriver.find_element_by_id('kw').clear()
#     i = i+1
#     print "start to %s." % ctime()
from selenium import webdriver

# 测试用例
from time import sleep, ctime
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import threading




def test_baidu(browser, search):
    print('start:%s' % ctime())
    print('browser:%s,' % browser)
    if browser == 'ie':
        driver = webdriver.Ie()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == 'ff':
        driver = webdriver.Firefox()
    else:
        print("browser 参数有误，只能为ie ，ff，chrome")
    driver.set_window_size(500, 1000)
    driver.get("https://www.baidu.com")
    driver.find_element_by_name("wd").send_keys(search)
    sleep(2)
    driver.quit()


if __name__ == '__main__':
    # 启动参数（指定浏览器与百度收缩内容）
    lists = {'chrome': 'threading','ff': 'python'}
    threads = []
    files = range(len(lists))
    pool = Pool()
    pool.map(test_baidu)
    pool.close()
    pool.join()
    # # 创建线程
    # for browser, search in lists.items():
    #     t = threading.Thread(target=test_baidu, args=(browser, search))
    #     threads.append(t)
    #
    # # 启动线程
    # for t in files:
    #     threads[t].start()
    # for t in files:
    #     threads[t].join()
    print('end:%s' % ctime())