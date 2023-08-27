import web_scraper
import language_processing
import time
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def movieLookup():
    while True:
        user_title_input = input('Please Input the Full Title of the Movie: ')
        guess_title = web_scraper.UrlPredictor(user_title_input)
        movie_finder =  web_scraper.MovieScraper(guess_title)
        movie_finder.find_movie_attributes()
        if movie_finder.movie_attributes == {}:
            notFoundDec = input('Movie Not Found, Would you like to try again y/n')
            if notFoundDec == 'y':
                comparasion()
            else:
                continue
        else:
            print(movie_finder.movie_attributes)
            nextDec = input('Is this the movie you are looking for y/n')

            if nextDec == 'y':
                language_processing.processInput()
            else:
                continue

def comparasion():
    user_description = input("Please Enter a Description to base your Reccomendation off of")
    user_genre = input("Please Enter a Genre to base your movie reccomendation off of")

    language_processing.processInput(user_description, user_genre)

print('Hello! Welcome to the application. I will give you a movie recommendation!')
print('We can either try to find a similar movie or you can give us a genre and description')

user_dec_input = None

while not isinstance(user_dec_input, str):
    user_dec_input = input('Would you like to base your recommendation on a movie? y/n ')
    if not isinstance(user_dec_input, str):
        print('Please enter a valid input')

    if user_dec_input == 'y':
        movieLookup()
    else:
        comparasion()
