cart = ["rice", "oil"]
cart.append("sugar")
cart[1] = "ghee"
cart.remove("rice")
print(cart)
# ----------prac 02-
stock = {"pens": 120, "notebooks": 45}
stock["pens"] = 100
stock["markers"] = 60
del stock["notebooks"]
print(stock)
# --------- prac 03---
price = [850, 1200, 400]
for i in range(len(price)):
    price[i] = round(price[i] * 1.1)
print(price)
