import tkinter as tk
import pyautogui as pag
from listener import Listener

class App:
    def __init__(self, master) -> None:
        self.master = master
        
    def start_recording(self):
        self.master.destroy()
        events = Listener().listen()
        [print(f'event: {item}') for item in events]


def main():
    w = tk.Tk()
    button = tk.Button(w, text='Start recording', width=25, command=App(w).start_recording)
    button.pack()
    w.mainloop()

if __name__ == '__main__':
    main()