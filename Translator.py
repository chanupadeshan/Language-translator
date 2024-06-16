from translate import Translator
translator = Translator(from_lang='en',to_lang='es')
translation = translator.translate("Hello")
print(translation)  # Output: Hola
