import requests

from config import Config


class NewsRequest:
    def __init__(self):
        self.API_KEY = Config.API_KEY

    def get_sources(self):
        sources = []
        sources_url = 'https://newsapi.org/v2/sources?q={}&apiKey={}'.format(sources, self.API_KEY)
        response = requests.get(sources_url)
        if response.status_code == 200:
            for data in response.json()['sources']:
                sources.append(data)
            print(sources)
            return sources

    def get_articles(self, article):
        articles = []
        articles_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(article, self.API_KEY)
        response = requests.get(articles_url)
        if response.status_code == 200:
            for data in response.json()['articles']:
                articles.append(data)
            print(articles)
            return articles
