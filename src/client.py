from listener import Listener
from runner import Runner
from screen_drawer import ScreenDrawer
from PyQt5.QtWidgets import QApplication
import sys

class Client:
    def __init__(self, window) -> None:
        self.window = window
        self.event_list = []
        self.listener = Listener()
        self.runner = Runner()
        self.qt_app = QApplication(sys.argv)
        self.screen_drawer = None
        
    def record_events(self):
        self.window.iconify()
        self.event_list = self.listener.listen()
        self.window.deiconify()
    
    def show_events(self):
        [print(f'event: {item}') for item in self.event_list]
        points = [point['key_value'] for point in self.event_list if point['event'] == 'click']
        if self.screen_drawer:
            self.screen_drawer.close()
        self.screen_drawer = ScreenDrawer(points)
        self.screen_drawer.show()
        self.screen_drawer.closeEvent = self.on_screen_drawer_close

    def on_screen_drawer_close(self, event):
        self.screen_drawer = None
        event.accept()

    def run_events(self):
        if self.screen_drawer:
            self.screen_drawer.close()
        self.window.iconify()
        self.runner.run_events(self.event_list)
        self.window.deiconify()