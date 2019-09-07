from flask import render_template

from app.news_request_handler import NewsRequest
from . import main

news_request_handler = NewsRequest()


@main.route('/')
def index():
    sources = news_request_handler.get_sources()
    if sources:
        return render_template('index.html', sources=sources)
