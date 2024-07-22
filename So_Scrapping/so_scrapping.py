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

    def get_articles(self):
        """
        :return: articles from the page
        """
        data = []
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

            data.append({
                'title': title,
                'link': link,
                'summary': summary,
                'tags': tags,
                'author_details': author_details,
                'date': date
            })
    
        return data

    def mongo_connect(self):
        """
        :return: mongodb collection object
        """
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['stackoverflow']
        collection = db['so_scrapper']
        return collection

    def add_data(self, data):
        """
        :add data to the collection
        """
        collection = self.mongo_connect()
        for datum in data:
            to_save = {
                'title': datum['title'],
                'link': datum['link'],
                'summary': datum['summary'],
                'tags': datum['tags'],
                'author_details': datum['author_details'],
                'date': datum['date']
            }
            collection.insert_one(to_save) if collection.find_one(to_save) is None else None

        return collection