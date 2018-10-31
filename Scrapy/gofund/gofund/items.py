import scrapy

class GofundItem(scrapy.Item):
    #fields
    title = scrapy.Field()
    desc = scrapy.Field()
    by = scrapy.Field()
    total = scrapy.Field()
    goal = scrapy.Field()
    created = scrapy.Field()
    shares = scrapy.Field()
    location = scrapy.Field()
    category = scrapy.Field()

 

