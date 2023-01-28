import ccxt

def connect_to_exchange(exchange_id):
    """Connects to the specified exchange and returns an instance of the exchange class.
    
    Args:
        exchange_id (str): The id of the exchange to connect to.
        
    Returns:
        object: An instance of the exchange class.
    """
    # create the exchange object
    exchange = getattr(ccxt, exchange_id)()
    # set the API credentials
    exchange.apiKey = 'YOUR_API_KEY'
    exchange.secret = 'YOUR_SECRET_KEY'
    return exchange
