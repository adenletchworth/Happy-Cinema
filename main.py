import web_scraper
import language_processing
import time
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

print('Hello! Welcome to the application. I will give you a movie recommendation!')
time.sleep(1)
print('We can either try to find a similar movie or you can give us a genre and description')

user_dec_input = None

while not isinstance(user_dec_input, str):
    user_dec_input = input('Would you like to base your recommendation on a movie? ')
    if not isinstance(user_dec_input, str):
        print('Please enter a valid input')

lz = WordNetLemmatizer()
model = SentenceTransformer('bert-base-nli-mean-tokens')

stop_words = set(stopwords.words('english'))

sample_response = word_tokenize('yes')
tokenized_dec_input = word_tokenize(user_dec_input)

#filtered_sample_response = [lz.lemmatize(word.lower()) for word in sample_response if word not in stop_words]
filtered_dec_input = [lz.lemmatize(word.lower()) for word in tokenized_dec_input if word not in stop_words]

encoded_sample_response = model.encode(sample_response)
encoded_dec_input = model.encode(filtered_dec_input)

similarity = cosine_similarity(encoded_sample_response.reshape, encoded_dec_input.reshape(1,-1))

decision = False

print(similarity)

if similarity.any() > .99:
    decision = True

if False:
    while(decision):
        user_title_input = input('Please Input the Full Title of the Movie: ')
        guess_title = web_scraper.UrlPredictor(user_title_input)
else:
    print('OK')





