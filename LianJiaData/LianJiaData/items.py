# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiadataItem(scrapy.Item):

    TotlePrice = scrapy.Field()   #总价
    UnitPrice = scrapy.Field()  #单价
    Type = scrapy.Field()  #户型
    Area = scrapy.Field()   #面积
    Orientation = scrapy.Field()   #朝向
    Decoration = scrapy.Field()   #装修状况
    Elevator = scrapy.Field()    #有无电梯
    CompName = scrapy.Field()  #小区名称
    Region1 = scrapy.Field()  #区域
    Region2 = scrapy.Field()  # 区域
    Floor = scrapy.Field()  #楼层详细
    BuildType = scrapy.Field()  #建筑类型
    BuildStruc = scrapy.Field()  #建筑结构
    Focus = scrapy.Field()  #关注人数
    # Visits = scrapy.Field() #看房次数
    Pubdate = scrapy.Field()  #发布时间
    Remarks = scrapy.Field()  #备注