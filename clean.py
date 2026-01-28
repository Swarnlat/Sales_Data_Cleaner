import csv
import json

USD_TO_INR = 83

cleaned_data = []
seen_products = set()

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"].replace('"', '').strip()
        price_str = row["price"].replace("$", "").replace('"', '').strip()
        price_usd = float(price_str)

        key = (product, price_usd)
        if key in seen_products:
            continue

        seen_products.add(key)

        price_inr = round(price_usd * USD_TO_INR, 2)

        cleaned_data.append({
            "product": product,
            "price_usd": price_usd,
            "price_inr": price_inr,
            "country": row["country"].strip()
        })

with open("clean.json", "w") as json_file:
    json.dump(cleaned_data, json_file, indent=4)

print("Clean sales data saved to clean.json")
