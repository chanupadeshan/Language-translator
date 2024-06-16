
from translate import Translator
from language_code import language_codes

def get_language_code(language_name):
    return language_codes.get(language_name.lower())


form_lang = 'english'
to_lang = 'spanish'

translator = Translator(from_lang='en',to_lang='es')
translation = translator.translate("Hello")
print(translation)  # Output: Hola
