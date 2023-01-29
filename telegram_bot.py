import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
import requests
import json

# Define the Telegram bot
def start(bot, update):
    update.message.reply_text("Hello! I am your trading bot. How can I assist you today?")

def signals(bot, update, args):
    # Get the stock symbol from the user's message
    symbol = args[0]
    # Make an API call to get the stock data
    url = f'https://financialmodelingprep.com/api/v3/stock/real-time-price/{symbol}'
    response = requests.get(url)
    data = response.json()
    # Get the current price and change
    price = data['price']
    change = data['change']
    # Check if the change is positive or negative
    if change > 0:
        update.message.reply_text(f'{symbol} is currently trading at {price} and is up {change}.')
    else:
        update.message.reply_text(f'{symbol} is currently trading at {price} and is down {change}.')

def main():
    # Get the Telegram API key
    TELEGRAM_API_KEY = os.environ['TELEGRAM_API_KEY']
    # Create the Telegram bot
    updater = Updater(TELEGRAM_API_KEY)
    dp = updater.dispatcher
    # Add the command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("signals", signals, pass_args=True))
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
