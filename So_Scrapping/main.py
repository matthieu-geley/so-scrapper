from so_scrapping import *
import datetime
import time
import concurrent.futures

def scrape_page(url):
    scrapper = Scrapping(url)
    scrapper.get_response()
    scrapper.get_soup()
    data = scrapper.get_articles()
    scrapper.add_data(data)

if __name__ == '__main__':
    url = 'https://stackoverflow.com/questions?tab=newest&pagesize=50'
    scrapper = Scrapping(url)

    if str(scrapper.get_response()) == '<Response [200]>':
        now = datetime.datetime.now()
        scrapper.get_soup()
        data = scrapper.get_articles()
        scrapper.add_data(data)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for i in range(1, 100):
                j = str(i+1)
                print('scrapping page', j)
                url = 'https://stackoverflow.com/questions?tab=newest&page=' + j
                futures.append(executor.submit(scrape_page, url))

            # Wait for all futures to complete
            concurrent.futures.wait(futures)

        print('total time taken:', datetime.datetime.now() - now)
        print('scrapping completed')

    else:
        print('error in response, status code:', scrapper.get_response())
