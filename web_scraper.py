import re
from bs4 import BeautifulSoup
import requests


class MovieScraper:
    def __init__(self, url):
        self.url = url
        self.movie_attributes = []

    def scrape_movie_attributes(self):

        # connect to the url
        movie_Scrape = requests.get(self.url)

        # get content of the page
        movie_html_Content = movie_Scrape.text

        # connect BeautifulSoup scraper
        soup = BeautifulSoup(movie_html_Content, 'lxml')

        # get the conent we are interested in
        movie_attributes_r = soup.find_all('span', class_='info-item-value')

        # forms text and adds to movie_attributes list
        for attribute in movie_attributes_r:
            attribute_text = re.sub(r'\s+', ' ', attribute.text.strip())
            self.movie_attributes.append(attribute_text)

    def print_movie_attributes(self):
        for attribute in self.movie_attributes:
            print(attribute)