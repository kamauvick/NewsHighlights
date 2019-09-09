from flask import render_template

from . import main


@main.errorhandler(404)
def errorpage(error):
    return render_template('404.html', error=error), 404
