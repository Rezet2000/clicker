import tkinter as tk
import pyautogui as pag
from listener import Listener
from runner import Runner

class Client:
    def __init__(self, master) -> None:
        self.master = master
        self.event_list = []
        
    def record_events(self):
        self.master.iconify()
        events = Listener().listen()
        self.event_list = events
        self.master.deiconify()
    
    def print_event_list(self):
        [print(f'event: {item}') for item in self.event_list]

    def run_events(self):
        Runner(self.event_list).run_events()



def interface():
    w = tk.Tk()
    app = Client(w)

    button = tk.Button(w, text='Start recording', width=25, command=app.record_events)
    print_list = tk.Button(w, text='Print list', width=25, command=app.print_event_list)
    run_events = tk.Button(w, text='Run events', width=25, command=app.run_events)

    button.pack()
    print_list.pack()
    run_events.pack()

    w.mainloop()

if __name__ == '__main__':
    interface()