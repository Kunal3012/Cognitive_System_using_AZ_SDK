import requests

class Translator:
    def __init__(self, cog_key, cog_region, translator_endpoint):
        self.cog_key = cog_key
        self.cog_region = cog_region
        self.translator_endpoint = translator_endpoint

    def get_language(self, text):
        language = 'en'

        path = '/detect'
        url = self.translator_endpoint + path

        params = {
            'api-version': '3.0'
        }

        headers = {
            'Ocp-Apim-Subscription-Key': self.cog_key,
            'Ocp-Apim-Subscription-Region': self.cog_region,
            'Content-type': 'application/json'
        }

        body = [{'text': text}]

        request = requests.post(url, params=params, headers=headers, json=body)
        response = request.json()

        language = response[0]["language"]

        return language

    def translate(self, text, source_language):
        translation = ''

        path = '/translate'
        url = self.translator_endpoint + path

        params = {
            'api-version': '3.0',
            'from': source_language,
            'to': ['en']
        }

        headers = {
            'Ocp-Apim-Subscription-Key': self.cog_key,
            'Ocp-Apim-Subscription-Region': self.cog_region,
            'Content-type': 'application/json'
        }

        body = [{'text': text}]

        request = requests.post(url, params=params, headers=headers, json=body)
        response = request.json()

        translation = response[0]["translations"][0]["text"]

        return translation
