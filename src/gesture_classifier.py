class GestureClassifier:

    def classify(self, hand_landmarks) -> str:
        lm      = hand_landmarks.landmark
        fingers = self._fingers_up(lm)
        total   = sum(fingers)

        # Open palm  →  Zoom In
        if total == 5:
            return "zoom_in"

        # Closed fist  →  Zoom Out
        if total == 0:
            return "zoom_out"

        # 1 finger (index only)  →  Scroll Up
        if fingers == [0, 1, 0, 0, 0]:
            return "scroll_up"

        # 2 fingers (index + middle)  →  Scroll Down
        if fingers == [0, 1, 1, 0, 0]:
            return "scroll_down"
        
        if fingers == [0, 1, 1, 1, 0]:
            return "next_slide"
        if fingers == [0, 1, 0, 0, 1]:
            return "prev_slide"

        return "none"

    # ── helpers ───────────────────────────────────────────────────────────────

    def _fingers_up(self, lm) -> list:
        """Return [thumb, index, middle, ring, pinky]  1=up  0=down."""
        fingers = []

        # Thumb: compare x-axis (mirrored feed)
        fingers.append(1 if lm[4].x < lm[3].x else 0)

        # Four fingers: tip y < pip y  means finger is up
        for tip, pip in [(8, 6), (12, 10), (16, 14), (20, 18)]:
            fingers.append(1 if lm[tip].y < lm[pip].y else 0)

        return fingers