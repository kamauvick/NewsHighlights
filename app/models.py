""" Model class for news """


class News:
    def __init__(self, source, urlToImage, description, title, author):
        self.urlToImage = urlToImage
        self.description = description
        self.title = title
        self.author = author
        self.source = source


""" Model class for articles which inherits from news """


class Articles(News):
    def __init__(self):
        super(News, self).__init__()
