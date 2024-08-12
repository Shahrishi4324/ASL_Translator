import pyttsx3
from sign_language_translator_gui import TranslatorApp

class TranslatorWithSpeech(TranslatorApp):
    def __init__(self, root):
        super().__init__(root)
        self.engine = pyttsx3.init()
        self.last_translation = None

    def translate(self, img):
        translation = super().translate(img)
        if translation != self.last_translation:
            self.engine.say(translation)
            self.engine.runAndWait()
            self.last_translation = translation
        return translation

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorWithSpeech(root)
    root.protocol("WM_DELETE_WINDOW", app.close)
    root.mainloop()