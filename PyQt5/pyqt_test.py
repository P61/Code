#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Py40 PyQt5 tutorial 

This program creates a quit
button. When we press the button,
the application terminates. 

author: Jan Bodnar
website: py40.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QDesktopWidget
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        opbtn = QPushButton('打开摄像头', self)
        opbtn.clicked.connect(QCoreApplication.instance().quit)
        opbtn.resize(opbtn.sizeHint())
        opbtn.move(80, 500)

        closebtn = QPushButton('关闭', self)
        # closebtn.clicked.connect(QCoreApplication.instance().quit)
        closebtn.resize(closebtn.sizeHint())
        closebtn.move(350, 500) 
        
        catbtn = QPushButton('抓取一帧', self)
        # closebtn.clicked.connect(QCoreApplication.instance().quit)
        catbtn.resize(catbtn.sizeHint())
        catbtn.move(650, 500) 

        # self.setGeometry(550, 200, 800, 600 )
        # self.setWindowTitle('演示')    
        # self.show()
        self.resize(800, 600)
        self.center()
        
        self.setWindowTitle('演示')    
        self.show()
    
    #控制窗口显示在屏幕中心的方法    
    def center(self):
        
        #获得窗口
        qr = self.frameGeometry()
        #获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        #显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())




if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())