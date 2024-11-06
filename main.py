import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from src.client import Client

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Sets screen interface parameters
        self.setWindowTitle('Event recorder')
        self.setGeometry(100, 100, 300, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Events recorder client
        self.client = Client(self)

        # Adds 'start recording' button to screen
        self.record_button = QPushButton('Start recording', self)
        self.record_button.clicked.connect(self.client.record_events)
        self.layout.addWidget(self.record_button)

        # Adds 'Show/display clicks' button to screen
        self.show_events_button = QPushButton('Show/hide clicks', self)
        self.show_events_button.clicked.connect(self.client.show_events)
        self.layout.addWidget(self.show_events_button)

        # Adds 'Run events' button to screen
        self.run_events_button = QPushButton('Run events', self)
        self.run_events_button.clicked.connect(self.client.run_events)
        self.layout.addWidget(self.run_events_button)

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