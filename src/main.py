import tkinter as tk
from client import Client

def interface():
    window = tk.Tk()
    app = Client(window)

    button = tk.Button(window, text='Start recording', width=25, command=app.record_events)
    print_list = tk.Button(window, text='Print list', width=25, command=app.print_event_list)
    run_events = tk.Button(window, text='Run events', width=25, command=app.run_events)

    button.pack()
    print_list.pack()
    run_events.pack()

    window.title('Simple event recorder')
    window.geometry('300x200')
    window.mainloop()

if __name__ == '__main__':
    interface()