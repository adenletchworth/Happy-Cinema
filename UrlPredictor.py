
import numpy as np
from nltk.tokenize import word_tokenize
import pandas as pd
import tensorflow as tf
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.layers import Input, LSTM, Dense

class Url_Generator:
    def __init__(self,title_input):
        self.title_input = word_tokenize(title_input)
    
    def __len__(self):
        return len(self.title_input)

    def __getitem__(self):
        # Define input layer
        encoder_input_layer = Input(shape=(None,len(self)))
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
title_train_input = movies_df['Title']
url_train_input = movies_df['URL']
# Tokenize movie title input
title_input_seq = [word_tokenize(word) for word in title_train_input]




    
    

    