# text_translation_module.py

from dotenv import load_dotenv
import os
from tkinter import Tk, filedialog
from text_translator_module import Translator

class TextTranslation:
    def __init__(self):
        try:
            # Get Configuration Settings
            load_dotenv()
            self.cog_key = os.getenv('COG_SERVICE_KEY')
            self.cog_region = os.getenv('COG_SERVICE_REGION')
            self.translator_endpoint = 'https://api.cognitive.microsofttranslator.com'

        except Exception as ex:
            print(ex)

    def get_text_file(self):
        root = Tk()
        root.withdraw()  # Hide the main window

        text_file = filedialog.askopenfilename(
            title="Select a Text File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        root.destroy()  # Close the main window

        return text_file

    def translate_text(self):
        try:
            # Create an instance of Translator
            translator = Translator(self.cog_key, self.cog_region, self.translator_endpoint)

            # Get the text file path using the file dialog
            text_file = self.get_text_file()

            if not text_file:
                print("No text file selected. Exiting.")
                return

            # Read the file contents
            text = open(text_file, encoding='utf8').read()

            # Detect the language
            language = translator.get_language(text)
            print('Language:', language)

            # Translate if not already English
            if language != 'en':
                translation = translator.translate(text, language)
                print("\nTranslation:\n{}".format(translation))

        except Exception as ex:
            print(ex)

def perform_text_translation():
    text_translation = TextTranslation()
    text_translation.translate_text()

if __name__ == "__main__":
    perform_text_translation()
