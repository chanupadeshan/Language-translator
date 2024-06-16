from translate import Translator
from language_code import language_codes
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")
root.title("Translator")

from_lang = tk.StringVar()
to_lang = tk.StringVar()
translate_word = tk.StringVar()
output=tk.StringVar()

def get_language_code(language_name):
    return language_codes.get(language_name.lower())

def translate():
    from_lang_name = from_lang.get()
    to_lang_name = to_lang.get()
    word_to_translate = translate_word.get()

    from_lang_code = get_language_code(from_lang_name)
    to_lang_code = get_language_code(to_lang_name)

    if from_lang_code is None or to_lang_code is None:
        print("Invalid language name. Please enter a valid language name.")
        invalid="Invalid language name. Please enter a valid language name."
        output.set(invalid)
        return

    
    translator = Translator(from_lang=from_lang_code, to_lang=to_lang_code)
    translation = translator.translate(word_to_translate)
    print(translation)
    output.set(translation.capitalize())

from_lang_label = ttk.Label(root, text="Enter the language you want to translate from:", font=("Helvetica", 16), foreground="green")
from_lang_label.pack()

from_lang_combobox = ttk.Combobox(root, values=list(language_codes.keys()), textvariable=from_lang)
from_lang_combobox.pack(pady=10)

to_lang_label = ttk.Label(root, text="Enter the language you want to translate to:", font=("Helvetica", 16), foreground="green")
to_lang_label.pack()

to_lang_combobox = ttk.Combobox(root, values=list(language_codes.keys()), textvariable=to_lang)
to_lang_combobox.pack(pady=10)

translate_word_label = ttk.Label(root, text="Enter the word you want to translate:", font=("Helvetica", 16), foreground="green")
translate_word_label.pack()

translate_word_entry = ttk.Entry(root, width=50, textvariable=translate_word)
translate_word_entry.pack(pady=10)

translate_button = ttk.Button(root, text="Translate", command=translate)
translate_button.pack(pady=10)

output_label = ttk.Label(root,textvariable=output, font=("Helvetica", 16), foreground="green")
output_label.pack()

root.mainloop()
