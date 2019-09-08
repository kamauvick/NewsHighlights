from flask import render_template, request

from app.news_request_handler import NewsRequest
from . import main

news_request_handler = NewsRequest()


@main.route('/')
def index():
    sources = news_request_handler.get_sources()
    if sources:
        return render_template('index.html', sources=sources)


@main.route('/articles', methods=["POST", "GET"])
def articles_page():
    if request.method == 'POST':
        search = request.form.get("search")
        articles = news_request_handler.get_articles(search)
    else:
        articles = news_request_handler.get_articles("tech")
    return render_template('articles_display.html', articles=articles)
    # return render_template('404.html', error = "Error while making request")
