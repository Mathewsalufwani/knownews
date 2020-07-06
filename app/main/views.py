from flask import render_template
from . import main
from ..request import get_news, get_articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popular_news = get_news()
    return render_template('index.html', popular = popular_news)

@main.route('/articles/<source>')
def articles(source):
    '''
    View articles from source
    '''
    articles = get_articles(source)
    return render_template('articles.html', articles=articles)