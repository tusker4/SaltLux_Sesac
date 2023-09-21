# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NavernewsItem(scrapy.Item):
    # 제목, 부제목, 출처
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    preview = scrapy.Field()
    
    
    pass
