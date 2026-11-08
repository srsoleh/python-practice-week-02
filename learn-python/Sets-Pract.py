# --------------01----------
city = ["Karachi", "Lahore", "Karachi", "Multan", "Lahore"]
new_cities = set(city)

print(len(new_cities))
print(sorted(new_cities))
# -------- 02----
order = ["A101", "A102", "A101", "A103", "A102"]
seen = set()

for o in order:
    if o in seen:
        print(f"Duplicate: {o}")
    else:
        seen.add(o)
