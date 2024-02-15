from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

class TextAnalyzer:
    def __init__(self, cog_service_endpoint, cog_service_key):
        self.cog_service_endpoint = cog_service_endpoint
        self.cog_service_key = cog_service_key

    def initialize_client(self):
        credential = AzureKeyCredential(self.cog_service_key)
        self.cog_client = TextAnalyticsClient(endpoint=self.cog_service_endpoint, credential=credential)

    def analyze_text(self, text):
        try:
            # Get language
            detected_language = self.cog_client.detect_language(documents=[text])[0]
            print('\nLanguage: {}'.format(detected_language.primary_language.name))

            # Get sentiment
            sentiment_analysis = self.cog_client.analyze_sentiment(documents=[text])[0]
            print("\nSentiment: {}".format(sentiment_analysis.sentiment))

            # Get key phrases
            phrases = self.cog_client.extract_key_phrases(documents=[text])[0].key_phrases
            if len(phrases) > 0:
                print("\nKey Phrases:")
                for phrase in phrases:
                    print('\t{}'.format(phrase))

            # Get entities
            entities = self.cog_client.recognize_entities(documents=[text])[0].entities
            if len(entities) > 0:
                print("\nEntities")
                for entity in entities:
                    print('\t{} ({})'.format(entity.text, entity.category))

            # Get linked entities
            linked_entities = self.cog_client.recognize_linked_entities(documents=[text])[0].entities
            if len(linked_entities) > 0:
                print("\nLinks")
                for linked_entity in linked_entities:
                    print('\t{} ({})'.format(linked_entity.name, linked_entity.url))

        except Exception as ex:
            print(ex)

    def analyze_file(self, file_path):
        try:
            # Read the file contents
            with open(file_path, encoding='utf8') as file:
                text = file.read()
                print('\n-------------\nFile: {}'.format(file_path))
                print('\n' + text)
                self.analyze_text(text)
        except Exception as ex:
            print(ex)
