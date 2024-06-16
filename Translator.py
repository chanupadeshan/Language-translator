
from translate import Translator
from language_code import language_codes

def get_language_code(language_name):
    return language_codes.get(language_name.lower())


form_lang = 'english'
to_lang = 'spanish'

translator = Translator(from_lang=get_language_code(form_lang),to_lang=get_language_code(to_lang))
translation = translator.translate("Hello")
print(translation)  # Output: Hola
