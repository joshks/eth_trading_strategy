import pandas as pd
import statsmodels.tsa.arima.model import ARIMA
class ARIMAModel:
  def __init__(self, order):
    self.order = order

  def fit(self, X):
    self.model = ARIMA(X, order=self.order).fit()

  def predict(self, start, end):
    return self.model.predict(start=start, end=end)
