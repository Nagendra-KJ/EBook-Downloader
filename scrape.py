
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from Ebook_Downloader_UI import Ui_MainWindow


    
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    print("Hello there, General Kenobi")
    sys.exit(app.exec_())

