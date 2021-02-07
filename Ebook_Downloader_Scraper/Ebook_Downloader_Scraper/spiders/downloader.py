from selenium import webdriver
import os.path
import pathlib

class Downloader():
    def setup(self, start_urls):
        download_dir = os.path.join(pathlib.Path().absolute(),'downloads')
        self.start_urls = start_urls
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2) # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.dir', download_dir)
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/epub+zip, application/x-mobipocket-ebook ')
        profile.set_preference("pdfjs.disabled", True)
        self.driver = webdriver.Firefox(profile)
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
        try:
            dlButton.click()
            try:
                failed_check = self.driver.find_element_by_class_name('recommended-plan-ribbon')
                print("Failed due to excess file downloads")
                #self.driver.close()
                return "Limit Reached"
            except:
                os.chdir(download_dir)
                downloading = True
                while downloading:
                    for fname in os.listdir('.'):
                        if fname.endswith('.part'):
                            downloading = True
                        else:
                            downloading = False
                return "Success"
        except Exception as e:
            return "Fail"
