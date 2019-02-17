# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LiosscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 老师名称
    name = scrapy.Field()
    # 老师职称
    title = scrapy.Field()
    # 老师信息
    info = scrapy.Field()

# 草榴Item
class CaoLiuItem(scrapy.Item):
    # 文件名称
    file_name = scrapy.Field()
    # 指定文件下载的连接
    file_urls = scrapy.Field()
    #文件下载完成后会往里面写相关的信息
    files = scrapy.Field()
