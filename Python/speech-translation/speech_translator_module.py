from dotenv import load_dotenv
import os
import azure.cognitiveservices.speech as speech_sdk

class SpeechTranslator:
    def __init__(self, cog_service_key, cog_region):
        self.translation_config = speech_sdk.translation.SpeechTranslationConfig(cog_service_key, cog_region)
        self.translation_config.speech_recognition_language = 'en-US'
        self.translation_config.add_target_language('fr')
        self.translation_config.add_target_language('es')
        self.translation_config.add_target_language('hi')
        print('Ready to translate from', self.translation_config.speech_recognition_language)

        self.speech_config = speech_sdk.SpeechConfig(cog_service_key, cog_region)

    def translate(self, target_language):
        translation = ''

        # Translate speech
        audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
        translator = speech_sdk.translation.TranslationRecognizer(self.translation_config, audio_config=audio_config)
        print("Speak now...")
        result = translator.recognize_once_async().get()
        print('Translating "{}"'.format(result.text))
        translation = result.translations[target_language]
        print(translation)

        # Synthesize translation
        voices = {
            "fr": "fr-FR-HenriNeural",
            "es": "es-ES-ElviraNeural",
            "hi": "hi-IN-MadhurNeural"
        }
        self.speech_config.speech_synthesis_voice_name = voices.get(target_language)
        speech_synthesizer = speech_sdk.SpeechSynthesizer(self.speech_config)
        speak = speech_synthesizer.speak_text_async(translation).get()
        if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
            print(speak.reason)
