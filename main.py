from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as beautifulsoup
import requests
import pymongo
import re

class Scrapping():
    def __init__(self, url):
        """
        :param url: url of the page to be scrapped
        """
        self.url = url
        self.soup = None
        self.driver = None
        self.response = None

    def get_response(self):
        """
        :return: response of the url
        """
        self.response = requests.get(self.url)
        return self.response

    def get_soup(self):
        """
        :return: soup object of the response
        """
        self.soup = beautifulsoup(self.response.content, 'html.parser')
        return self.soup

    def get_driver(self):
        """
        :return: selenium driver object
        """
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        return self.driver

    def get_articles(self):
        """
        :return: articles from the page
        """
        get_id = re.compile(r'question-summary-\d+')
        articles = self.soup.find_all('div', id=get_id)
        for article in articles:
            title = article.find('a', class_='s-link').text
            link = article.find('a', class_='s-link')['href']
            summary = article.find('div', class_='s-post-summary--content-excerpt').text
            tagss = article.find_all('a', class_='s-tag')
            tags = [tag.text for tag in tagss]
            author_details = article.find('div', class_='s-user-card--link d-flex gs4').text
            date = article.find('span', class_='relativetime')['title']

            data = {
                'title': title,
                'link': link,
                'summary': summary,
                'tags': tags,
                'author_details': author_details,
                'date': date
            }

            collection = self.mongo_connect()
            collection.insert_one(data) if collection.find_one(data) is None else None

    def get_page(self, url):
        """
        :return: next page url
        """
        num_of_pages = self.soup.find('div', class_='s-pagination site1 themed pager float-left').text
        print(num_of_pages)

    def get_data(self):
        """
        :return: response, soup and articles from the page if status code is 200
        """
        if self.get_response().status_code == 200:
            self.get_soup()
            self.get_articles()
        else:
            print('Error in getting response, status code: ', self.get_response().status_code)

    def close(self):
        """
        close the driver
        """
        self.driver.close()

    def mongo_connect(self):
        """
        :return: mongodb collection object
        """
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['stackoverflow']
        collection = db['so_scrapper']
        return collection

if __name__ == '__main__':
    url = 'https://stackoverflow.com/questions?tab=newest&pagesize=50'
    print('initiating scrapping')
    scrapper = Scrapping(url)
    print('getting response')
    scrapper.get_response()
    print('getting soup')
    scrapper.get_soup()
    print('getting articles')
    scrapper.get_articles()
    for i in range(1, 999):
        i = str(i+1)
        print('scrapping page ', i)
        url = 'https://stackoverflow.com/questions?tab=newest&page=' + i
        scrapper = Scrapping(url)
        scrapper.get_response()
        scrapper.get_soup()
        scrapper.get_articles()
    print('scrapping completed')