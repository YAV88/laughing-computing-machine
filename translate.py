import os
import json
from deep_translator import GoogleTranslator


class Translator:
    def translate(self, prompt):
        translator = GoogleTranslator(source='auto', target='en')
        r = translator.translate(prompt)
        return r