import time
from pynput import keyboard

class Runner:
    def __init__(self, event_list) -> None:
        self.event_list = event_list
        self.running = True

    def stop_runner(self, key):
        if key == keyboard.Key.esc:
            self.running = False
            return False  # Stop the listener

    def run_events(self):
        with keyboard.Listener(on_release=self.stop_runner) as keyboard_listener:
            while self.running:
                print('Printing...')
                time.sleep(1)

        # Once the loop ends, stop the listener
        keyboard_listener.stop()