from stocker import Stocker

microsoft = Stocker('MSFT')

stock_history = microsoft.stock
stock_history.head()