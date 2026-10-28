import csv

with open("marketing_campaign_enriched.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

print("Customers:", len(rows))
print("Columns:", len(reader.fieldnames))
print("New fields:", ["Age", "Total_Spend", "Total_Purchases", "Children"])
print("First customer's Age:", rows[0]["Age"])
print("First customer's Total_Spend:", rows[0]["Total_Spend"])