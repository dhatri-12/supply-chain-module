import numpy as np

class WMAForecaster:
    def __init__(self, weights):
        self.weights = np.array(weights)
        self.window = len(weights)

    def forecast(self, demand_series):
        if len(demand_series) < self.window:
            raise ValueError("Not enough data points to apply WMA with the given window size.")

        forecasts = []
        for t in range(self.window, len(demand_series)):
            window_data = demand_series[t - self.window:t]
            wma = np.sum(window_data * self.weights)
            forecasts.append(wma)

        return forecasts

    def evaluate(self, actual, forecasted):
        if len(actual) != len(forecasted):
            raise ValueError("Actual and forecasted data must be of the same length.")
        
        errors = np.abs(np.array(actual) - np.array(forecasted))
        mae = np.mean(errors)
        return mae
