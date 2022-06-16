import scrapy


class GdpSpider(scrapy.Spider):
    name = 'gdp'
    allowed_domains = ['data.stats.gov.cn']
    start_urls = ['https://data.stats.gov.cn/search.htm?s=GDP']

    def parse(self, response):
        pass
