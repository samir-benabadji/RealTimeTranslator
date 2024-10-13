# translator/language_translation.py

from googletrans import Translator

class LanguageTranslator:
    def __init__(self, dest_language='fr'):
        self.dest_language = dest_language
        self.translator = Translator()

    def translate_text(self, text):
        try:
            translated = self.translator.translate(text, dest=self.dest_language)
            print(f"Translated: {translated.text}")
            return translated.text
        except Exception as e:
            print(f"Translation service error: {e}")
            return ""
