# main.py
from controller import GestureController
from action_mapper import ActionMapper

# ── Create the action mapper ──────────────────────────────
mapper = ActionMapper()  # no arguments needed

# ── Create gesture controller ────────────────────────────
controller = GestureController(mapper)

# ── Start gesture detection ──────────────────────────────
controller.start()
print("Gesture Controller running...")
print("Use gestures: 1 finger=scroll up, 2 fingers=scroll down, palm=zoom in, fist=zoom out")
print("Press Enter to stop the controller.")

# ── Keep program running until user presses Enter ────────
input()
controller.stop()
print("Gesture Controller stopped.")