import sys
import MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QImage, QPixmap
import cv2


class MainCode(QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        MainWindow.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.openButton.clicked.connect(self.open_video)
        self.closeButton.clicked.connect(self.close_video)
        self.catchButton.clicked.connect(self.get_img)
        self.open_flag = False
        # self.video_stream = cv2.VideoCapture('F:/电影/乔纳森.mkv')
        self.video_stream = cv2.VideoCapture(0)
        self.painter = QPainter(self)
        self.count = 0

    def open_video(self):
        if self.open_flag==False:
            self.open_flag = True
        # self.open_flag = bool(1 - self.open_flag)

    def close_video(self):
         if self.open_flag:
            self.open_flag = False

        # self.open_flag = bool(1 - self.open_flag)

    def on_video(self):
        """
            打开关闭可以使用一个按钮
        """
        if self.open_flag:
            self.pushButton.setText('打开摄像头')
        else:
            self.pushButton.setText('关闭')
        self.open_flag = bool(1 - self.open_flag)  #False=0/True=1

    def paintEvent(self, a0: QtGui.QPaintEvent):

        if self.open_flag:
            ret, frame = self.video_stream.read()
            frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)# 压缩
            # interpolation 是指定插值的方式，图像缩放之后，肯定像素要进行重新计算的，
            # 就靠这个参数来指定重新计算像素的方式
            # 使用像素面积关系进行重采样。这可能是首选的图像抽取方法，因为它可以提供无波纹的结果。
            # 但是，当图像缩放时，它类似于INTER_NEAREST方法。

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # 颜色转换

            # cv2.imshow('test',frame)
            # cv2.waitKey(10)
            self.Qframe = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QImage.Format_RGB888)
            # frame.shape[0]图像的垂直尺寸（高度），[1]图像的水平尺寸（宽度），[2]图像的通道数。
            # frame.shape[1] * 3 每行的字节 
            self.img_label.setPixmap(QPixmap.fromImage(self.Qframe))
            self.update()
        else:
            # print('11')
            pass
            # self.video_stream.release()
            # cv2.destroyAllWindows()

    def get_img(self):
        ret, frame = self.video_stream.read()
        cv2.imwrite("frame%d.jpg" %self.count, frame)
        self.count += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainCode()
    md.show()
    sys.exit(app.exec_())

