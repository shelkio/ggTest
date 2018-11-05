# _*_ coding: utf-8 _*_

# coding=utf-8
"""根据搜索词下载百度图片"""
import re
import sys
import urllib
import threading
import os
from functools import partial
from time import ctime
from multiprocessing import Pool,Lock
import requests

reload(sys)

sys.setdefaultencoding('utf8')
lock = threading.Lock()
def getPage(keyword, page):
    page = page
    keyword = urllib.quote(keyword, safe='/')
    url_begin = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="
    url = url_begin + keyword + "&pn=" + str(page) + "&gsm=" + str(hex(page)) + "&ct=&ic=0&lm=-1&width=0&height=0"
    return url


def get_onepage_urls(onepageurl):
    try:
        html = requests.get(onepageurl).text
    except Exception as e:
        print(e)
        pic_urls = []
        return pic_urls
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    print pic_urls
    return pic_urls


def down_pic(pic_urls):
    """给出图片链接列表, 下载所有图片"""
    for i, pic_url in enumerate(pic_urls):
        try:
            pic = requests.get(pic_url, timeout=15)
            string = 'C:\\Users\\lishuhang\\Desktop\\png\\' + str(i + 1) + '.jpg'
            urlA = []
            with open(string, 'wb') as f:
                for root, dirs, files in os.walk(string):
                    print(dirs)  # 当前路径下所有子目录
                    print('haha' + files)  # 当前路径下所有非目录子文件
                if pic_url not in urlA:
                    f.write(pic.content)
                    urlA.append(pic_url)
                    print 'biubiu'+str(urlA)
                    print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))
                    print('下载时间:%s' % ctime())
                else:
                    break
        except Exception as e:
            print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
            print(e)
            continue

if __name__ == '__main__':
    keyword = '狗'  # 关键词, 改为你想输入的词即可, 相当于在百度图片里搜索一样
    page_begin = 1
    image_number = 1
    all_pic_urls = []
    while 1:
        if page_begin > image_number:
            break
        print("第%d次请求数据" % page_begin)
        url = getPage(keyword, page_begin)
        onepage_urls = get_onepage_urls(url)
        page_begin += 1
    for i in range(0, 5):
        t = threading.Thread(target=down_pic, name='LoopThread %s' % i, args=(onepage_urls,))
        t.start()
    # for i in onepage_urls:
    #     all_pic_urls.append(i)
    # print all_pic_urls
    # lock = Lock()
    # pool = Pool(3,initializer=init,initargs=(lock,))
    # pool.map(down_pic, all_pic_urls)
    # pool.close()
    # pool.join()
