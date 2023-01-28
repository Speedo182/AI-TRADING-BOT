import coin_data_scraper
import news_data_scraper
import config

def generate_signals(coin_list):
    signals = {}
    for coin in coin_list:
        coin_data = coin_data_scraper.scrape_data(coin)
        news_data = news_data_scraper.scrape_news(coin)

        # analyze data and generate signals
        current_price = coin_data["price"]
        volume = coin_data["volume"]
        news_sentiment = analyze_news_sentiment(news_data)
        historical_data = analyze_historical_data(coin_data)

        signal = None
        margin = config.min_margin
        if current_price * volume > news_sentiment + historical_data and margin > 5:
            signal = "BUY"
        elif current_price * volume < news_sentiment + historical_data and margin < 100:
            signal = "SELL"
        else:
            signal = "HOLD"

        signals[coin] = signal

    return signals

if __name__ == "__main__":
    coin_list = ["BTC", "ETH", "XRP", "LTC", "BCH", "BNB", "EOS", "BSV", "XLM", "ADA", "TRX", "LINK", "DOT", "XTZ", "YFI", "AAVE", "UNI", "DOGE", "SUSHI", "CRV"]
    signals = generate_signals(coin_list)
    print(signals)
