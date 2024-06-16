from translate import Translator
from language_code import language_codes
import tkinter as tk
from tkinter import ttk

def get_language_code(language_name):
    return language_codes.get(language_name.lower())

def translate():
    from_lang_name = from_lang.get()
    to_lang_name = to_lang.get()
    word_to_translate = translate_word.get()

    from_lang_code = get_language_code(from_lang_name)
    to_lang_code = get_language_code(to_lang_name)

    if from_lang_code is None or to_lang_code is None:
        output.set("Invalid language name. Please enter a valid language name.")
        return
    
    translator = Translator(from_lang=from_lang_code, to_lang=to_lang_code)
    translation = translator.translate(word_to_translate)
    output.set(translation.capitalize())

# Create the main application window
root = tk.Tk()
root.geometry("600x400")
root.title("Translator")

# StringVars for inputs and output
from_lang = tk.StringVar()
to_lang = tk.StringVar()
translate_word = tk.StringVar()
output = tk.StringVar()

# Labels and Comboboxes for language selection
from_lang_label = ttk.Label(root, text="Translate from:", font=("Helvetica", 16), foreground="green")
from_lang_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

from_lang_combobox = ttk.Combobox(root, values=list(language_codes.keys()), textvariable=from_lang, width=30)
from_lang_combobox.grid(row=0, column=1, padx=10, pady=10)

to_lang_label = ttk.Label(root, text="Translate to:", font=("Helvetica", 16), foreground="green")
to_lang_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

to_lang_combobox = ttk.Combobox(root, values=list(language_codes.keys()), textvariable=to_lang, width=30)
to_lang_combobox.grid(row=1, column=1, padx=10, pady=10)

# Entry for word to translate
translate_word_label = ttk.Label(root, text="Enter text to translate:", font=("Helvetica", 16), foreground="green")
translate_word_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

translate_word_entry = ttk.Entry(root, width=50, textvariable=translate_word)
translate_word_entry.grid(row=2, column=1, padx=10, pady=10)

# Button to trigger translation
translate_button = ttk.Button(root, text="Translate", command=translate)
translate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label for displaying output
output_label = ttk.Label(root, textvariable=output, font=("Helvetica", 16), foreground="green")
output_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main GUI event loop
root.mainloop()
