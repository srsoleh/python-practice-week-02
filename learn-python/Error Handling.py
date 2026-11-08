quantities = ["12", "abc", "5"]
total = 0

for text in quantities:
    try:
        total = total + int(text)
        print(f"Quantity: {text}")
    except ValueError:
        print(f"{text} is invalide value")

print(f"Total: {total}")
