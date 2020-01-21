from PyQt5 import QtCore, QtGui, QtWidgets
import pafy
import requests
import os
from PIL import Image

directory = os.getcwd()
class Ui_Form(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(328, 569)
        self.lineEdit_UrlGrabber = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_UrlGrabber.setGeometry(QtCore.QRect(10, 240, 271, 31))
        self.lineEdit_UrlGrabber.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "color: rgb(0, 0, 255);\n"
                                               "font: 75 italic 11pt \"Sitka\";")
        self.lineEdit_UrlGrabber.setObjectName("lineEdit_UrlGrabber")
        self.pushButton_DownloadButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton_DownloadButton.setGeometry(
            QtCore.QRect(100, 530, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_DownloadButton.setFont(font)
        self.pushButton_DownloadButton.setCursor(
            QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_DownloadButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                     "background-color: rgb(255, 0, 17);")
        self.pushButton_DownloadButton.setObjectName(
            "pushButton_DownloadButton")
        self.pushButton_DownloadButton.clicked.connect(self.download)
        self.label_notdecided = QtWidgets.QLabel(MainWindow)
        self.label_notdecided.setGeometry(QtCore.QRect(260, 510, 51, 21))
        self.label_notdecided.setObjectName("label_notdecided")
        self.pushButton_search = QtWidgets.QPushButton(MainWindow)
        self.pushButton_search.setGeometry(QtCore.QRect(290, 240, 31, 31))
        self.pushButton_search.clicked.connect(self.fetchVideo)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_search.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{directory}/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search.setIcon(icon)
        self.pushButton_search.setObjectName("pushButton_search")
        self.label_image = QtWidgets.QPushButton(MainWindow)
        self.label_image.setGeometry(QtCore.QRect(20, 50, 291, 141))
        self.label_image.setObjectName("")
        self.label_image.setIcon(QtGui.QIcon(f'{directory}/logo.png'))
        self.label_image.setIconSize(QtCore.QSize(self.label_image.width(), self.label_image.height()))
        self.label_VideoTitle = QtWidgets.QLabel(MainWindow)
        self.label_VideoTitle.setGeometry(QtCore.QRect(10, 490, 241, 41))
        self.label_VideoTitle.setObjectName("label_VideoTitle")
        self.label_Url_header = QtWidgets.QLabel(MainWindow)
        self.label_Url_header.setGeometry(QtCore.QRect(10, 200, 221, 21))
        self.label_Url_header.setObjectName("label_Url_header")
        self.label_ViewCount = QtWidgets.QLabel(MainWindow)
        self.label_ViewCount.setGeometry(QtCore.QRect(260, 490, 51, 21))
        self.label_ViewCount.setObjectName("label_ViewCount")
        self.label_header_name = QtWidgets.QLabel(MainWindow)
        self.label_header_name.setGeometry(QtCore.QRect(10, 0, 301, 41))
        self.label_header_name.setStyleSheet(
            "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_header_name.setObjectName("label_header_name")
        self.choice = QtWidgets.QComboBox(MainWindow)
        self.choice.setGeometry(QtCore.QRect(200, 280, 121, 22))
        self.choice.setObjectName("choice")
        self.choice.addItem("Video")
        self.choice.addItem("Music")
        self.choice.activated[str].connect(self.process_choice)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(10, 280, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_thumbnail = QtWidgets.QPushButton(MainWindow)
        self.label_thumbnail.setGeometry(QtCore.QRect(10, 310, 301, 181))
        self.label_thumbnail.setText("")
        self.label_thumbnail.setObjectName("label_thumbnail")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_DownloadButton.setText(_translate("MainWindow", "Download"))
        self.label_notdecided.setText(_translate("MainWindow", "Duration"))
        self.label_image.setText(_translate("MainWindow", ""))
        self.label_VideoTitle.setText(_translate("MainWindow", "Video Title"))
        self.label_Url_header.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#ff0004;\">Enter the URL below</span></p></body></html>"))
        self.label_ViewCount.setText(_translate("MainWindow", "Views"))
        self.label_header_name.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">YouTube Video Downloader</span></p></body></html>"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0004;\">Video Details</span></p></body></html>"))
    def process_choice(self,text):
        self.data = text
    def fetchVideo(self):
        if self.lineEdit_UrlGrabber.text() != "":
            self.video = pafy.new(self.lineEdit_UrlGrabber.text())
            ima = Image.open(requests.get(self.video.thumb, stream=True).raw)
        #     ima.resize((self.label_thumbnail.width()-1, self.label_thumbnail.height()-2))
            ima.save("temp.png")
            self.label_thumbnail.setIcon(QtGui.QIcon('temp.png'))
            self.label_thumbnail.setIconSize(QtCore.QSize(
                self.label_thumbnail.width(), self.label_thumbnail.height()))
            self.label_VideoTitle.setText(str(self.video.title))
            self.label_ViewCount.setText(str(self.video.viewcount))
            self.label_notdecided.setText(str(self.video.duration))
            os.remove("temp.png")
        else:
            self.mes = QtWidgets.QMessageBox()
            self.mes.setIcon(self.mes.Warning)
            self.mes.setInformativeText("Please enter a URL")
            self.mes.show()
        
    def download(self):
        if self.lineEdit_UrlGrabber.text() != "":
            if self.data == "Video":
                best = self.video.getbest()
                best.download()
            elif self.data == "Music":
                best = self.video.getbestaudio()
                best.download()
            else:
                pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
