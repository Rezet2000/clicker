from listener import Listener
from runner import Runner

class Client:
    def __init__(self, master) -> None:
        self.master = master
        self.event_list = []
        
    def record_events(self):
        self.master.iconify()
        self.event_list = Listener().listen()
        self.master.deiconify()
    
    def print_event_list(self):
        [print(f'event: {item}') for item in self.event_list]

    def run_events(self):
        self.master.iconify()
        Runner(self.event_list).run_events()
        self.master.deiconify()