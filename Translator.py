
from translate import Translator
from language_code import language_codes
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")
root.title("Translator")

def get_language_code(language_name):
    return language_codes.get(language_name.lower())


from_lang = tk.StringVar()
to_lang = tk.StringVar()
translate_word = tk.StringVar()

from_lang_label = ttk.Label(root,text="Enter the language you want to translate from: ",font=("Helvetica",16),foreground="green")
from_lang_label.pack()

from_lang_combobox = ttk.Combobox(root,values=list(language_codes.keys()),textvariable=from_lang)
from_lang_combobox.pack(pady=10)

to_lang_labal = ttk.Label(root,text="Enter the language you want to translate to: ",font=("Helvetica",16),foreground="green")
to_lang_labal.pack()

to_lang_combobox = ttk.Combobox(root,values=list(language_codes.keys()),textvariable=to_lang)
to_lang_combobox.pack(pady=10)


translate_word_label = ttk.Label(root,text="Enter the word you want to translate:",font=("Helvetica",16),foreground="green")
translate_word_label.pack()

translate_word_entry = ttk.Entry(root,textvariable=translate_word,width=50)
translate_word_entry.pack(pady=10)


# form_lang = input("Enter the language you want to translate from: ")
# to_lang = input("Enter the language you want to translate to: ")

# if form_lang not in language_codes.keys() or to_lang not in language_codes.keys():
#     print("Invalid language")
#     exit()
# else:
#     translate_word = input("Enter the word you want to transalte:")
#     translator = Translator(from_lang=get_language_code(form_lang),to_lang=get_language_code(to_lang))
#     translation = translator.translate(translate_word)
#     print(translation)  

root.mainloop()

