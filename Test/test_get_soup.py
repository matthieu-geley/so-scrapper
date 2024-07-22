import pytest
import sys
import os
directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'So_Scrapping'))
sys.path.append(directory_path)
from so_scrapping import *

def test_get_soup():
    url = 'https://stackoverflow.com/questions/tagged/python'
    scrapper = Scrapping(url)
    response = scrapper.get_response()
    soup = scrapper.get_soup()
    if soup is not None:
        print('Soup is not None')
    else:
        print('Soup is None')

test_get_soup()