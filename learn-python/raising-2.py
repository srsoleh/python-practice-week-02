orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": -200, "status": "pending"},
    {"total": 2300, "status": "delivered"},
    {"id": "A104", "total": "7600", "status": "delivered"},
    {"id": "A105", "total": 3900, "status": "lost"},
    {"id": "A106", "total": 6100, "status": "pending"},
]


def validate_order(order):
    if "id" not in order:
        raise ValueError("missing id")

    total = order.get("total")

    
    if not isinstance(total, (int, float)) or isinstance(total, bool):
        raise ValueError("total must be a number")

    
    if total <= 0:
        raise ValueError("total must be more than 0")

    
    valid = ["pending", "delivered", "cancelled"]
    if order.get("status") not in valid:
        raise ValueError(f"unknown status lost ")


valid_count = 0

for i, order in enumerate(orders, start=1):
    try:
        validate_order(order)
        valid_count += 1
    except ValueError as e:
        
        prefix = order.get("id", f"Order {i}")
        if "missing id" in str(e):
            print(f"Order {i}: {e}")
        else:
            print(f"{prefix}: {e}")

print(f"{valid_count} of {len(orders)} orders are valid")
