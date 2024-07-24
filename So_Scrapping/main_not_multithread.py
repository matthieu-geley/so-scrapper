from so_scrapping import *
import datetime
import time

if __name__ == '__main__':
    url = 'https://stackoverflow.com/questions?tab=newest&pagesize=50'
    scrapper = Scrapping(url)

    if str(scrapper.get_response()) == '<Response [200]>':

        now = datetime.datetime.now()

        scrapper.get_soup()

        data = scrapper.get_articles()

        scrapper.add_data(data)

        for i in range(1, 100):

            time.sleep(0.5)

            j = str(i+1)

            print('scrapping page ', j)

            url = 'https://stackoverflow.com/questjons?tab=newest&page=' + j

            scrapper = Scrapping(url)

            scrapper.get_response()

            scrapper.get_soup()

            data = scrapper.get_articles()

            scrapper.add_data(data)

        print('total time taken: ', datetime.datetime.now() - now)
        print('scrapping completed')

    else:
        print('error in response, status code: ', scrapper.get_response())