stock = 120
before = id(stock)
stock += 30
print(id(stock) == before)

prices = [850, 1200]
before = id(prices)
prices.append(400)
print(id(prices) == before)
