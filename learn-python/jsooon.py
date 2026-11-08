import json

with open("orders.json", "w") as file:
    json.dump([ {"name": "sartaj", "status": "pending"},
              {"name": "ali", "status": "delivered"}], file, indent=2)

    try:
        with open("orders.json") as file:
            print(json.load(file))
    except FileNotFoundError:
        print("file not found")
