from scrapy import Spider
from gofund.items import GofundItem
import pickle

with open('gofund/pages.pkl', 'rb') as f:
    adds = pickle.load(f)
    f.close()

class GoFundSpider(Spider):
    name = "GoFundSpider"
    allowed_urls = ['https://www.gofundme.com/']
    start_urls = adds

    def parse(self, response):

        title = response.xpath('//h1[@class="campaign-title"]/text()').extract()
        desc = response.xpath('//div[@id="story"]/div[3]/text()').extract()
        by = response.xpath('//div[@class="campaign-status text-small"]/span/text()').extract()[1]
        total = response.xpath('//h2[@class="goal"]/strong/text()').extract()[1]
        goal = response.xpath('//h2[@class="goal"]/span/text()').extract()[1]
        created = response.xpath('//div[@class="created-date"]/text()').extract()[1]
        try:
            shares = response.xpath('//strong[@class="js-share-count-text"]/text()').extract_first().strip()
        except:
            shares='0'
        location = response.xpath('//a[@class="icon-link location-name js-location-link"]/text()').extract()[1].strip()
        category = response.xpath('//a[@class="icon-link category-link-name js-category-link"]//span/text()').extract()[1]

        item = GofundItem()
        item['title'] = title
        item['desc'] = desc
        item['by'] = by
        item['total'] = total
        item['goal'] = goal
        item['created'] = created
        item['shares'] = shares
        item['location'] = location
        item['category'] = category

        yield item
