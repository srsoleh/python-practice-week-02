raw_orders = [
    {"customer": " noor foods ", "status": "Delivered", "paid": 1},
    {"customer": "BILAL TRADERS", "status": " pending ", "paid": 0},
    {"customer": "noor foods", "status": "PENDING", "paid": 0},
]

orders = []
for raw in raw_orders:
    orders.append(
        {
            "customer": raw["customer"].strip().title(),
            "status": raw["status"].strip().lower(),
            "paid": bool(raw["paid"]),
        }
    )

for order in orders:
    print(order)

customers = set()
for order in orders:
    customers.add(order["customer"])
print(sorted(customers))
