# Web Scraping for lianjia.com

## 1 爬取信息

进入链家二手房网站：https://bj.lianjia.com/ershoufang/ 网页底部有翻页功能的按钮。
通过点击第1页、第2页的方式，可以发现链家二手房各页网址URL的规律为：

http://bj.lianjia.com/ershoufang/pg(页码)/

## 2 爬虫代码

### 2.1 实现翻页功能

```python
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
#启动chrome浏览器
wait = WebDriverWait(browser, 10)

def get_urls(page):
    """
    获取所有的二手房链接
    :param page:网页
    :return:二手房链接
    """
    print('正在爬取第', page, '页')
    URL = 'https://bj.lianjia.com/ershoufang/pg{}/'.format(page)
    browser.get(URL)

def main():
    for i in range(1, 10):
        get_urls(i)
```



### 2.2  获取每页二手房链接

```Python
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

def get_urls(page):
    """
    获取所有的二手房链接
    :param page:页码
    :return:每个二手房网址的链接
    """
    print('正在爬取第', page, '页')
    URL = 'https://bj.lianjia.com/ershoufang/pg{}/'.format(page)
    browser.get(URL)
    urls_html = browser.page_source
    # 获取页面源代码
    doc = pq(urls_html)
    # pyquery初始化，以便锁定信息位置
    for a in doc('.sellListContent .title a').items():
        url = a.attr.href
        # 获取各个二手房的URL
        print(url)

def main():
    for i in range(1, 10):
        get_urls(i)
    browser.close()
    # 关闭浏览器
```

### 2.3 网页解析

```Python
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

def get_urls(page):
    """
    获取所有的二手房链接
    :param page:页码
    :return:链家二手房的第一、二部分信息
    """
    print('正在爬取第', page, '页')
    URL = 'https://bj.lianjia.com/ershoufang/pg{}/'.format(page)
    browser.get(URL)
    urls_html = browser.page_source
    urls_doc = pq(urls_html)
    for a in urls_doc('.sellListContent .title a').items():
        url = a.attr.href
        get_data(url)

def get_data(url):
    """
    获取某个二手房的数据信息
    :param url: 某个二手房的链接
    :return: 二手房数据
    """
    browser.get(url)
    data_html = browser.page_source
    data_doc = pq(data_html)
    detail = {}
    detail["价格"] = data_doc('.total').text()
    detail["单价"] = data_doc('.unitPriceValue').text()
    detail["建楼时间"] = data_doc('.houseInfo .subInfo').text()
    #获取‘基本属性’
    base_lis = data_doc('.base .content li').items()
    for base_li in base_lis:
        detail[base_li.text()[0:4]] = base_li.text()[4:]
    #获取‘交易属性’
    transaction_lis = data_doc('.transaction .content li').items()
    for transaction_li in transaction_lis:
        detail[transaction_li.text()[0:4]] = transaction_li.text()[4:]
    print(detail)

def main():
    for i in range(1, 10):
        get_urls(i)
    browser.close()
```

### 2.4 导出文件

```Python
import sys
 
sys.stdout = open('house_price_data', mode = 'w',encoding='utf-8')
main()
```

