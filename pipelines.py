# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.pipelines.files import FilesPipeline
from scrapy.http.request import Request
class LiosscrapyPipeline(object):
    def __init__(self):
        self.f = open("/Users/wenchao.wang/LiosWang/sublimetext/LiosScrapy/data/itcash_pipeline.json",'w')
    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.f.write(content)
        return item
    def close_spider(self,spider):
        self.f.close()

class CaoLiuPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        file_url = item['file_urls']
        meta = {'filename': item['file_name']}
        yield Request(url=file_url, meta=meta)
    def file_path(self, request, response=None, info=None):
        return request.meta.get('filename','')

