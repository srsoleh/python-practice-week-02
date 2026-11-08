print("start")
try:
    total = int(42)
    print("converted")
except ValueError as error:
    print(type(error))
print("done")
#---------3--
lines = ["A101,4500", "A102,abc", "A103,2300"]

def load_totals(lines):
    totals = []
    for l , line in enumerate(lines, start=51 ):
        order_id, sartaj =line.split(",")
        try:
            total= int(sartaj)
        except ValueError as error:
            raise ValueError(f"line{l}: total{sartaj} is not a whole number") from error
        totals.append(total)
    return totals
        
try:
    print(load_totals(lines))
except ValueError as s:
    print(f"could load file {s}")
cleaned_lines = ["A101,4500","A103,2300"]
print(load_totals(cleaned_lines))