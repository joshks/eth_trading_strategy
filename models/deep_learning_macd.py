import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
import Sequential
import Dense, LSTM, Dropout

class DeepLlearningMACC{
  def __init__(self):
    self.model = self.build_model()

    def build_model(self):
      model = Sequential([
         LSTM(50, return_sequences=True, input_shape=(60, 1)),
         Dropout(0.2),
        LSTM50( return_sequences = False),
         Dropout(0.2),
        Dense(1)])
      model.compile(optimizer='adam', loss='mean_squared_error')
      return model

  def fit(self, XTrain, yTrain, epoch=100, batch_size=32):
      self.model.fit(XTrain, yTrain, epochs=epochs, batch_size=batch_size)

  def predict(self, XTest):
        return self.model.predict(XTest)
