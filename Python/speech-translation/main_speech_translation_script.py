from dotenv import load_dotenv
import os
from speech_translator_module import SpeechTranslator

class SpeechTranslation:
    def __init__(self):
        try:
            # Get Configuration Settings
            load_dotenv()
            self.cog_key = os.getenv('COG_SERVICE_KEY')
            self.cog_region = os.getenv('COG_SERVICE_REGION')

            # Create an instance of SpeechTranslator
            self.speech_translator = SpeechTranslator(self.cog_key, self.cog_region)

        except Exception as ex:
            print(ex)

    def run_translator(self):
        try:
            # Get user input
            target_language = ''
            while target_language != 'quit':
                target_language = input('\nEnter a target language\n fr = French\n es = Spanish\n hi = Hindi\n Enter anything else to stop\n').lower()
                if target_language in self.speech_translator.translation_config.target_languages:
                    self.speech_translator.translate(target_language)
                else:
                    target_language = 'quit'

        except Exception as ex:
            print(ex)

def perform_translation():
    translator_a = SpeechTranslation()
    translator_a.run_translator()

if __name__ == "__main__":
    perform_translation()