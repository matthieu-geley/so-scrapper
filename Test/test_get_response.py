import pytest
import sys
import os
directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'So_Scrapping'))
sys.path.append(directory_path)
from so_scrapping import *


def test_get_response():
    url = 'https://stackoverflow.com/questions/tagged/python'
    scrapper = Scrapping(url)
    response = scrapper.get_response()
    if response.status_code == 200:
        print('Response is 200')
    else:
        print('Response is :', response.status_code)

test_get_response()