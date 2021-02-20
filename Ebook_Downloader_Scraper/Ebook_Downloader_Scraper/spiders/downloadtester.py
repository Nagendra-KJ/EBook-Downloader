from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os.path
import pathlib
import time

class Downloader():
    def setup(self, start_urls):
        download_dir = os.path.join(pathlib.Path().absolute(),'downloads\\')
        print(download_dir)
        self.start_urls = start_urls
        chromeOptions = webdriver.ChromeOptions()
        prefs = {'download.default_directory':download_dir}
        chromeOptions.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chromeOptions)
        for url in start_urls:
            status = self.download('https://filesamples.com/formats/mobi')
            if status == "Limit Reached" or status=="Success":
                break
            if status == "Fail":
                continue
        self.driver.close()
        self.driver.quit()
        return status
                

    def download(self, url):
        self.driver.get(url)
        dlButton = self.driver.find_element_by_class_name('btn-primary')
        try:
            time.sleep(5)
            dlButton.click()
            #failed_check = self.driver.find_element_by_class_name('recommended-plan-ribbon')
            time.sleep(10)
            print("Failed due to excess file downloads")
            return "Limit Reached"
        except Exception as e:
            print(e)
            return "Fail"

Downloader().setup(['summat'])