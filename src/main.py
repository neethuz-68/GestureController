import keyboard
from controller import GestureController
from action_mapper import ActionMapper

# ── Create the action mapper ──────────────────────────────
mapper = ActionMapper()  # no arguments needed

# ── Create gesture controller ────────────────────────────
controller = GestureController(mapper)

active = False

def toggle():
    global active
    if active:
        controller.stop()
        active = False
        print("Gesture control OFF")
    else:
        controller.start()
        active = True
        print("Gesture control ON")

# Assign a hotkey, e.g., Ctrl+Shift+G
keyboard.add_hotkey("ctrl+shift+g", toggle)

print("Press Ctrl+Shift+G to toggle gesture control")
keyboard.wait() 

# ── Start gesture detection ──────────────────────────────
'''controller.start()
print("Gesture Controller running...")
print("Use gestures: 1 finger=scroll up, 2 fingers=scroll down, palm=zoom in, fist=zoom out")
print("Press Enter to stop the controller.")

# ── Keep program running until user presses Enter ────────'''
input()
controller.stop()
print("Gesture Controller stopped.")