from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk
import pandas as pd
import matplotlib.pyplot as plt

full_movie_data = pd.read_csv('movies_combined.csv')

description_df = full_movie_data['Description']

stop_words = set(stopwords.words('english'))

words = word_tokenize(description_df[0])

ps = PorterStemmer()
lz = WordNetLemmatizer()

stemmed_words = [ps.stem(word) for word in words]

filtered_words = [word for word in stemmed_words if not word in stop_words]

lemmatized_words = [lz.lemmatize(word) for word in words]

tagged = nltk.pos_tag(words)
chunked_words = nltk.ne_chunk(tagged,binary=True)

print(lemmatized_words)
 