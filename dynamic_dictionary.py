import tkinter as tk
from tkinter import simpledialog
from gesture_to_text import SignLanguageTranslator

class CustomTranslator(SignLanguageTranslator):
    def __init__(self):
        super().__init__()

    def add_translation(self, gesture, translation):
        self.translation_dict[gesture] = translation

class TranslatorAppWithCustomDict(TranslatorApp):
    def __init__(self, root):
        super().__init__(root)
        self.translator = CustomTranslator()

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.settings_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Settings", menu=self.settings_menu)
        self.settings_menu.add_command(label="Add Gesture", command=self.add_gesture)

    def add_gesture(self):
        gesture = simpledialog.askstring("Input", "Enter gesture label:")
        translation = simpledialog.askstring("Input", "Enter translation:")
        if gesture and translation:
            self.translator.add_translation(gesture, translation)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorAppWithCustomDict(root)
    root.protocol("WM_DELETE_WINDOW", app.close)
    root.mainloop()