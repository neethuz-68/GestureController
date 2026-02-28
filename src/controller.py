# controller.py
import threading
import cv2
import mediapipe as mp
from gesture_classifier import GestureClassifier

class GestureController:
    def __init__(self, action_mapper):
        """
        action_mapper: an instance of ActionMapper
        """
        self._mapper = action_mapper
        self._classifier = GestureClassifier()
        self._running = False
        self._thread = None

        self._mp_hands = mp.solutions.hands
        self._hands = self._mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def start(self):
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join()

    def _loop(self):
        cap = cv2.VideoCapture(0)  # default webcam

        # Lower resolution = faster processing
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        cap.set(cv2.CAP_PROP_FPS, 15)

        while self._running:
            ret, frame = cap.read()
            if not ret:
                continue

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self._hands.process(rgb)

            if results.multi_hand_landmarks:
                hand_lm = results.multi_hand_landmarks[0]
                gesture = self._classifier.classify(hand_lm)
                self._mapper.execute(gesture)

        cap.release()