# important libraries
import scrapy
from scrapy.crawler import CrawlerProcess
import csv


# inheriting from the scrapy.Spider class
class MySpider(scrapy.Spider):
    name = "news_spider"  # name for our web scrawler

    def start_requests(self):
        urls = ['https://www.cnbc.com/finance/']   #target url for scraping
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        # user-agent argument is used so that website cannot classify the request as scraping and block it
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        headlines = response.xpath('//a[@class="Card-title"]/text()').extract()   #change it as per your use

        for headline in headlines:
            print(headline)
            with open('financialnews.csv', 'a', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([headline])


process = CrawlerProcess()
process.crawl(MySpider)
process.start()
