import time
from pynput.mouse import Controller
from pynput.keyboard import Listener as KeyboardListener, KeyCode

class MouseMover:
    def __init__(self, controller):
        self.controller = controller
        self.is_running = True
        self.is_paused = False

    def jiggle_mouse(self):
        while self.is_running:
            if not self.is_paused:
                for direction in [(100, 0), (0, 100), (-100, 0), (0, -100)]:
                    if not self.is_running:
                        break
                    self.controller.move(*direction)
                    time.sleep(1)

    def start(self):
        print("\nPress 'p' to pause/resume or 's' to stop.")
        print("Starting mouse mover in ", end='', flush=True)
        for i in range(5, 0, -1):
            print(f"{i}...", end='', flush=True)
            time.sleep(1)
        print("Started!")
        with KeyboardListener(on_press=self.process_key):
            self.jiggle_mouse()

    def process_key(self, key):
        if key == KeyCode(char='s'):
            self.is_running = False
            print("\nStopping application.")
        elif key == KeyCode(char='p'):
            self.is_paused = not self.is_paused
            status = "Paused" if self.is_paused else "Resumed"
            print(f"\n{status} application.")

if __name__ == "__main__":
    mouse_controller = Controller()
    mover = MouseMover(mouse_controller)
    try:
        mover.start()
    except KeyboardInterrupt:
        print("\nExiting mouse mover.")
