
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def processInput(
        user_description: str, 
        user_genre: str, 
        #description_df: list,
        #genre_df: list,
        #title_df: list
    ):
    
    
    # Importing movie data
    full_movie_data = pd.read_csv('current_movies.csv')
    

    # Getting features from dataframe
    description_df = np.array(full_movie_data.Description)
    title_df = np.array(full_movie_data.Title)
    genre_df = np.array(full_movie_data.Genre)
   

    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Encode Movie Data fields
    encoded_descriptions = model.encode(description_df)
    encoded_genres = model.encode(genre_df)

    # Encode User Data fields
    encoded_user_description = model.encode(user_description)
    encoded_user_genre = model.encode(user_genre)

    # Calculate cosine similarity for movie versus input
    similarity_description_scores = cosine_similarity(encoded_user_description.reshape(1, -1), encoded_descriptions)
    similarity_genre_scores = cosine_similarity(encoded_user_genre.reshape(1, -1), encoded_genres)

    # Assign weights
    description_weight = .6
    genre_weight = .4

    # Calculate weighted similarity scores
    weighted_scores = (description_weight * similarity_description_scores) + (genre_weight * similarity_genre_scores)

    # Sort movies based on weighted similarity scores
    sorted_indices = weighted_scores.argsort(axis=0)[::-1].flatten()

    # Find the most similar movies with the highest score
    most_similar_indices = sorted_indices[0]

    # Get the most similar movie titles, descriptions, and genres
    most_similar_movie_titles = title_df[most_similar_indices]
    most_similar_movie_descriptions = description_df[most_similar_indices].strip()
    most_similar_movie_genres = genre_df[most_similar_indices]

    return (most_similar_movie_titles, most_similar_movie_descriptions, most_similar_movie_genres)




