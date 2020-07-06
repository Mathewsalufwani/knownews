class Articles:
    '''
    Article class to define Source Objects
    '''

    def __init__(self,id,title,description,url,urlToImage,publishedAt):
        self.id = id 
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        