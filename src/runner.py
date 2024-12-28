import time
import pyautogui
from pynput import keyboard

class Runner:
    def __init__(self) -> None:
        self.running = True

    def stop_runner(self, key):
        if key == keyboard.Key.esc:
            self.running = False
            return False

    def run_events(self, event_list):
        with keyboard.Listener(on_release=self.stop_runner) as keyboard_listener:
            self.running = True
            while self.running:
                if event_list == []:
                    break
                for item in event_list:
                    if not self.running:
                        break
                    time.sleep(item['time'])
                    try:
                        if item['event'] == 'press':
                            pyautogui.press(item['key_value'])
                        if item['event'] == 'click':
                            pyautogui.click(*item['key_value'])
                    except Exception as e:
                        raise Exception('Something went wrong...', e)

        # Once the loop ends, stop the listener
        keyboard_listener.stop()