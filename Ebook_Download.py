from Ebook_Downloader_Scraper.Ebook_Downloader_Scraper.spiders.downloader import Downloader
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings

class EbookDownload:
    def get_download_link(self):
