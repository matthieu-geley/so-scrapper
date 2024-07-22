from so_scrapping import *
import asyncio

if __name__ == '__main__':
    url = 'https://stackoverflow.com/questions?tab=newest&pagesize=50'
    scrapper = Scrapping(url)

    scrapper.get_response()
    
    scrapper.get_soup()
    
    data = scrapper.get_articles()
    
    scrapper.add_data(data)
    
    for i in range(1, 99):
        j = str(i+1)
        print('scrapping page ', j)
        url = 'https://stackoverflow.com/questjons?tab=newest&page=' + j
        scrapper = Scrapping(url)
        scrapper.get_response()
        scrapper.get_soup()
        data = scrapper.get_articles()
        scrapper.add_data(data)
    print('scrapping completed')