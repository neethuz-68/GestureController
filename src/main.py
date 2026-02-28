import sys
import threading
import keyboard
from controller import GestureController
from action_mapper import ActionMapper

if sys.platform == "win32":
    import win32gui
    def get_active_window():
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())

elif sys.platform == "darwin":
    from AppKit import NSWorkspace
    def get_active_window():
        return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']

else:
    import subprocess
    def get_active_window():
        try:
            return subprocess.check_output(
                ["xdotool", "getactivewindow", "getwindowname"]
            ).decode().strip()
        except Exception:
            return ""

mapper = ActionMapper(get_active_window)
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