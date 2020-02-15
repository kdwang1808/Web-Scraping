#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
  # 启动chrome浏览器
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