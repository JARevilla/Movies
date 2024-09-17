# myapp/management/commands/crawler.py

import requests
from bs4 import BeautifulSoup # type: ignore
from django.core.management.base import BaseCommand # type: ignore
import pdb

class Command(BaseCommand):
    # pdb.set_trace()
    help = 'Crawl and scrape film information from the website and send to the API'
    print(help)

    # pdb.set_trace()
    def handle(self, *args, **kwargs):
        # pdb.set_trace()
        self.stdout.write(self.style.SUCCESS('Handle method started'))
        start_url = 'https://real-fmovies.show/fmovies.html'  # Replace with the starting URL
        api_url = 'http://127.0.0.1:8000//movies/bulkMovie/'  # Replace with your API endpoint
        # pdb.set_trace()
        self.crawl_page(start_url, api_url)
        # pdb.set_trace()

    # pdb.set_trace()
    def crawl_page(self, url, api_url):
        # pdb.set_trace()
        movie_data = []
        # print('testing')
        # Send a GET request to the URL
        try:
            # pdb.set_trace()
            response = requests.get(url)
            if response.status_code != 200:
                self.stdout.write(self.style.ERROR(f'Failed to retrieve {url}'))
                return

            # Parse the HTML content
            # pdb.set_trace()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract film data
            # pdb.set_trace()
            film_containers = soup.find_all('div', class_='_rDFitCirWH')
            for film in film_containers:
                # pdb.set_trace()
                title = film.get('data-filmname')
                image = film.find('img')['data-src']
                pagelink = 'https://real-fmovies.show' + film.find('a')['href']
                sitename = " https://real-fmovies.show/"

                # pdb.set_trace()
                # Prepare data for POST request
                data = {
                    'title': title,
                    'image': image,
                    'pagelink': pagelink,
                    'sitename': sitename
                }
                movie_data.append(data)

            # Send bulk POST request to the API
            bulk_data = {'movies': movie_data}
            api_response = requests.post(api_url, json=bulk_data, headers={'Content-Type': 'application/json'})

            print(api_response)
            # Find next page link
            ##### enable if want to go to next page #####
            # next_page = soup.find('a', class_='_BFKBqTHoir')
            # if next_page and 'href' in next_page.attrs:
            #     next_page_url =  next_page['href']
            #     url = 'https://real-fmovies.show' + next_page_url
            #     self.crawl_page(url, api_url)


        except Exception as e:
            # pdb.set_trace()
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))