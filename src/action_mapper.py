import pyautogui

class ActionMapper:
    """
    Maps gestures to actions using PyAutoGUI.
    Works for any active document (PPT, PDF, Word, browser, etc.)
    """

    def execute(self, gesture: str):
        if gesture == "scroll_up":
            pyautogui.scroll(20)        # scroll up
        elif gesture == "scroll_down":
            pyautogui.scroll(-20)       # scroll down
        elif gesture == "zoom_in":
            pyautogui.keyDown('ctrl')   # hold Ctrl
            pyautogui.scroll(10)        # scroll up = zoom in
            pyautogui.keyUp('ctrl')
        elif gesture == "zoom_out":
            pyautogui.keyDown('ctrl')   # hold Ctrl
            pyautogui.scroll(-10)       # scroll down = zoom out
            pyautogui.keyUp('ctrl')
        else:
            pass  # do nothing if gesture is "none"