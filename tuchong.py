import scrapy
from scrapy.http import Request
from tuchong.items import TuchongItem
import json

class tuchongSpider(scrapy.Spider):
    name = 'tuchong'
    allowed_domins = ['tuchong.com']
    start_urls = ['https://tuchong.com/rest/tags/%E4%BA%BA%E5%83%8F/posts?page=2&count=20&order=weekly']

    def parse(self, response):
        s = json.loads(response.text)
        for i in range(20):
            t = s["postList"][i]["url"]
            yield Request(t, callback=self.parse_name)

        for i in range(3, 100):
            page_url = 'https://tuchong.com/rest/tags/%E4%BA%BA%E5%83%8F/posts?page={}&count=20&order=weekly'.format(i)
            yield Request(page_url, callback=self.parse)

    def parse_name(self, response):
        items = TuchongItem()
        items['title'] = response.xpath('//title/text()').extract()
        items['url']= response.xpath('//img[@class="multi-photo-image"]/@src').extract()
        yield items

