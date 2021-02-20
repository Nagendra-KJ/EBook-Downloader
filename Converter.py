import os
import subprocess
import pathlib

class Converter:
    def convert(self, book_name='ebook'):
        print('Trying to convert now')
        download_dir = os.path.join(pathlib.Path().absolute(),'downloads')
        epubExt = r"*.epub"
        fileList = list(pathlib.Path(download_dir).glob(epubExt))
        fileList = [str(x) for x in fileList]
        num = len(fileList)
        currDir = os.getcwd()
        os.chdir(download_dir)
        for fname in fileList:
            command = f'ebook-convert "{fname}" "{book_name}.mobi"'
            subprocess.call(command)
        os.chdir(currDir)
        
        if num == 0:
            mobiExt = r"*.mobi"
            fileList = list(pathlib.Path(download_dir).glob(mobiExt))
            fileList = [str(x) for x in fileList]
            os.chdir(download_dir)
            for fname in fileList:
                bookname = f'{book_name}.mobi'
                os.rename(fname, bookname)
            os.chdir(currDir)