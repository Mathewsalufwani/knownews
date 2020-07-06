from flask import render_template
from . import main
from ..request import get_news, get_articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Knownews"
    popular_news = get_news()
    return render_template('index.html', popular = popular_news, title=title)

@main.route('/articles/<source>')
def articles(source):
    '''
    View articles from source
    '''
    title = "Articles"
    articles = get_articles(source)
    return render_template('articles.html', articles=articles, title=title)