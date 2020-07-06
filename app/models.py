class News:
    '''
    News class to define Source Objects
    '''

    def __init__(self,id,name,description,url,category,language):
        self.id = id 
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language

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