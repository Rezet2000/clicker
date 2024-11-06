from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class ScreenDrawer(QWidget):
    def __init__(self, points):
        super().__init__()
        self.points = points
        self.setGeometry(0, 0, QApplication.desktop().screenGeometry().width(),
                         QApplication.desktop().screenGeometry().height())
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def paintEvent(self, event):
            painter = QPainter(self)
            pen = QPen(QColor(70, 255, 51))
            pen.setWidth(7)
            painter.setPen(pen)
            for index, point in enumerate(self.points):
                x, y = point
                painter.drawText(x + 8, y, f'{index + 1}')
                painter.drawPoint(*point)
    
    def keyPressEvent(self, event):
        if event.key():
            self.close()
