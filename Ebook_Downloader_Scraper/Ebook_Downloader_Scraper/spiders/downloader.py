import scrapy
from selenium import webdriver-

class Downloader(scrapy.Spider):
    name = "downloader"

    def __init__(self, book_link='', **kwargs): # Set Search url to b-ok.asia/s/book_name
        self.start_urls = [f'https://b-ok.asia/4550503/eedf40']
        self.driver = webdriver.Firefox()
        super().__init__(**kwargs)

    def parse(self, response):
        print("Inside this function")
        yield