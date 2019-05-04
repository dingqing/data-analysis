# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101280600/?query=go&page=1']

    def parse(self, response):
    	for x in response.xpath("//div[@class='job-primary']"):
    		item = {}

    		item['position'] = x.xpath("div[@class='info-primary']/h3/a/div[@class='job-title']/text()").extract_first()
    		item['salary'] = x.xpath("div[@class='info-primary']/h3/a/span[@class='red']/text()").extract_first()
    		item['company'] = x.xpath("div[@class='info-company']/div[@class='company-text']/h3/a/text()").extract_first()

    		yield item

        # 跟踪分页链接
    	next_page = response.css('div.page a.next::attr("href")').extract_first()
    	if next_page is not None:
    		next_full_url = response.urljoin(next_page)
    		yield scrapy.Request(next_full_url, callback=self.parse)