
from translate import Translator
from language_code import language_codes

def get_language_code(language_name):
    return language_codes.get(language_name.lower())


form_lang = input("Enter the language you want to translate from: ")
to_lang = input("Enter the language you want to translate to: ")

if form_lang not in language_codes.keys() or to_lang not in language_codes.keys():
    print("Invalid language")
    exit()
else:
    translate_word = input("Enter the word you want to transalte:")
    translator = Translator(from_lang=get_language_code(form_lang),to_lang=get_language_code(to_lang))
    translation = translator.translate(translate_word)
    print(translation)  



