import time
from pynput import mouse, keyboard

class Listener:
    def __init__(self) -> None:
        self.events = []

    def listen(self):
        self.events = [] # Clear events to not overlap event recordings
        start_time = time.time()

        def track_time():
            nonlocal start_time
            elapsed_time = time.time() - start_time
            start_time = time.time()
            return elapsed_time

        def on_click(x, y, button, pressed):
            if not pressed:
                self.events.append({
                    'event': 'click', 
                    'key_value': [x, y], 
                    'time': track_time()
                })
        
        def on_press(key):
            press_key = key.name if hasattr(key, 'name') else key.char
            print('key pressed:', press_key)
            if self.events:
                if self.events[-1]['event'] != 'press' and self.events[-1]['key_value'] != press_key:
                    self.events.append({
                        'event': 'press', 
                        'key_value': press_key, 
                        'time': 0,
                    })
            else:
                self.events.append({
                    'event': 'press', 
                    'key_value': press_key, 
                    'time': 0,
                })

        # Keyboard recorder
        def on_release(key):
            try:
                if key != keyboard.Key.esc:
                    press_key = key.name if hasattr(key, 'name') else key.char
                    print('key released:', press_key)
                    print(self.events)
                    self.events[-1]['event'] = 'release'
                    self.events[-1]['time'] = track_time()
                else:
                    mouse_listener.stop()
                    return False
            except AttributeError:
                print('key not supported')

        # Collect events until released
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as keyboard_listener, \
            mouse.Listener(
                on_click=on_click) as mouse_listener:

                keyboard_listener.join()
                mouse_listener.join()
        
        return self.events