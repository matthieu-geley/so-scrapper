from so_scrapping import *
import datetime
import time
import threading


def scrape_page(i, scrapper):
    time.sleep(0.5)
    j = str(i+1)
    print('scrapping page ', j)
    url = 'https://stackoverflow.com/questions?tab=newest&page=' + j
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

        threads = []
        for i in range(1, 100):
            
            thread = threading.Thread(target=scrape_page, args=(i, scrapper))
            threads.append(thread)
            thread.start()

            time.sleep(0.5)

        for thread in threads:
            thread.join()

        print('total time taken: ', datetime.datetime.now() - now)
        print('scrapping completed')

    else:
        print('error in response, status code: ', scrapper.get_response())