from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# 룰을 지정하고 어떤 곳에서 가져올것인지

class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com"]
    
    rules=[
        Rule(LinkExtractor(allow="catalogue/category")), 
        Rule(LinkExtractor(allow="catalogue", deny="category"), 
                           callback ="parse_item")
    ]
    
    def parse_item(self, response):
        yield{
            "title" : response.css (".product_main h1::text").get(),
            "price" :  response.css(".price_color::text").get(),
            "availability" : response.css(".availability::text")[1].get()
        }
        # yield 를 쓰면 다 만들어져야지만 전달된다. 한 묶음씩?
        #content_inner > article > div.row > div.col-sm-6.product_main > h1
        
    