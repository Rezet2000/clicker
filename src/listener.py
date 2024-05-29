from pynput import mouse, keyboard
from datetime import datetime

class Listener:
    def __init__(self) -> None:
        self.events = []
        self.prev_time = datetime.now()
    
    def track_time(self):
        elapsed_time = datetime.now() - self.prev_time
        self.prev_time = elapsed_time
        return elapsed_time

    def listen(self):
        def on_click(x, y, button, pressed):
            # print('{0} at {1}'.format(
            #     'Pressed' if pressed else 'Released',
            #     (x, y)))

            self.events.append(('click', [x, y], self.track_time()))

        # Keyboard recorder
        def on_release(key):
            # print('{0} released'.format(
            #     key))

            # TO-D0: change verification of special keys, not by capturing the exception
            try:
                if key != keyboard.Key.esc:
                    self.events.append(('press', key.char, self.track_time()))
                else:
                    # Stop listener
                    mouse_listener.stop()
                    return False
            except AttributeError:
                self.events.append(('press', key.name, self.track_time()))

        # Collect events until released
        with keyboard.Listener(
                on_release=on_release) as keyboard_listener, \
            mouse.Listener(
                on_click=on_click) as mouse_listener:

                keyboard_listener.join()
                mouse_listener.join()
        
        return self.events