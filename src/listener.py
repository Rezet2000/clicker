from pynput import mouse, keyboard

class Listener:
    def __init__(self) -> None:
        self.events = []

    def listen(self):
        hotkey_collector = []

        def on_click(x, y, button, pressed):
            # print('{0} at {1}'.format(
            #     'Pressed' if pressed else 'Released',
            #     (x, y)))
            self.events.append(('click', [x, y]))

        def on_press(key):
            nonlocal hotkey_collector
            try:
                # print('alphanumeric key {0} pressed'.format(
                #     key.char))
                hotkey_collector.append(key.char)
            except AttributeError:
                # print('special key {0} pressed'.format(
                #     key))
                hotkey_collector.append(key)

        def on_release(key):
            nonlocal hotkey_collector
            # print('{0} released'.format(
            #     key))

            if key != keyboard.Key.esc:
                if len(hotkey_collector) > 1:
                    self.events.append(('hotkey', hotkey_collector.copy()))
                elif len(hotkey_collector) == 1:
                    self.events.append(('press', hotkey_collector.copy()))
                hotkey_collector.clear()
            else:
                # Stop listener
                mouse_listener.stop()
                return False

        # Collect events until released
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as keyboard_listener, \
            mouse.Listener(
                on_click=on_click) as mouse_listener:

                keyboard_listener.join()
                mouse_listener.join()
        
        return self.events