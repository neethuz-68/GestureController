# Hotkey to toggle the controller on / off
TOGGLE_HOTKEY = "ctrl+alt+g"

# Webcam index (0 = default camera)
CAMERA_INDEX = 0

# Seconds to wait between repeated actions (prevents spamming)
GESTURE_COOLDOWN = 0.8

# Camera runs silently in background — no window ever shown
SHOW_PREVIEW = False

# Minimum confidence for hand detection
DETECTION_CONFIDENCE = 0.75
TRACKING_CONFIDENCE  = 0.70

# ── Per-application keyboard shortcuts ────────────────────────────────────────
#    Each action maps to either:
#      - a single key string   → pyautogui.press(key)
#      - a list of strings     → pyautogui.hotkey(*keys)
# ──────────────────────────────────────────────────────────────────────────────
APP_KEYMAPS = {
    # Microsoft PowerPoint
    "powerpoint": {
        "scroll_up":   "left",          # previous slide
        "scroll_down": "right",         # next slide
        "zoom_in":     ["ctrl", "="],
        "zoom_out":    ["ctrl", "-"],
    },
    # Microsoft Word
    "word": {
        "scroll_up":   "pageup",
        "scroll_down": "pagedown",
        "zoom_in":     ["ctrl", "="],
        "zoom_out":    ["ctrl", "-"],
    },
    # PDF viewers (Acrobat, Edge, Chrome, Foxit …)
    "pdf": {
        "scroll_up":   "pageup",
        "scroll_down": "pagedown",
        "zoom_in":     ["ctrl", "+"],
        "zoom_out":    ["ctrl", "-"],
    },
    # Fallback for any other window
    "default": {
        "scroll_up":   "pageup",
        "scroll_down": "pagedown",
        "zoom_in":     ["ctrl", "+"],
        "zoom_out":    ["ctrl", "-"],
    },
}