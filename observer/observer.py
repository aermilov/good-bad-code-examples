import random
import time

class Subject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, data):
        for observer in self._observers:
            observer.update(data)

class StockMarket(Subject):
    def __init__(self):
        super().__init__()
        self.prices = {}

    def set_price(self, stock, price):
        self.prices[stock] = price
        self.notify_observers({stock: price})

class Observer:
    def update(self, data):
        raise NotImplementedError("Subclasses should implement this!")

class PriceLogger(Observer):
    def update(self, data):
        print(f"Logging updated prices: {data}")

class TradingAlgorithm(Observer):
    def update(self, data):
        for stock, price in data.items():
            if price > 100:
                print(f"Executing BUY for {stock} at price {price}")
            elif price < 50:
                print(f"Executing SELL for {stock} at price {price}")

market = StockMarket()
logger = PriceLogger()
trader = TradingAlgorithm()

market.register_observer(logger)
market.register_observer(trader)

stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB']

while True:
    stock = random.choice(stocks)
    price = random.randint(30, 150)
    market.set_price(stock, price)
    time.sleep(1)
