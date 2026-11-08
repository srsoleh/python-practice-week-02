emails = ["AMNA@noorfoods.pk ", " ", "bilal.traders"]


def clean_email(email):
    cleaned = email.strip()

   
    if not cleaned:
        raise ValueError("email cannot be blank")

   
    if "@" not in cleaned:
        raise ValueError("email must contain @")

    
    return cleaned.lower()

for i in emails:
    try:
        result = clean_email(i)
        print(result)
    except ValueError as e:
        print(f"Skipping '{i}': {e}")
