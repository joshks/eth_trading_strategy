
import numpy as np
from pyswarm import pso

class AHPPSO:
    def __init__(self, model, bounds, args=()):
        self.model = model
        self.bounds = bounds
        self.args = args

    def objective_function(self, params):
        order = (int(params[0]), int(params[1]), int(params[2]))
        self.model.order = order
        self.model.fit(self.args[0])
        forecast = self.model.predict(start=self.args[1], end=self.args[2])
        return -np.corrcoef(forecast, self.args[3])[0, 1]

    def optimize(self):
        return pso(self.objective_function, self.bounds[:, 0], self.bounds[:, 1])
