# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Ebook Downloader.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Book_Link_Scraper import BookLinkScraper
from Download_Link_Scraper import DownloadLinkScraper
from Prioritizer import Prioritizer
from Converter import Converter
from Emailer import Emailer
import sys
import re

class Ui_MainWindow(object): # UI defined with help of QT Designer
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bookNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.bookNameLabel.setGeometry(QtCore.QRect(40, 70, 71, 31))
        self.bookNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bookNameLabel.setObjectName("bookNameLabel")
        self.bookNameTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.bookNameTextbox.setGeometry(QtCore.QRect(130, 70, 651, 22))
        self.bookNameTextbox.setObjectName("bookNameTextbox")
        self.authorNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.authorNameLabel.setGeometry(QtCore.QRect(30, 120, 81, 41))
        self.authorNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.authorNameLabel.setObjectName("authorNameLabel")
        self.authorNameTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.authorNameTextbox.setGeometry(QtCore.QRect(130, 120, 651, 22))
        self.authorNameTextbox.setObjectName("authorNameTextbox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 230, 121, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fetch)
        self.error_dialog = QtWidgets.QMessageBox()
        self.error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
        self.error_dialog.setWindowTitle("Error")
        self.msg_dialog = QtWidgets.QMessageBox()
        self.msg_dialog.setIcon(QtWidgets.QMessageBox.Information)
        self.msg_dialog.setWindowTitle("Information")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow): # Auto generated code
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EBook Downloader"))
        self.bookNameLabel.setText(_translate("MainWindow", "Book Name"))
        self.authorNameLabel.setText(_translate("MainWindow", "Author Name"))
        self.pushButton.setText(_translate("MainWindow", "Fetch"))

    
    def fetch(self): # Get bookname and author name and send it to the scrapy module for searching and scraping
        bookName = self.bookNameTextbox.text()
        authorName = self.authorNameTextbox.text()
        authorName = re.split(';|,| ',authorName) #Get the different words in the author name list
        authorName = [x.lower() for x in authorName if x] # Convert it to lower case and filter out empty strings
        authorName = set(authorName) # Add to set
        if bookName == '':
            self.show_error('Please provide atleast one book name')
        else:
            linkScraper = BookLinkScraper()
            linkScraper.begin(bookName, authorName)
            if linkScraper.get_list_length() == 0:
                self.show_error("No matches found")
                return
            prioritizer = Prioritizer()
            prioritizer.prioritize()

            downloader = DownloadLinkScraper()
            status = downloader.begin()
            #status = "Success"
            if status == "Limit Reached":
                self.show_error('Download cannot be completed due to limits')
            elif status == "Success":
                Converter().convert(bookName)
                Emailer().send(bookName)
                self.show_message("Process Complete")

    
    def show_error(self, msg): # show an error message on the error dialog
        self.error_dialog.setText(msg)
        self.error_dialog.exec_()
    
    def show_message(self, msg):
        self.msg_dialog.setText(msg)
        self.msg_dialog.exec_()

if __name__ == "__main__": # run the app
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
