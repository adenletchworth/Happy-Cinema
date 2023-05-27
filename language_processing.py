from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def processInput(user_description: str, user_genre: str):
    full_movie_data = pd.read_csv('movies_combined.csv')

    description_df = full_movie_data['Description']
    title_df = full_movie_data['Title']
    genre_df = full_movie_data['Genre']

    stop_words = set(stopwords.words('english'))

    lz = WordNetLemmatizer()

    input_tokens = word_tokenize(user_description)
    input_words = [lz.lemmatize(word.lower()) for word in input_tokens if word.lower() not in stop_words]

    # Encode movie descriptions and user input
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    encoded_descriptions = model.encode(description_df)
    encoded_user_description = model.encode([' '.join(input_words)])

    encoded_genres = model.encode(genre_df)
    encoded_user_genre = model.encode([user_genre])

    # Calculate cosine similarity
    similarity_description_scores = cosine_similarity(encoded_descriptions, encoded_user_description)
    similarity_genre_scores = cosine_similarity(encoded_genres, encoded_user_genre)

    # Calculate weights
    description_weight = .5
    genre_weight = .5

    # Calculate weighted similarity scores
    weighted_scores = (description_weight * similarity_description_scores) + (genre_weight * similarity_genre_scores)

    # Sort movies based on weighted similarity scores
    sorted_indices = weighted_scores.argsort(axis=0)[::-1].flatten()

    # Find the most similar movie with the highest score
    most_similar_index = sorted_indices[0]

    # Get the most similar movie title, description, and genre
    most_similar_movie_title = title_df[most_similar_index]
    most_similar_movie_description = description_df[most_similar_index].strip()
    most_similar_movie_genre = genre_df[most_similar_index]

    return most_similar_movie_title, most_similar_movie_description, most_similar_movie_genre

user_input = 'I want a happy movie with a good ending'
user_genre = 'Horror'

most_similar_movie_title, most_similar_movie_description, most_similar_movie_genre = processInput(user_input, user_genre)
print("Title:", most_similar_movie_title)
print("Description:", most_similar_movie_description)
print("Genre:", most_similar_movie_genre)