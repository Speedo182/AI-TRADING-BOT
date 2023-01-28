import ccxt
import pandas as pd
import numpy as np

def backtesting(signals, trade_orders, exchange_id):
    # initialize the exchange
    exchange = getattr(ccxt, exchange_id)()

    # create a new dataframe to store the results
    backtesting_results = pd.DataFrame(columns=["timestamp", "coin", "signal", "price", "position_size", "stop_loss", "take_profit", "profit_loss", "cumulative_profit_loss"])

    # set the current capital
    current_capital = 100

    # get the historical data
    historical_data = exchange.fetch_ohlcv("BTC/USD")

    # iterate over the historical data
    for i, data in enumerate(historical_data):
        # get the date
        date = pd.to_datetime(data[0], unit='ms')

        # get the trade orders for the current date
        current_trade_orders = trade_orders.loc[trade_orders["timestamp"] == date]

        # iterate over the trade orders
        for j, trade_order in current_trade_orders.iterrows():
            # get the signal for the current coin
            signal = signals.loc[signals["coin"] == trade_order["coin"]]["signal"].iloc[0]

            # check if the signal is a buy signal
            if signal == "buy":
                # get the previous sell order for the current coin
                previous_sell_order = backtesting_results.loc[(backtesting_results["coin"] == trade_order["coin"]) & (backtesting_results["signal"] == "sell")].iloc[-1]

                # calculate the position size
                position_size = current_capital * trade_order["position_size"] / data[1]

                # calculate the stop loss and take profit
                stop_loss = data[1] * (1 - trade_order["stop_loss"])
                take_profit = data[1] * (1 + trade_order["take_profit"])

                # execute the trade
                current_capital -= position_size * data[1]

                # add the results to the backtesting_results dataframe
                backtesting_results = backtesting_results.append({"timestamp": date, "coin": trade_order["coin"], "signal": signal, "price": data[1], "position_size": position_size, "stop_loss": stop_loss, "take_profit": take_profit, "profit_loss": 0, "cumulative_profit_loss": current_capital}, ignore_index=True)

            # check if the signal is a sell signal
            elif signal == "sell":
                # get the previous buy order for the current coin
                previous_buy_order = backtesting_results.loc[(backtesting_results["coin"] == trade_order["coin"]) & (backtesting_results["signal"] == "buy")].iloc[-1]

                # calculate the position size
                position_size = previous_buy_order["position_size"]

                # calculate the stop loss and take profit
                stop_loss = 0
                take_profit = 0

                # execute the trade
                current_capital += position_size * data[1]

                # calculate the profit loss
                profit_loss = (data[1] - previous_buy_order["price"]) * position_size

                # add the results to the backtesting_results dataframe
                backtesting_results = backtesting_results.append({"timestamp": date, "coin": trade_order["coin"], "signal": signal, "price": data[1], "position_size": position_size, "stop_loss": stop_loss, "take_profit": take_profit, "profit_loss": profit_loss, "cumulative_profit_loss": current_capital}, ignore_index=True)

    # calculate the performance metrics
    annual_return = (current_capital / 100) ** (365 / backtesting_results["timestamp"].nunique()) - 1
    sharpe_ratio = (backtesting_results["profit_loss"].mean() / backtesting_results["profit_loss"].std()) * np.sqrt(365)
    max_drawdown = (backtesting_results["cumulative_profit_loss"].cummax() - backtesting_results["cumulative_profit_loss"]) / backtesting_results["cumulative_profit_loss"].cummax()

    # print the results
    print("Annual return: {:.2%}".format(annual_return))
    print("Sharpe ratio: {:.2f}".format(sharpe_ratio))
    print("Max drawdown: {:.2%}".format(max_drawdown.max()))

if __name__ == "__main__":
    # load the signals
    signals = pd.read_csv("signals.csv")

    # load the trade orders
    trade_orders = pd.read_csv("trade_orders.csv")

    # set the exchange
    exchange_id = "binance"

    # execute the bot in backtesting
    backtesting(signals, trade_orders, exchange_id)


