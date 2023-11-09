import re
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import spacy

class MovieScraper:
    def __init__(self, url):
        self.url = url
        self.movie_attributes = {}

    def find_movie_attributes(self):

        # connect to the url
        movie_Scrape = requests.get(self.url)

        # get content of the page
        movie_html_Content = movie_Scrape.text

        # connect BeautifulSoup scraper
        soup = BeautifulSoup(movie_html_Content, 'lxml')

        # get the conent we are interested in
        movie_attributes_r = soup.find_all('span', class_='info-item-value')
        movie_labels_r = soup.find_all('b', class_='info-item-label')
        movie_name_r = soup.find('h1',class_='title')
        movie_description = soup.find('p',{'data-qa':'movie-info-synopsis'})
        movie_genre = soup.find('span',class_='genre')

        if(movie_name_r != None):
            self.movie_attributes['URL'] = self.url
            self.movie_attributes['Title'] = movie_name_r.text
            self.movie_attributes['Description'] = movie_description.text.strip()
            self.movie_attributes['Genre'] = movie_genre.text.strip()

        # forms text and adds to movie_attributes list
        for label, attribute in zip(movie_labels_r, movie_attributes_r):
            label_text = label.text.replace(':','').strip()
            attribute_text = re.sub(r'\s+', ' ', attribute.text.strip())
            self.movie_attributes[label_text] = attribute_text


    def print_movie_attributes(self):
        for label, attribute in self.movie_attributes.items():
            print(f"{label}: {attribute}")

class UrlFinder:
    def __init__(self,movie_url_page):
        self.movie_url_page = movie_url_page
        self.url_Ending = set()

    def __getitem__(self):

        url_Scrape = requests.get(self.movie_url_page)

        url_Text = url_Scrape.content


        soup = BeautifulSoup(url_Text,'lxml')

        url_List = soup.find_all('a',{'data-track':'scores'})

        for url in url_List:
            self.url_Ending.add(url['href'])
            time.sleep(1)

def UrlPredictor(title_input):
    nlp = spacy.load("en_core_web_sm")
    doc=nlp(title_input)
    filtered_title = [token.text.lower() for token in doc if not token.is_punct]
    url = '_'.join(filtered_title)
    return 'https://www.rottentomatoes.com/m/' + url


def refreshDatabase():
    url1 = 'https://www.rottentomatoes.com/browse/movies_at_home/?page=100'
    url2 = 'https://www.rottentomatoes.com/browse/movies_in_theaters/?page=100'

    urls1 = UrlFinder(url1)
    urls2 = UrlFinder(url2)

    # Create a list to store movie attributes
    movie_data = []

    # Process urls1
    for url_end in urls1.url_Ending:
        current_url = 'https://www.rottentomatoes.com' + url_end
        scrape = MovieScraper(current_url)
        scrape.find_movie_attributes()
        movie_attributes = scrape.movie_attributes
        movie_data.append(movie_attributes)

    # Process urls2
    for url_end in urls2.url_Ending:
        current_url = 'https://www.rottentomatoes.com' + url_end
        scrape = MovieScraper(current_url)
        scrape.find_movie_attributes()
        movie_attributes = scrape.movie_attributes
        movie_data.append(movie_attributes)

    # Create a DataFrame using pd.concat
    url_df = pd.concat([pd.Series(data) for data in movie_data], axis=1)
    url_df = url_df.T
    # Write the DataFrame to a CSV file
    url_df.to_csv('current_movies.csv', index=False)

   
    







