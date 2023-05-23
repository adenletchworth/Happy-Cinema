import re
from bs4 import BeautifulSoup
import requests


class MovieScraper:
    def __init__(self, url):
        self.url = url
        self.movie_attributes = []

    def scrape_movie_attributes(self):
        tag_Scrape = requests.get(self.url)
        tag_html_Content = tag_Scrape.text
        soup = BeautifulSoup(tag_html_Content, 'lxml')

        movie_attributes_r = soup.find_all('span', class_='info-item-value')

        for attribute in movie_attributes_r:
            attribute_text = re.sub(r'\s+', ' ', attribute.text.strip())
            self.movie_attributes.append(attribute_text)

    def print_movie_attributes(self):
        for attribute in self.movie_attributes:
            print(attribute)