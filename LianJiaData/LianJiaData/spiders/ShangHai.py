# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
from LianJiaData.items import LianjiadataItem


class ShanghaiSpider(scrapy.Spider):
    name = 'ShangHai'
    allowed_domains = ['sh.lianjia.com']
    start_urls = ['https://sh.lianjia.com/ershoufang/baoshan/']

    def parse(self, response):
        post_urls = response.css(".sellListContent .LOGCLICKDATA .info.clear .title a::attr(href)").extract()
        for post_url in post_urls:
            yield Request(url = parse.urljoin(response.url,post_url),callback = self.parse_detail)
            # print(post_url)
        for i in range(1,101):
            url = 'https://sh.lianjia.com/ershoufang/baoshan/pg{}/'.format(str(i))
            yield Request(url, callback=self.parse)

    def parse_detail(self,response):
        lianjia_item = LianjiadataItem()
        TotlePrice = response.css(".overview .price span::text").extract()[0]
        UnitPrice = response.css(".overview .price span::text").extract()[2]
        Type = response.css(".m-content #introduction .introContent .content ul li::text").extract()[0]
        Area = response.css(".m-content #introduction .introContent .content ul li::text").extract()[2]
        Orientation = response.css(".m-content #introduction .introContent .content ul li::text").extract()[6]
        Decoration =  response.css(".m-content #introduction .introContent .content ul li::text").extract()[8]
        Elevator = response.css(".m-content #introduction .introContent .content ul li::text").extract()[10]
        CompName = response.css(".overview .communityName a::text").extract()[0]
        Region1 = response.css(".overview .areaName span a::text").extract()[0]
        Region2 = response.css(".overview .areaName span a::text").extract()[1]
        Floor = response.css(".m-content #introduction .introContent .content ul li::text").extract()[1]
        BuildType = response.css(".m-content #introduction .introContent .content ul li::text").extract()[5]
        BuildStruc = response.css(".m-content #introduction .introContent .content ul li::text").extract()[7]
        Focus = response.css(".sellDetailHeader .title-wrapper .content .btnContainer .action span::text").extract()[0]

        lianjia_item['TotlePrice'] = TotlePrice
        lianjia_item['UnitPrice'] = UnitPrice
        lianjia_item['Type'] = Type
        lianjia_item['Area'] = Area
        lianjia_item['Orientation'] = Orientation
        lianjia_item['Decoration'] = Decoration
        lianjia_item['Elevator'] = Elevator
        lianjia_item['CompName'] = CompName
        lianjia_item['Region1'] = Region1
        lianjia_item['Region2'] = Region2
        lianjia_item['Floor'] = Floor
        lianjia_item['BuildType'] = BuildType
        lianjia_item['BuildStruc'] = BuildStruc
        lianjia_item['Focus'] = Focus

        yield lianjia_item