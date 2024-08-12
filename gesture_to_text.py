import cv2
from gesture_recognition import HandGestureRecognition

class SignLanguageTranslator:
    def __init__(self):
        self.recognizer = HandGestureRecognition()
        self.translation_dict = {
            'Fist': 'Hello',
            'Palm': 'Goodbye',
            'Peace': 'Yes',
            'Thumbs Up': 'OK'
        }

    def translate(self, img):
        gesture = self.recognizer.recognize_gesture(img)
        if gesture:
            translation = self.translation_dict.get(gesture, "Unknown")
            cv2.putText(img, translation, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        return img

def main():
    cap = cv2.VideoCapture(0)
    translator = SignLanguageTranslator()

    while True:
        success, img = cap.read()
        img = translator.translate(img)
        cv2.imshow("Sign Language Translator", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()