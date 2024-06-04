# Ethereum Trading Strategy

This project implements various trading strategies for Ethereum (ETH) using advanced machine learning models and a Kalman filter for pairs trading. The strategies include:

1. **Kalman Filter for Pairs Trading**: Uses a Kalman filter to dynamically update the hedge ratio for ETH and BTC.
2. **ARIMA Model for Price Prediction**: Implements an ARIMA model to predict ETH prices.
3. **AHP-PSO Optimized ARIMA**: Enhances the ARIMA model using AHP and PSO for parameter optimization.
4. **Deep Learning Enhanced MACD Strategy**: Utilizes deep learning networks to improve MACD trading signals.

## Project Structure

eth_trading_strategy/
├── data/
│   ├── eth_btc_price_data.csv
├── models/
│   ├── kalman_filter_model.py
│   ├── arima_model.py
│   ├── ahp_pso_model.py
│   ├── deep_learning_macd.py
├── notebooks/
│   ├── data_preprocessing.ipynb
│   ├── kalman_filter.ipynb
│   ├── arima_prediction.ipynb
│   ├── ahp_pso_prediction.ipynb
│   ├── deep_learning_macd.ipynb
├── main.py
├── requirements.txt
└── README.md

## Setup and Installation (continued)

Run the main script to execute all trading strategies:

```bash
python main.py
```

## Usage

Each model is implemented in a separate Python script under the models directory. The results can be visualized using the provided Jupyter notebooks.

## Contributing

Feel free to submit issues or pull quests if you find any bugs or have suggestions for improvements.


## License

This project is licensed under the MIT License.
