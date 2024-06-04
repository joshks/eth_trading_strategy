import numpy as np
import pandas as pd
from pykalman import KalmanFilter

class KalmanFilterPairsTrading:
    def init(self):
        self.kf = KalmanFilter(n_dim_obs=2, n_dim_state=2)

    def fit(self, X):
        self.kf = self.kf.em(X, n_iter=100)

    def predict(self, X):
        state_means, _ = self.kf.filter(X)
        return state_means

    def get_hedge_ratio(self, X):
        state_means = self.predict(X)
        return state_means.[, 0]
