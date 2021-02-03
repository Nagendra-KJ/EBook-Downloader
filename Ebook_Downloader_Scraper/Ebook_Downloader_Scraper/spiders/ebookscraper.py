import scrapy

from ..items import EbookItem

class EbookScraper(scrapy.Spider):
    name = "ebook"
    

    def __init__(self, book_name='', author_name='', **kwargs): # Set Search url to b-ok.asia/s/book_name
        self.start_urls = [f'https://b-ok.asia/s/{book_name}']
        self.author_name=author_name
        print(self.start_urls[0])
        super().__init__(**kwargs)


    def parse(self, response):

        items = EbookItem() # Create an ebook item

        #Xpath for the counter parameter. links, author, languages, files

        list_counter = response.xpath("//div[contains(@class, 'exactMatch')]//div[contains(@class, 'counter')]/text()").extract()
        list_counter = [int(x)-1 for x in list_counter]
        list_links = response.css("div.exactMatch").css("div.itemCoverWrapper a").xpath("@href").extract()
        list_authors_divs = response.xpath("//div[contains(@class, 'exactMatch')]//div[contains(@class, 'authors')]").extract()
        list_languages = response.css("div.exactMatch").css("div.property_language").css("div.property_value::text").extract()
        list_files = response.css("div.exactMatch").css("div.property__file").css("div.property_value::text").extract()       

        #Extract the author names as a list from each authors div
        authors=[]
        for author_div in list_authors_divs:
            response = scrapy.http.HtmlResponse(url="my url", body=author_div, encoding="utf-8")
            temp_list = response.xpath("//div[contains(@class, 'authors')]/a/text()").extract() # Get a temporary list of authors
            author_set= set()
            for name in temp_list:
                author_set = author_set.union(set(name.lower().split(' '))) # Append each word in the list to a set
            authors.append(author_set) # Append the entire set to the list of authors

        #Keep only those files that are present in list counter

        list_links = [list_links[x] for x in list_counter]
        list_languages = [list_languages[x] for x in list_counter]
        list_files = [list_files[x] for x in list_counter]
        list_format = [(x.split(', '))[0] for x in list_files]
        list_size = [(x.split(', '))[1] for x in list_files]

        # Add it to the list with Item container and skip if they are in PDF, not in English or do not match the author names

        for [idx, link] in enumerate(list_links):
            items["link"] = list_links[idx]
            if (self.author_name != set() and len(self.author_name.intersection(authors[idx])) <= 0) or list_languages[idx] != 'english' or list_format[idx] == 'PDF':
                continue
            items["author"] = authors[idx]
            items["language"] = list_languages[idx]
            items["format"] = list_format[idx]
            items["size"] = list_size[idx]
            yield items            

        


