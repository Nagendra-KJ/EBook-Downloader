import scrapy

from ..items import EbookItem

class EbookScraper(scrapy.Spider):
    name = "ebook"
    

    def __init__(self, book_name='', author_name='', **kwargs):
        self.start_urls = [f'https://b-ok.asia/s/{book_name}']
        self.author_name=author_name
        print(self.start_urls[0])
        super().__init__(**kwargs)


    def parse(self, response):

        items = EbookItem()

        list_counter = response.xpath("//div[contains(@class, 'exactMatch')]//div[contains(@class, 'authors') and not(contains(text(), ','))]\
                                        //ancestor::div[contains(@class, 'exactMatch')]//div[contains(@class, 'counter')]/text()").extract()
        list_counter = [int(x)-1 for x in list_counter]
        list_links = response.css("div.exactMatch").css("div.itemCoverWrapper a").xpath("@href").extract()
        list_authors = response.xpath("//div[contains(@class, 'exactMatch')]//div[contains(@class, 'authors') and not(contains(text(), ','))]/a/text()").extract()
        list_languages = response.css("div.exactMatch").css("div.property_language").css("div.property_value::text").extract()
        list_files = response.css("div.exactMatch").css("div.property__file").css("div.property_value::text").extract()

        list_links = [list_links[x] for x in list_counter]
        list_languages = [list_languages[x] for x in list_counter]
        list_files = [list_files[x] for x in list_counter]
        list_format = [(x.split(', '))[0] for x in list_files]
        list_size = [(x.split(', '))[1] for x in list_files]

        for [idx, link] in enumerate(list_links):
            items["link"] = list_links[idx]
            if (self.author_name != '' and list_authors[idx] != self.author_name) or list_languages[idx] != 'english' or list_format[idx] == 'PDF':
                continue
            items["author"] = list_authors[idx]
            items["language"] = list_languages[idx]
            items["format"] = list_format[idx]
            items["size"] = list_size[idx]
            yield items            

        


