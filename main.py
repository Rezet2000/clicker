import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from src.client import Client

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Sets screen interface parameters
        self.setWindowTitle('Clicker')
        self.setGeometry(100, 100, 300, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QtGui.QIcon('src/assets/logo.png'))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Events recorder client
        self.client = Client(self)

        def create_button(button, method):
            button.clicked.connect(method)
            self.layout.addWidget(button)

        # Adds 'Start recording' button to screen
        create_button(QPushButton('Start recording', self), self.client.record_events)
        # Adds 'Show/display clicks' button to screen
        create_button(QPushButton('Show/hide clicks', self), self.client.show_events)
        # Adds 'Run events' button to screen
        create_button(QPushButton('Run events', self), self.client.run_events)
        # Loads events
        create_button(QPushButton('Load events', self), self.client.load_events)
        # Saves events
        create_button(QPushButton('Save events', self), self.client.save_events)

    # Minimizes window
    def iconify(self):
        self.showMinimized()

    # Maximize window
    def deiconify(self):
        self.showNormal()

def start_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    start_app()