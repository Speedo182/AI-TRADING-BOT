import requests
import json

def scrape_news(coin_list):
    data = {}
    for coin in coin_list:
        url = f"https://api.coindesk.com/v1/bpi/historical/close.json?start=2010-07-17&end=2022-07-17&currency={coin}"
        response = requests.get(url)
        coin_data = json.loads(response.text)
        data[coin] = coin_data
    return data

if __name__ == "__main__":
    coin_list = ["BTC", "ETH", "XRP", "LTC", "BCH", "BNB", "EOS", "BSV", "XLM", "ADA", "TRX", "LINK", "DOT", "XTZ", "YFI", "AAVE", "UNI", "DOGE", "SUSHI", "CRV"]
    data = scrape_news(coin_list)
    print(data)
