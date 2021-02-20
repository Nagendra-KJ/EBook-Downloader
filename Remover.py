import os
import pathlib

class Remover:
    def remove(self):
        os.chdir(os.path.join(pathlib.Path().absolute(),'downloads'))
        files = os.listdir()
        for f in files:
            os.remove(f)

