import scrapy
from scrapy.http import Request
from tuchong.items import TuchongItem
import json


class tuchongSpider(scrapy.Spider):
    name = 'tuchong'
    allowed_domins = ['tuchong.com']
    start_urls = ['https://tuchong.com/rest/users/2333677/following?count=2000&page=1&before_timestamp=1507983429']

    def parse(self, response):
        s = json.loads(response.text)
        item = TuchongItem()
        for i in range(2000):
            t = s["sites"][i]["site_id"]
            name=s["sites"][i]["name"]
            location=s["sites"][i]["location"]
            count = s["sites"][i]["following"]
            url = s["sites"][i]["url"]
            item['id'] = t
            item['name'] = name
            item['location'] = location
            item['following'] = count
            item['followers'] = s["sites"][i]["followers"]
            item['url'] = url
            item['description'] = s["sites"][i]["description"]
            u ='https://tuchong.com/rest/users/' + str(t) + '/following?count=' + str(count) + '&page=1&before_timestamp=1507983429'
            print u
            yield item
            yield Request(u, callback=self.parse)

