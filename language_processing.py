
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Initialize encoding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def getSimilarity(text,user_text):
    # Encode Texts 
    encoded_text = model.encode(text)
    encoded_user_text = model.encode(user_text)

    # Return Cosine Similarity between texts
    return cosine_similarity(encoded_text, encoded_user_text.reshape(1, -1))


def processInput(
        user_description: str, 
        user_genre: str, 
    ):
    
    
    # Importing movie data
    full_movie_data = pd.read_csv('current_movies.csv')

    similarity_description_scores=getSimilarity(full_movie_data.Description,user_description)
    similarity_genre_scores=getSimilarity(full_movie_data.Genre,user_genre)

    # Assign weights
    description_weight = .6
    genre_weight = .4

    # Calculate weighted similarity scores
    full_movie_data['Weighted_Scores'] = (description_weight * similarity_description_scores) + (genre_weight * similarity_genre_scores)

    # Sort movies based on weighted similarity scores
    max_index = full_movie_data['Weighted_Scores'].idxmax()

    # Get the most similar movie titles, descriptions, and genres
    most_similar_movie_titles = full_movie_data.Title[max_index]
    most_similar_movie_descriptions = full_movie_data.Description[max_index].strip()
    most_similar_movie_genres = full_movie_data.Genre[max_index].split()

    most_similar_genres = '  '.join(most_similar_movie_genres)

    return (most_similar_movie_titles, most_similar_movie_descriptions, most_similar_genres)




