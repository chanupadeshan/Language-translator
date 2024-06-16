
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

def get_language_code(language_name):
    return language_codes.get(language_name.lower())

def translate():
    from_lang_code = get_language_code(from_lang.get())
    to_lang_code = get_language_code(to_lang.get())
    word_to_translate = translate_word.get()

    if from_lang_code not in language_codes.keys() or to_lang_code not in language_codes.keys():
        print("Invalid language")
        exit()
    
    else:
        translator = Translator(from_lang=from_lang_code,to_lang=to_lang_code)
        translation = translator.translate(word_to_translate)
        print(translation)


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

translate_word_entry = ttk.Entry(root,width=50)
translate_word_entry.pack(pady=10)


enter_button = ttk.Button(root,text="Tranlate",command=translate)
enter_button.pack(pady=10)


# if from_lang not in language_codes.keys() or to_lang not in language_codes.keys():
#     print("Invalid language")
#     exit()
# else:
#     translate_word = input("Enter the word you want to transalte:")
#     translator = Translator(from_lang=get_language_code(from_lang),to_lang=get_language_code(to_lang))
#     translation = translator.translate(translate_word)
#     print(translation)  

root.mainloop()

