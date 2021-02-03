import json

from twisted.internet import reactor, defer
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from multiprocessing import Process, Queue
from Ebook_Downloader_Scraper.Ebook_Downloader_Scraper.spiders.ebookscraper import EbookScraper

class BookLinkScraper:
    def run(self, q, bookName, authorName):
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
        print('Fetching ', bookName)
        q = Queue()
        p = Process(target=self.run, args=(q,bookName,authorName))
        p.start()
        result = q.get()
        p.join() 
        if result is not None:
            raise result

    def get_list_length(self):
        with open("result.json","r") as json_file:
            try:
                data = json.load(json_file)
            except Exception as e:
                data = []
        return len(data)

