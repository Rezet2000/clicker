import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from src.client import Client

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple event recorder')
        self.setGeometry(100, 100, 300, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.client = Client(self)

        self.record_button = QPushButton('Start recording', self)
        self.record_button.clicked.connect(self.client.record_events)
        self.layout.addWidget(self.record_button)

        self.show_events_button = QPushButton('Display clicks', self)
        self.show_events_button.clicked.connect(self.client.show_events)
        self.layout.addWidget(self.show_events_button)

        self.run_events_button = QPushButton('Run events', self)
        self.run_events_button.clicked.connect(self.client.run_events)
        self.layout.addWidget(self.run_events_button)

    def iconify(self):
        self.showMinimized()

    def deiconify(self):
        self.showNormal()

def interface():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    interface()