# Ethereum Trading Strategy

This project implements various trading strategies for Ethereum (ETH) using advanced machine learning models and a Kalman filter for pairs trading. The strategies include:

1. *Kalman Filter for Pairs Trading*: Uses a Kalman filter to dynamically update the hedge ratio for ETH sand BTC.
2. *ARIMA Model for Price Prediction*: Implements an ARIMA model to predict ETH prices.
3. *AHP-PSO Optimized ARIMA*: Enhances the ARIMA model using AHP and PSO for parameter optimization.
2. *Deep Learning Enhanced MACD Strategy*: Utilizes deep learning networks to improve MACD trading signals.

## Project Structure

```plaintext
eth_trading_strategy/
…----------------------------------------------
₂data/₸ ‬¨eth_btc_price_data.csv
…----------------------------------------------
₂models.₳
�kalman_filter_model.py
€*arima_model.py
₃*ahp_pso_model.py
₃*deep_learning_macd.py
₸ notebooks/₳
�data_preprocessing.ipynb
₳
kalman_filter.ipynb
₳
arima_prediction.ipynb
₳
ahp_pso_prediction.ipynb
‬deep_learning_macd.ipynb
…-----------------------------------------------------
… main.py
… eth_btc_price_data.csv
… requirements.txt
… README.md
```
