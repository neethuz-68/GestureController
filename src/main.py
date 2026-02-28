import keyboard
from controller import GestureController
from action_mapper import ActionMapper

mapper = ActionMapper()
controller = GestureController(mapper)

active = False

def toggle():
    global active
    if active:
        controller.stop()
        active = False
        print("Gesture OFF")
    else:
        controller.start()
        active = True
        print("Gesture ON")

# Assign hotkey
keyboard.add_hotkey("ctrl+shift+g", toggle)

print("Gesture Controller running in background. Press Ctrl+Shift+G to toggle.")
keyboard.wait()  # keep script alive