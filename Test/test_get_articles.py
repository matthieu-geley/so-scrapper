import pytest
import sys
import os
directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'So_Scrapping'))
sys.path.append(directory_path)
from so_scrapping import *

def test_get_articles():
    url = 'https://stackoverflow.com/questions?tab=newest&pagesize=50'
    scrapper = Scrapping(url)
    response = scrapper.get_response()
    soup = scrapper.get_soup()
    articles = scrapper.get_articles()
    if articles is not None:
        print('Articles are not None')
        print(articles[0])
    else:
        print('Articles are None')

test_get_articles()