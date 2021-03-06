import urllib.request,json
from .models import News, Articles


# Getting api key
api_key = None

# Getting the movie base url
base_url = None
article_url = None

def configure_request(app):
    global api_key,base_url, article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['ARTICLES_API_BASE_URL']

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results

def process_results(source_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_results: A list of movie objects
    '''
    news_results = []
    for news_item in source_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')

        source_object = News(id, name, description, url, category, language)
        news_results.append(source_object)

    return news_results

def get_articles(source):
    '''
    Function that gets the json response to our url request
    '''
    get_article_url = article_url.format(source, api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_article_results(article_results_list)

        return article_results

def process_article_results(articles_list):
    '''
    Function that processes the article result and transforms them to a list of objects
    
    Args:
        article_list: A list of dictionaries that contain article details
    Returns:
        article_results: A list of article objects
    '''

    article_results = []
    for article_item in articles_list:
        id = article_item.get("id")
        title = article_item.get("title")
        description = article_item.get("description")
        url = article_item.get("url")
        urlToImage = article_item.get("urlToImage")
        publishedAt = article_item.get("publishedAt")

        article_object = Articles(id, title, description, url, urlToImage, publishedAt)
        article_results.append(article_object)

    return article_results