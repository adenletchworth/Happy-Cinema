from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd

full_movie_data = pd.read_csv('movies_combined.csv')

description_df = full_movie_data['Description']

stop_words = set(stopwords.words('english'))

words = word_tokenize(description_df[0])

ps = PorterStemmer()

stemmed_words = [ps.stem(word) for word in words]

filtered_words = [word for word in words if not word in stop_words]

print(filtered_words)