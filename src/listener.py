import time
from pynput import mouse, keyboard

class Listener:
    def __init__(self) -> None:
        self.events = []

    def listen(self):

        start_time = time.time()

        def track_time():
            nonlocal start_time
            elapsed_time = time.time() - start_time
            start_time = time.time()
            return elapsed_time

        def on_click(x, y, button, pressed):
            if not pressed:
                self.events.append(('click', [x, y], track_time()))


        # Keyboard recorder
        def on_release(key):
            # TO-D0: change verification of special keys, not by capturing the exception
            try:
                if key != keyboard.Key.esc:
                    self.events.append(('press', key.char, track_time()))
                else:
                    # Stop listener
                    mouse_listener.stop()
                    return False
            except AttributeError:
                self.events.append(('press', key.name, track_time()))

        # Collect events until released
        with keyboard.Listener(
                on_release=on_release) as keyboard_listener, \
            mouse.Listener(
                on_click=on_click) as mouse_listener:

                keyboard_listener.join()
                mouse_listener.join()
        
        return self.events