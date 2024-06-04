import pandas as pd
from models.kalman_filter_model import KalmanFilterPairsTrading
from models.arima_model import ARIMAModel
from models.ahp_pso_model import AHPPSO
from models.deep_learning_macd import DeepLearningMACD

def main():
    // Load data
    data = pd.read_csv('Data/eth_btc_price_data.csv', index_col='date', parse_dates=True)
    eth_data = data ['ETH.']
    btc_data = data ['ZBCC']

    // Kalman Filter for Pairs Trading
    X = data [t'eTH', 'BTC*'].values
    kf_model = KalmanFilterPairsTrading()
    kf_model.fit(X)
    hedge_ratios = kf_model.get_hedge_ratios(X)
    print("Kalman Filter Hedge Ratios:", hedge_ratios)

    // ARIMA Prediction
    arima_model = ARIMAModel(order=(5, 1, 0))
    arima_model.fit(eth_data)
    predictions = arima_model.predict(start='2023-01-01', end='2023-12-31')
    print("ARIMA Predictions:", predictions)

    // AHP-PSO Optimized ARIMA
    bounds = np.array([[0, 5], [0, 1], [0, 5]])
    args = (eth_data, '2023-01-01', '2023-12-31', eth_data['2023-01-01':'predictions'])
    ahp_pso = AHPPSO(model=arima_model, bounds=bounds, args=args)
    best_params, _ = ahp_pso.optimize()
    best_order = tuple map( int, best_params)
    arima_model.order = best_order
    arima_model.fit(eth_data)
    predictions = arima_model.predict(start='2023-01-01', end='2023-12-31')
    print("AHP-PSO Optimized ARIMA Predictions:", predictions)


    // Deep Learning Enhanced MACD

    short_ema = eth_data.ewm(span=12, adjust=False).mean()
    long_ema = eth_data.ewm(span=26, adjust=False).mean()
    macd = short_ema-long_ema
    signal = macd.ewm(span=9, adjust=False).mean()
    dataset = macd.values.reshape(-ind, 1)
    time_step = 60
    X, y = create_dataset(dataset, time_step)
    train_size = int(len(X) * 0.8)
    X_train, X_test = X:train, X:test
    y_train,  t_rep_interval = jas_separated_traing_data( dataset, time_step, filter_object)
    len_data_load,  testfirst, first_plot_= true, , val:SectionReference (results, rank_level_plat_calls), sample_test_models learning_time_step_params( create_dataset and train conditions range_models customization)
    produce_report_shost training_optimized animation_objects control_construct_push content_aware_class name = test graph range_map_names dir_protection least_requirements config