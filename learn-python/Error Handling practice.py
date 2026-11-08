# ---------1----------
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return None


test = ["42", " 7 ", "4.5", "abc", ""]
for i in test:
    print(f" {to_int(i)}")

# -----------2------
customers = ["12", "abc", "-3", "5", "2.5"]
total = 0
for i in customers:
    try:
        qauntity = int(i)
        if qauntity < 0:
            print(f"Skipping {i} must be more than 0")
            continue

        total += qauntity
        print(f"qauntity: {qauntity}")

    except ValueError:
        print("Skipping {i} not a whole number")
print(f"Total= {total}")

# -----------3--------
