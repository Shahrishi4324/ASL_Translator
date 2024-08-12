import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model

class HandGestureRecognition:
    def __init__(self):
        self.hand_detector = HandDetector()
        self.model = load_model('gesture_model.h5')
        self.gesture_labels = ['Fist', 'Palm', 'Peace', 'Thumbs Up']

    def recognize_gesture(self, img):
        img = self.hand_detector.findHands(img, draw=False)
        if self.hand_detector.results.multi_hand_landmarks:
            landmarks = self.hand_detector.results.multi_hand_landmarks[0].landmark
            data = []
            for lm in landmarks:
                data.extend([lm.x, lm.y, lm.z])
            data = np.array(data).reshape(1, -1)
            prediction = self.model.predict(data)
            gesture = self.gesture_labels[np.argmax(prediction)]
            return gesture
        return None

def main():
    cap = cv2.VideoCapture(0)
    recognizer = HandGestureRecognition()

    while True:
        success, img = cap.read()
        gesture = recognizer.recognize_gesture(img)
        if gesture:
            cv2.putText(img, gesture, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow("Gesture Recognition", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()