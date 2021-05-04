from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os.path
import pathlib
import time

class Downloader():
    def __init__(self, download_path):
        self.download_path = download_path

    def setup(self, start_urls):
        download_dir = self.download_path
        self.start_urls = start_urls
        chromeOptions = webdriver.ChromeOptions()
        prefs = {'download.default_directory':download_dir}
        chromeOptions.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chromeOptions)
        for url in start_urls:
            status = self.download(url)
            if status == "Limit Reached" or status=="Success":
                break
            if status == "Fail":
                continue
        self.driver.close()
        self.driver.quit()
        return status
                
    def download(self, url):
        self.driver.get(url)
        dlButton = self.driver.find_element_by_class_name('dlButton')
        failed_check = None
        try:
            dlButton.click()
            time.sleep(20)
            failed_check = None
            failed_check = self.driver.find_element_by_class_name('recommended-plan-ribbon')
            if(failed_check != None):
                return "Limit Reached"
            else:
                return "Success"
        except Exception as e:
            if failed_check == None:
                return "Success"
            else:
                print(e)
                return "Fail"
