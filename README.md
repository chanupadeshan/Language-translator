# Language Translator Application

A simple language translator application created using Python and Tkinter. This application translates text from one language to another using the `translate` library.

## Features

- Translate text from one language to another.
- Easy-to-use graphical interface.

## Requirements

- Python 3.x
- `translate` library
- `tkinter` and `ttkthemes`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/language-translator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd language-translator
    ```

3. Install the required libraries:

    ```bash
    pip install translate ttkthemes
    ```

## Usage

1. Run the application:

    ```bash
    python translator_app.py
    ```

2. **Select languages**: Choose the languages to translate from and to using the dropdown menus.
3. **Enter text**: Type the text you want to translate in the input field.
4. **Translate**: Click the "Translate" button to see the translation.

## Files

- `translator.py`: Main application script.
- `language_code.py`: Dictionary of language codes used for translation.

## screenshot
![language_Translator01](https://github.com/chanupadeshan/Language-translator/assets/90650370/8196f740-9c7d-4403-9eea-bc76b121869f)
![language_translator02](https://github.com/chanupadeshan/Language-translator/assets/90650370/bb50bba5-e2fd-4039-a783-68fdf95c1048)
![language_Translator03](https://github.com/chanupadeshan/Language-translator/assets/90650370/3d81312e-3adf-4f6f-b289-841cae8777d0)


## Example `language_code.py`

Here's an example `language_code.py` file:

```python
language_codes = {
    'afrikaans': 'af',
    'albanian': 'sq',
    'amharic': 'am',
    'arabic': 'ar',
    'armenian': 'hy',
    'azerbaijani': 'az',
    'basque': 'eu',
    'belarusian': 'be',
    'bengali': 'bn',
    'bosnian': 'bs',
    'bulgarian': 'bg',
    'catalan': 'ca',
    'cebuano': 'ceb',
    'chichewa': 'ny',
    'chinese (simplified)': 'zh-cn',
    'chinese (traditional)': 'zh-tw',
    'corsican': 'co',
    'croatian': 'hr',
    'czech': 'cs',
    'danish': 'da',
    'dutch': 'nl',
    'english': 'en',
    'esperanto': 'eo',
    'estonian': 'et',
    'filipino': 'tl',
    'finnish': 'fi',
    'french': 'fr',
    'frisian': 'fy',
    'galician': 'gl',
    'georgian': 'ka',
    'german': 'de',
    'greek': 'el',
    'gujarati': 'gu',
    'haitian creole': 'ht',
    'hausa': 'ha',
    'hawaiian': 'haw',
    'hebrew': 'he',
    'hindi': 'hi',
    'hmong': 'hmn',
    'hungarian': 'hu',
    'icelandic': 'is',
    'igbo': 'ig',
    'indonesian': 'id',
    'irish': 'ga',
    'italian': 'it',
    'japanese': 'ja',
    'javanese': 'jw',
    'kannada': 'kn',
    'kazakh': 'kk',
    'khmer': 'km',
    'korean': 'ko',
    'kurdish (kurmanji)': 'ku',
    'kyrgyz': 'ky',
    'lao': 'lo',
    'latin': 'la',
    'latvian': 'lv',
    'lithuanian': 'lt',
    'luxembourgish': 'lb',
    'macedonian': 'mk',
    'malagasy': 'mg',
    'malay': 'ms',
    'malayalam': 'ml',
    'maltese': 'mt',
    'maori': 'mi',
    'marathi': 'mr',
    'mongolian': 'mn',
    'myanmar (burmese)': 'my',
    'nepali': 'ne',
    'norwegian': 'no',
    'odia': 'or',
    'pashto': 'ps',
    'persian': 'fa',
    'polish': 'pl',
    'portuguese': 'pt',
    'punjabi': 'pa',
    'romanian': 'ro',
    'russian': 'ru',
    'samoan': 'sm',
    'scots gaelic': 'gd',
    'serbian': 'sr',
    'sesotho': 'st',
    'shona': 'sn',
    'sindhi': 'sd',
    'sinhala': 'si',
    'slovak': 'sk',
    'slovenian': 'sl',
    'somali': 'so',
    'spanish': 'es',
    'sundanese': 'su',
    'swahili': 'sw',
    'swedish': 'sv',
    'tajik': 'tg',
    'tamil': 'ta',
    'telugu': 'te',
    'thai': 'th',
    'turkish': 'tr',
    'ukrainian': 'uk',
    'urdu': 'ur',
    'uyghur': 'ug',
    'uzbek': 'uz',
    'vietnamese': 'vi',
    'welsh': 'cy',
    'xhosa': 'xh',
    'yiddish': 'yi',
    'yoruba': 'yo',
    'zulu': 'zu'
}