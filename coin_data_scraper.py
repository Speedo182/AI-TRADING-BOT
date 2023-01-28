import requests
import json

def scrape_data(coin_list):
    data = {}
    for coin in coin_list:
        url = f"https://data.chain.link/v1/price/{coin}"
        response = requests.get(url)
        coin_data = json.loads(response.text)
        data[coin] = coin_data
    return data

if __name__ == "__main__":
    coin_list = ["BTC", "ETH", "XRP", "LTC", "BCH", "BNB", "EOS", "BSV", "XLM", "ADA", "TRX", "LINK", "DOT", "XTZ", "YFI", "AAVE", "UNI", "DOGE", "SUSHI", "CRV"]
    data = scrape_data(coin_list)
    print(data)
