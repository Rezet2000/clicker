import time
import pyautogui
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
                for item in self.event_list:
                    if not self.running:
                        break
                    print(item[1])
                    if item[0] == 'press':
                        pyautogui.press(item[1])
                    if item[0] == 'click':
                        pyautogui.click(item[1][0], item[1][1])
                    time.sleep(item[2])

        # Once the loop ends, stop the listener
        keyboard_listener.stop()