import json

from twisted.internet import reactor, defer
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from multiprocessing import Process, Queue
from Ebook_Downloader_Scraper.Ebook_Downloader_Scraper.spiders.ebookscraper import EbookScraper

class BookLinkScraper:
    def run(self, q, bookName, authorName): # Create a custom crawler runner. Multiprocessing is used so that multiple books can be fetched without woorries
        try:
            custom_settings={
                'FEEDS':{
                    'result.json':{'format':'json',
                                    'overwrite':True}
                }
            }
            runner = CrawlerRunner(custom_settings)
            deferred = runner.crawl(EbookScraper, author_name=authorName, book_name=bookName)
            deferred.addBoth(lambda _: reactor.stop())
            reactor.run()
            q.put(None)
        except Exception as e:
            q.put(e)

    def begin(self,bookName, authorName):
        q = Queue()
        p = Process(target=self.run, args=(q,bookName,authorName))
        p.start()
        result = q.get()
        p.join() # Wait until one book is fetched until the process is ended for next book
        if result is not None:
            raise result

    def get_list_length(self): # Find list of links, if it is none, put empty list
        with open("result.json","r") as json_file:
            try:
                list_of_links = json.load(json_file)
            except Exception as e:
                list_of_links = []
        return len(list_of_links)

