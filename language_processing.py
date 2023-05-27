from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def processInput(user_input: str):
    full_movie_data = pd.read_csv('movies_combined.csv')

    description_df = full_movie_data['Description']
    title_df = full_movie_data['Title']
    genre_df = full_movie_data['Genre']

    stop_words = set(stopwords.words('english'))

    lz = WordNetLemmatizer()

    input_tokens = word_tokenize(user_input)
    input_words = [lz.lemmatize(word.lower()) for word in input_tokens if word.lower() not in stop_words]

    # Encode movie descriptions and user input
    encoded_descriptions = model.encode(description_df)
    encoded_user_input = model.encode([' '.join(input_words)])

    # Calculate cosine similarity
    similarity_scores = cosine_similarity(encoded_descriptions, encoded_user_input)

    # Calculate weights
    description_weight = 0.6
    genre_weight = 0.4

    # Calculate weighted similarity scores
    weighted_scores = description_weight * similarity_scores

    # Sort movies based on weighted similarity scores
    sorted_indices = weighted_scores.argsort(axis=0)[::-1].flatten()

    # Find the most similar movie with the highest score
    most_similar_index = sorted_indices[0]

    # Get the most similar movie title, description, and genre
    most_similar_movie_title = title_df[most_similar_index]
    most_similar_movie_description = description_df[most_similar_index].strip()
    most_similar_movie_genre = genre_df[most_similar_index]

    return most_similar_movie_title, most_similar_movie_description, most_similar_movie_genre

# Load the pre-trained model for encoding text
model = SentenceTransformer('bert-base-nli-mean-tokens')

user_input = 'I want a psychological thriller with a female lead'
most_similar_movie_title, most_similar_movie_description, most_similar_movie_genre = processInput(user_input)
print("Title:", most_similar_movie_title)
print("Description:", most_similar_movie_description)
print("Genre:", most_similar_movie_genre)