import re
from bs4 import BeautifulSoup
import requests


class MovieScraper:
    def __init__(self, url):
        self.url = url
        self.movie_attributes = {}

    def get_movie_attributes(self):

        # connect to the url
        movie_Scrape = requests.get(self.url)

        # get content of the page
        movie_html_Content = movie_Scrape.text

        # connect BeautifulSoup scraper
        soup = BeautifulSoup(movie_html_Content, 'lxml')

        # get the conent we are interested in
        movie_attributes_r = soup.find_all('span', class_='info-item-value')
        movie_labels_r = soup.find_all('b', class_='info-item-label')

        # forms text and adds to movie_attributes list
        for label, attribute in zip(movie_labels_r, movie_attributes_r):
            label_text = label.text.replace(':','').strip()
            attribute_text = re.sub(r'\s+', ' ', attribute.text.strip())
            self.movie_attributes[label_text] = attribute_text

    def print_movie_attributes(self):
        for label, attribute in self.movie_attributes.items():
            print(f"{label}: {attribute}")




url = 'https://www.rottentomatoes.com/m/dark_nature_2022'

scrape = MovieScraper(url)

scrape.get_movie_attributes()

scrape.print_movie_attributes()