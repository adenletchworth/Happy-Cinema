from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
import spacy

def processInput(user_input: str):
    full_movie_data = pd.read_csv('movies_combined.csv')

    description_df = full_movie_data['Description']
    title_df = full_movie_data['Title']

    stop_words = set(stopwords.words('english'))

    lz = WordNetLemmatizer()

    input_tokens = word_tokenize(user_input)
    input_words = [lz.lemmatize(word.lower()) for word in input_tokens if word.lower() not in stop_words]

    nlp = spacy.load('en_core_web_lg')

    input_ = nlp(" ".join(input_words))  # Convert input_words to string before passing to nlp

    max_similarity = 0
    similar_title = ""
    similar_description = ""

    clean_description_df = description_df.str.replace('\n', '').str.strip()

    for title, description in zip(title_df, clean_description_df):
        description_tokens = word_tokenize(description)
        description_words = [lz.lemmatize(word.lower()) for word in description_tokens if word.lower() not in stop_words]
        description_text = " ".join(description_words)
        description_ = nlp(description_text)
        similarity = input_.similarity(description_)
        if similarity > max_similarity:
            max_similarity = similarity
            similar_title = title
            similar_description = description

    return max_similarity, similar_title, similar_description

process = processInput('Mystery with lots of murder')
print(process)


