# 3. Використовуючи Scrapy, заходите на "https://chrome.google.com/webstore/sitemap", переходите на кожен лінк з тегів <loc>, з кожного лінка берете посилання на 
# сторінки екстеншенів, парсите їх і зберігаєте в CSV файл ID, назву та короткий опис кожного екстеншена (пошукайте уважно де його можна взяти)
from task_3.items import ExtensionItem

import scrapy
from bs4 import BeautifulSoup


class ExtensionsSpider(scrapy.Spider):
    name = 'extensions'

    def start_requests(self):
        site_map = 'https://chrome.google.com/webstore/sitemap'
        yield scrapy.Request(url=site_map, callback=self.parse_sitemap)
    
    def parse_sitemap(self, response):
        soup = BeautifulSoup(response.body, 'xml')
        
        for loc in soup.select('sitemap > loc'):
            yield scrapy.Request(url=loc.text, callback=self.parse_shard)

    def parse_shard(self, response):
        soup = BeautifulSoup(response.body, 'xml')

        for url in soup.find_all('loc'):
            yield scrapy.Request(url=url.text, callback=self.parse_extension_page)

    def parse_extension_page(self, response):
        name = response.css('[property="og:title"]::attr(content)').get()
        description = response.css('[property="og:description"]::attr(content)').get()
        extension = ExtensionItem(name=name, description=description)

        yield extension
