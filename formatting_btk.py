def format_number(number):
    """Format a number to a more readable format with thousands separator."""
    return "{:,.2f}".format(number)

def generate_chart_url(symbol, platform="BINANCE", interval="1h"):
    """Generate a trading view chart URL for a given symbol and platform."""
    base_url = "https://www.tradingview.com/chart/"
    if platform.upper() == "BINANCE":
        chart_params = f"symbol=BINANCE:{symbol.upper()}&interval={interval}"
    elif platform.upper() == "KUCOIN":
        chart_params = f"symbol=KUCOIN:{symbol.replace('-','').upper()}&interval={interval}"
    else:
        chart_params = ""
    return f"{base_url}?{chart_params}"
