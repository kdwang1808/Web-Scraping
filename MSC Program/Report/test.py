#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import jieba
from os import path  # 获取文档路径
from PIL import Image
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

background = np.array(Image.open("background3.jpg"))  # 背景图
recent_path = path.dirname(__file__)
stop_words_path = 'stopwords.txt'

text_path = 'house_price_data(1).txt'
text = open(path.join(recent_path, text_path), encoding='utf-8').read()


# 分词预处理函数
def pre_build(data):
    my_words_list = []
    seg_list = jieba.cut(data, cut_all=False)
    list_str = '/'.join(seg_list)
    # 打开停用词表
    f_stop = open(stop_words_path, encoding="utf8")
    try:
        f_stop_text = f_stop.read()
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split("\n")
    for word in list_str.split('/'):
        if not(word.split()) in f_stop_seg_list and len(word.strip()) >> 1:
            my_words_list.append(word)
    return ' '.join(my_words_list)


text1 = pre_build(text)
graph = WordCloud(
    background_color="white",
    max_words=200,
    mask=background,
    max_font_size=60,
    random_state=42,
    font_path='方正兰亭细黑_GBK.TTF'
).generate(text1)
# 设置字体
my_font = fm.FontProperties(fname='方正兰亭细黑_GBK.TTF')
# 背景图片
image_colors = ImageColorGenerator(background)
plt.imshow(graph.recolor(color_func=image_colors))
plt.axis("off")
plt.figure()
plt.axis("off")
plt.imshow(background, cmap=plt.cm.gray)
plt.show()

