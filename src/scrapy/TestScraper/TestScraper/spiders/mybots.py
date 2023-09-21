import scrapy
from TestScraper.items import TestscraperItem


class MybotsSpider(scrapy.Spider):
    name = "mybots"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        titles = response.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/h3/a/@title').extract()
        # //*[@id="default"]/div/div/div/div/section/div[2]/ol/li[2]/article/h3/a
        # prices = response.css(".price_color::text").extract()
        # default > div > div > div > div > section > div:nth-child(2) > ol > li:nth-child(2) > article > div.product_price > p.price_color
        
        # 방법1.
        # items = []
        # for idx in range(len(titles)):
        #     item = TestscraperItem()
        #     item['title'] = str(titles[idx]).strip()
        #     item['price'] = str(prices[idx]).strip()
        #     items.append(item)
        # print(items)
        # return items

        #방법2.
        item = TestscraperItem()
        count = 0
        for idx in range(len(titles)):
            item['title'] = response.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/h3/a/@title').get()
            item['price'] = response.css(".price_color::text").get()
            # 하나만 가져오니까 get - 페이지의 가장 앞에 있는 책의 정보만 가져온다.
        yield item
        
        next_page =   response.css('.next a::attr(href)').extract_first()
        if next_page :
            yield response.follow(next_page, callback=self.parse)
