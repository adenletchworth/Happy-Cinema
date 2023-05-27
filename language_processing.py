from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk
import pandas as pd
import matplotlib.pyplot as plt

full_movie_data = pd.read_csv('movies_combined.csv')

description_df = full_movie_data['Description']

stop_words = set(stopwords.words('english'))

words = word_tokenize(description_df[0])

lz = WordNetLemmatizer()

tagged = nltk.pos_tag(words)
chunked_words = nltk.ne_chunk(tagged,binary=True)

all_words = []

for sentence in description_df:
    words = word_tokenize(sentence)
    for word in words:
        if word not in stop_words:
            all_words.append(lz.lemmatize(word.lower()))
 
print(nltk.FreqDist(all_words).most_common(20))

