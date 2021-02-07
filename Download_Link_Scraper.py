import json

from Ebook_Downloader_Scraper.Ebook_Downloader_Scraper.spiders.downloader import Downloader

class DownloadLinkScraper:
    def begin(self):
        with open('sorted_json_file.json') as f:
            sorted_array = json.load(f)
            sorted_array = [x['link'] for x in sorted_array]
            print(sorted_array)
        book_link=[f'https://b-ok.asia{x}' for x in sorted_array]
        downloader = Downloader()
        status = downloader.setup(book_link)
        return status
        
