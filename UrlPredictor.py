import numpy as np
from nltk.tokenize import word_tokenize
import pandas as pd
import tensorflow as tf
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.layers import Input, LSTM, Dense
from keras.utils import pad_sequences
from keras.preprocessing.text import Tokenizer


class Url_Generator:
    def __init__(self,title_input):
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(title_input)
        title_sequences = tokenizer.texts_to_sequences(title_input)
        title_input_seq = pad_sequences(title_sequences, padding='post')
        self.title_input_seq = title_input_seq

    def __len__(self):
        len(self.title_input_seq)
    def __getitem__(self):
        # Define input layer
        encoder_input_layer = Input(shape=(None,len(self.title_input_seq)))
        # Define LSTM layer
        encoder_ltsm_layer = LSTM(64,return_state=True)
        # Get encoded outputs,final hidden state, final cell state
        encoded_output, state_h, state_c = encoder_ltsm_layer(encoder_input_layer)
        encoder_states = [state_h,state_c]

        decoder_input_layer = Input(shape=(None,1))
        decoder_lstm_layer = LSTM(64,return_state=True,return_sequences=True)

        decoder_outputs, _, _ = decoder_lstm_layer(decoder_input_layer, initial_state=encoder_states)
        decoder_dense_layer = Dense(1,activation='softmax')
        decoded_output = decoder_dense_layer(decoder_outputs)

        model = Model([encoder_input_layer, decoder_input_layer], decoder_outputs)
        return model



# Import dataset
movies_df = pd.read_csv('movies_combined.csv')
# Get title input and URL input
title_train_input = movies_df['Title'].tolist()
url_train_input = movies_df['URL'].tolist()
# Tokenize movie title input (not implemented)


test_input = 'Lord of the Rings: Return of the King'

url = Url_Generator(test_input)

model = url.__getitem__()

model.compile(optimizer='adam', loss='categorical_crossentropy')

model.fit([title_input_seq, url_input_seq], url_input_seq, batch_size=32, epochs=10)

predicted_output = model.predict([title_input_seq, url_input_seq])
