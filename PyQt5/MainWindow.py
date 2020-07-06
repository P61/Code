# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(713, 629)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(100, 540, 93, 28))
        self.openButton.setObjectName("openButton")

        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(330, 540, 93, 28))
        self.closeButton.setObjectName("closeButton")

        self.catchButton = QtWidgets.QPushButton(self.centralwidget)
        self.catchButton.setGeometry(QtCore.QRect(550, 540, 93, 28))
        self.catchButton.setObjectName("catchButton")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 640, 480))
        self.widget.setObjectName("widget")
        self.img_label = QtWidgets.QLabel(self.widget)
        self.img_label.setGeometry(QtCore.QRect(0, 0, 640, 480))# 截取
        self.img_label.setObjectName("img_label")
        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)# 窗体菜单栏
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 0))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # 底部水平条，作为状态栏（QstatusBar），用于显示永久或临时的状态信息
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "演示"))
        self.openButton.setText(_translate("MainWindow", "打开摄像头"))
        self.closeButton.setText(_translate("MainWindow", "关闭"))
        self.catchButton.setText(_translate("MainWindow", "抓取一帧"))
        self.img_label.setText(_translate("MainWindow", "                                                视频播放区域"))
