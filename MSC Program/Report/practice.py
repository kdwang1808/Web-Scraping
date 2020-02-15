#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from pyecharts.charts import Bar
import  matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

text_from_file_with_apath =open("house_price_data(1).txt", encoding="UTF-8").read()

wordlist_after_jieba =jieba.cut(text_from_file_with_apath, cut_all=True)

wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud(font_path="方正兰亭细黑_GBK.TTF").generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()