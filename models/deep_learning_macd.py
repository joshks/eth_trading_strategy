
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

class DeepLearningMACD:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        model = Sequential([
            LSTM(50, return_sequences=True, input_shape=(60, 1)),
            Dropout(0.2),
            LSTM(50, return_sequences=False),
            Dropout(0.2),
            Dense(1)
        ])
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model

    def fit(self, X_train, y_train, epochs=100, batch_size=32):
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

    def predict(self, X_test):
        return self.model.predict(X_test)
