import tkinter as tk
from tkinter import Label
import cv2
from PIL import Image, ImageTk
from gesture_to_text import SignLanguageTranslator

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Language Translator")

        self.cap = cv2.VideoCapture(0)
        self.translator = SignLanguageTranslator()

        self.label = Label(self.root)
        self.label.pack()

        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        frame = self.translator.translate(frame)

        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        imgtk = ImageTk.PhotoImage(image=img)
        self.label.imgtk = imgtk
        self.label.config(image=imgtk)

        self.root.after(10, self.update_frame)

    def close(self):
        self.cap.release()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.protocol("WM_DELETE_WINDOW", app.close)
    root.mainloop()