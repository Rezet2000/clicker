import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QTimer

class ScreenDrawer(QWidget):
    def __init__(self, points):
        super().__init__()
        self.points = points
        self.setGeometry(0, 0, QApplication.desktop().screenGeometry().width(),
                         QApplication.desktop().screenGeometry().height())
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def paintEvent(self, event):
            painter = QPainter(self)
            pen = QPen(QColor(255, 0, 0))
            pen.setWidth(5)
            painter.setPen(pen)
            for point in self.points:
                painter.drawPoint(*point)
    
    def keyPressEvent(self, event):
        if event.key():
            self.close()
