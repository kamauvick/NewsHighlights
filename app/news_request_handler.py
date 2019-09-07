from config import Config
import requests


class NewsRequest:
    def __init__(self):
        self.API_KEY = Config.API_KEY

    def get_sources(self):
        sources = []
        sources_url = 'https://newsapi.org/v2/sources?q={}&apiKey={}'.format(sources, self.API_KEY)
        response = requests.get(sources_url)
        if response.status_code == 200:
            for data in response.json()['sources']:
                pass

    def get_news(self, source):
        pass

    def get_article(self, article):
        pass
