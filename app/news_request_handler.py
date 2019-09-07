from config import Config


class NewsRequest:
    def __init__(self):
        self.API_KEY = Config.API_KEY

    def get_sources(self):
        pass

    def get_news(self, source):
        pass

    def get_article(self, article):
        pass
