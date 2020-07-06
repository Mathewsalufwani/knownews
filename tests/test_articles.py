import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles('abc-news','Louvre reopens in Paris for first time since March','Masks are compulsory and visitor numbers are restricted at the worlds most visited museum.','https://abcnews.go.com','https://ichef.bbci.co.uk/news/1024/branded_news/C9B3/production/_113253615_tv062312827.jpg','2020')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))


if __name__ == '__main__':
    unittest.main()