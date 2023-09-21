import scrapy
from NaverEconomy.items import NavereconomyItem
import requests
session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}


class MybotsSpider(scrapy.Spider):
    name = "mybots"
    allowed_domains = ["news.naver.com"]
    start_urls = ["https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101" ]

    def parse(self, response):
        titles = response.xpath("//*[@id='main_content']/div/div[2]/div[1]/ul/li/div[2]/a/text()").extract()
        authors = response.css(".sh_text_press::text").extract()
        previews = response.css(".sh_text_lede::text").extract()
        
        items = []
        for idx in range(len(titles)):
            item = NavereconomyItem()
            item['title'] = str(titles[idx]).strip()
            item['author'] =str( authors[idx]).strip()
            item['preview'] = str(previews[idx]).strip()
            items.append(item)
        return items
        
        
