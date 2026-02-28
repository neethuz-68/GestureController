import time
import pyautogui
import keyboard

class ActionMapper:
    def __init__(self, get_active_window, cooldown=0.5):
        """
        get_active_window: function returning current window title
        cooldown: minimum seconds between executing the same gesture
        """
        self.get_active_window = get_active_window
        self.cooldown = cooldown
        self.last_triggered = {}  # store last time each gesture was executed

    def execute(self, gesture: str):
        now = time.time()
        # check cooldown
        if gesture in self.last_triggered:
            if now - self.last_triggered[gesture] < self.cooldown:
                return  # skip this gesture for now

        self.last_triggered[gesture] = now

        active_window = self.get_active_window()

        if "PowerPoint" in active_window:
            if gesture == "next_slide":
                keyboard.send("right")
            elif gesture == "prev_slide":
                keyboard.send("left")
            elif gesture == "scroll_up":
                pyautogui.scroll(20)
            elif gesture == "scroll_down":
                pyautogui.scroll(-20)
            elif gesture == "zoom_in":
                pyautogui.keyDown('ctrl')
                pyautogui.scroll(10)
                pyautogui.keyUp('ctrl')
            elif gesture == "zoom_out":
                pyautogui.keyDown('ctrl')
                pyautogui.scroll(-10)
                pyautogui.keyUp('ctrl')
        else:
            if gesture == "scroll_up":
                pyautogui.scroll(20)
            elif gesture == "scroll_down":
                pyautogui.scroll(-20)
            elif gesture == "zoom_in":
                pyautogui.keyDown('ctrl')
                pyautogui.scroll(10)
                pyautogui.keyUp('ctrl')
            elif gesture == "zoom_out":
                pyautogui.keyDown('ctrl')
                pyautogui.scroll(-10)
                pyautogui.keyUp('ctrl')