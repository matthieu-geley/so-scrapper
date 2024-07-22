import pytest
import sys
import os
directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'So_Scrapping'))
sys.path.append(directory_path)
from so_scrapping import *

def test_add_data():
    url = 'https://stackoverflow.com/questions?tab=newest&pagesize=50'
    scrapper = Scrapping(url)

    scrapper.get_response()
    
    scrapper.get_soup()
    
    data = scrapper.get_articles()
    
    scrapper.add_data(data)

    print('Test passed')
    assert True

test_add_data()