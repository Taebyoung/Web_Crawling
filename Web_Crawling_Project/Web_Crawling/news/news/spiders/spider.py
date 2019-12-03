
import scrapy
from news.items import NewsItem

class Spider(scrapy.Spider):
    name = "News"
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
        }
    }
    
    def start_requests(self):
        url = "https://media.daum.net/"
        yield scrapy.Request(url, callback=self.parse)
        
    def parse(self, response):
        
        links = response.xpath('//*[@id="kakaoGnb"]/div/ul/li/a/@href').extract()
        links = list(map(response.urljoin, links))
        for link in links[1:7]:
            yield scrapy.Request(link, callback=self.page_content)
            
    def page_content(self, response):
        item = NewsItem()
        
        item["category"] = response.xpath(
                '//*[@id="cSub"]/div/div[2]/div[1]/h3/text()'
            ).extract()
        item["title1"] = response.xpath(
                '//*[@id="cSub"]/div/div[1]/div[1]/div/strong/a/text()'
            ).extract()
        item["link1"] = response.xpath(
                '//*[@id="cSub"]/div/div[1]/div[1]/div/strong/a/@href'
            ).extract()
        item["title2"] = response.xpath(
                '//*[@id="cSub"]/div/div[1]/ul[1]/li[1]/div[1]/strong/a/text()'
            ).extract()
        item["link2"] = response.xpath(
                '//*[@id="cSub"]/div/div[1]/ul[1]/li[1]/div[1]/strong/a/@href'
            ).extract()
        item["title3"] = response.xpath(
                '//*[@id="cSub"]/div/div[1]/ul[1]/li[2]/div[1]/strong/a/text()'
            ).extract()
        item["link3"] = response.xpath(
                '//*[@id="cSub"]/div/div[1]/ul[1]/li[2]/div[1]/strong/a/@href'
            ).extract()
        item["title4"] = response.xpath(
                '//*[@id="cSub"]/div/div[1]/ul[1]/li[3]/div[1]/strong/a/text()'
            ).extract()
        item["link4"] = response.xpath(
                '//*[@id="cSub"]/div/div[1]/ul[1]/li[3]/div[1]/strong/a/@href'
            ).extract()
        item["title5"] = response.xpath(
                '//*[@id="cSub"]/div/div[1]/ul[1]/li[4]/div[1]/strong/a/text()'
            ).extract()
        item["link5"] = response.xpath(
                '//*[@id="cSub"]/div/div[1]/ul[1]/li[4]/div[1]/strong/a/@href'
            ).extract()
        yield item
