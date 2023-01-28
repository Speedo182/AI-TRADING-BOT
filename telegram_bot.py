import telegram
from telegram.ext import Updater, CommandHandler
import signals_generator
import config

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Crypto Signals Bot. Send /help for more information.")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="This bot sends the buy and sell signals for the top 20 crypto coins (excluding stablecoins) with a margin from x5 to x100. Send /signals to receive the signals.")

def signals(update, context):
    coin_list = ["BTC", "ETH", "XRP", "LTC", "BCH", "BNB", "EOS", "BSV", "XLM", "ADA", "TRX", "LINK", "DOT", "XTZ", "YFI", "AAVE", "UNI", "DOGE", "SUSHI", "CRV"]
    signals = signals_generator.generate_signals(coin_list)
    message = "Signals:\n"
    for coin, signal in signals.items():
        message += f"{coin}: {signal}\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

if __name__ == "__main__":
    token = config.telegram_token
    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("signals", signals))

    updater.start_polling()
    updater.idle()
