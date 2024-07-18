import unittest
from main import Scrapping

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.scrapper = Scrapping('https://stackoverflow.com/questions?tab=newest&pagesize=50')

    def test_response(self):
        self.assertEqual(self.scrapper.get_response().status_code, 200)

    def test_soup(self):
        self.assertEqual(self.scrapper.get_soup(), BeautifulSoup(self.scrapper.get_response().content, 'html.parser'))

    def test_driver(self):
        self.assertEqual(self.scrapper.get_driver(), webdriver.Chrome())

    def test_articles(self):
        self.assertEqual(self.scrapper.get_articles(), self.scrapper.get_soup().find_all('div', class_='question-summary'))

    def test_connect_mongo(self):
        self.assertEqual(self.scrapper.mongo_connect(), pymongo.MongoClient('mongodb://localhost:27017/')['stackoverflow']['so_scrapper'])