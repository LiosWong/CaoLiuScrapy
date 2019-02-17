# -*- coding: utf-8 -*-
import scrapy
import json
from LiosScrapy.items import CaoLiuItem
from scrapy.http.request import Request
import sys
type = sys.getfilesystemencoding()


class CaoliuSpider(scrapy.Spider):
    name = 'caoliu'
    allowed_domains = ['http://cl.57v.xyz']
    start_urls = ['http://cl.57v.xyz/thread0806.php?fid=2&search=&page=0']
    # 列表解析
    def parse(self, response):
        node_list = response.xpath("//td[@class='tal']")
        next_page = response.xpath("//a[text()='下一頁']/@href").extract()[0]
        for node in node_list:
            if not len(node.xpath('./h3/a/text()').extract()) or not len(node.xpath('./h3/a/@href').extract()):
                continue
            fileName = node.xpath('./h3/a/text()').extract()[0]
            listUrl = node.xpath('./h3/a/@href').extract()[0]
            # print('fileName,listUrl', fileName, listUrl)
            yield scrapy.Request(self.allowed_domains[0] + "/" + listUrl, callback=self.parseDetail, meta={'fileName': fileName}, dont_filter=True)
            # print(json.dumps(dict(item),ensure_ascii=False))
        if next_page not in self.allowed_domains[0]:
            yield scrapy.Request(self.allowed_domains[0] + "/" + next_page,callback=self.parse,dont_filter=True)

    # 解析详情页
    def parseDetail(self, response):
        fileName = response.meta['fileName']
        # print('fileName:',fileName)
        node_list = response.xpath(
            '//a[@style="cursor:pointer;color:#008000;"]')
        for node in node_list:
            yield scrapy.Request(node.xpath('./@href').extract()[0], callback=self.parseDownLoanUrl, meta={'fileName': fileName}, dont_filter=True)
            # print("下载页面====>",node.xpath('./@href').extract()[0]);
            break

    # 拼接种子、下载
    def parseDownLoanUrl(self, response):
        fileName = response.meta['fileName']
        refNode = response.xpath("//input[@type='hidden' and @name='ref']/@value")[0].extract()
        reffNode = response.xpath("//input[@type='hidden' and @name='reff']/@value")[0].extract()
        torrentUrl = "http://www.rmdown.com/download.php?" + "ref="+str(refNode)+ "&reff="+str(reffNode)
        item = CaoLiuItem()
        item['file_urls'] = torrentUrl
        item['file_name'] = fileName+".torrent"
        # print('%d====>%d',fileName,torrentUrl)
        yield item
