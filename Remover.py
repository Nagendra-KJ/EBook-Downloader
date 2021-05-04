import os
import pathlib

class Remover:
    def remove(self, download_dir):
        path = os.getcwd()
        os.chdir(download_dir)
        files = os.listdir()
        for f in files:
            os.remove(f)
        os.rmdir(download_dir)
