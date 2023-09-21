import scrapy
from navernews.items import NavernewsItem


class MybotsSpider(scrapy.Spider):
    name = "mybots"
    allowed_domains = ["news.naver.com"]
    start_urls = ["http://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=732"]
    

    def parse(self, response):
        # main_content가 2개만 있기 때문에 id=main_content는 1개 값이
        # text() 는 바디값
        titles = response.xpath("//*[@id='main_content']/div[2]/ul/li/dl/dt[2]/a/text()").extract()
        # stylesheet  인경우  .추가 /  ::text/  extract
        authors = response.css(".writing::text").extract()
        previews = response.css(".lede::text").extract()
        
        items = []
        for idx in range(len(titles)):
            item = NavernewsItem()
            item['title'] = str(titles[idx]).strip()
            item['author'] =str( authors[idx]).strip()
            item['preview'] = str(previews[idx]).strip()
            items.append(item)
        return items
        
        
