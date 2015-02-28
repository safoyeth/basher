#! /usr/bin/python
# -*- coding: utf-8 -*-
 
import re
import sys
import random
import requests
try:
    from PyQt4.QtGui import *
except:
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
 
class Main(QMainWindow):
    '''
    class Main - создание окна приложения.
    '''
    def __init__(self):
        super(Main, self).__init__()
 
        self.index = 0
        self.statuz = None
        self.text = QTextEdit(self)
        self.text.setReadOnly(True)
        self.text.setStyleSheet("font-size: 14px; "
                                "text-align: left;"
                                "font-family: Verdana;")
        self.toolbar = QToolBar(u"Действия", self)
        self.getRandomButton = QPushButton(u"Случайная [F5]", self)
        self.getNewButton = QPushButton(u"Свежачок! [F4]", self)
        self.getNewButton.clicked.connect(self.getNew)
        self.getRandomButton.clicked.connect(self.getRandom)
        self.status = QStatusBar(self)
        self.progress = QProgressBar(self)
        self.progress.setRange(0, 10)
        self.countLabel = QLabel(u"", self)
        self.toolbar.addWidget(self.getNewButton)
        self.toolbar.addWidget(self.getRandomButton)
        self.toolbar.addWidget(self.countLabel)
        self.status.addPermanentWidget(self.progress)
        self.addToolBar(self.toolbar)
        self.setStatusBar(self.status)
        self.setCentralWidget(self.text)
 
    def getRandom(self):
        '''
        getRandom() - получает случайную цитату с сайта.
        '''
        self.progress.setValue(2)
        self.text.append("<span style='color:green';>BASH.IM {RANDOM}</span></br>")
        self.progress.setValue(4)
        self.text.append(re.findall('<div class="text">.*</div>', requests.get("http://bash.im/random").text)[random.randint(0, 10)])
        self.progress.setValue(6)
        self.text.append("<br/>")
        self.progress.setValue(8)
        self.index += 1
        self.countLabel.setText(u"     Цитат получено: %s"%str(self.index))
        self.progress.setValue(10)
 
    def getNew(self):
        '''
        getNew() - получает новые цитаты.
        '''
        if not self.statuz:
            self.progress.setValue(1)
            dates = re.findall('<span class="date">.*</span>', requests.get("http://bash.im").text)
            for each, date in enumerate(dates):
                self.progress.setValue(2)
                if dates[each][19:29] == QDate().currentDate().toString("yyyy-MM-dd"):
                    self.progress.setValue(3)
                    self.text.append(u"<span style='color:green';>BASH.IM {Свежачок!}</span></br>")
                    self.progress.setValue(4)
                    self.text.append(re.findall('<div class="text">.*</div>', requests.get("http://bash.im").text)[each])
                    self.progress.setValue(5)
                    self.text.append("<br/>")
                    self.progress.setValue(6)
                    self.index += 1
                    self.progress.setValue(7)
                    self.countLabel.setText(u"     Цитат получено: %s"%str(self.index))
                    self.progress.setValue(8)
            else:
                QMessageBox.information(self, u"Цитатник рунета", u"Свежачка больше пока нет...")
                self.progress.setValue(10)
            self.statuz = True
            self.progress.setValue(10)
        else:
            QMessageBox.information(self, u"Цитатник рунета", u"Свежачок уже был получен!", QMessageBox.Ok)
            self.progress.setValue(10)
 
    def keyPressEvent(self, event):
        '''
        keyPressEvent() - привязывает F4 к получению новых цитат, а F5 к получению случайной.
        '''
        if event.key() == Qt.Key_F5:
            self.getRandom()
        if event.key() == Qt.Key_F4:
            self.getNew()
 
def main():
    '''
    main() - главный цикл приложения.
    '''
    application = QApplication(sys.argv)
    window = Main()
    window.setWindowIcon(QIcon("net.ico"))
    application.setStyle("plastique")
    window.setWindowTitle(u"Цитатник рунета")
    window.showMaximized()
    sys.exit(application.exec_())
 
if __name__ == "__main__":
    main()
