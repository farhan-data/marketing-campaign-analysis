import csv

input_file = "marketing_campaign_data.csv"
output_file = "marketing_campaign_enriched.csv"

with open(input_file, "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    original_columns = reader.fieldnames

spending_columns = [
    "MntWines",
    "MntFruits",
    "MntMeatProducts",
    "MntFishProducts",
    "MntSweetProducts",
    "MntGoldProds",
]

purchase_columns = [
    "NumWebPurchases",
    "NumStorePurchases",
    "NumCatalogPurchases",
    "NumDealsPurchases",
]

for row in rows:
    row["Age"] = 2014 - int(row["Year_Birth"])
    row["Total_Spend"] = sum(int(row[column]) for column in spending_columns)
    row["Total_Purchases"] = sum(int(row[column]) for column in purchase_columns)
    row["Children"] = int(row["Kidhome"]) + int(row["Teenhome"])

new_columns = original_columns + [
    "Age",
    "Total_Spend",
    "Total_Purchases",
    "Children",
]

with open(output_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=new_columns)
    writer.writeheader()
    writer.writerows(rows)

print("Saved", len(rows), "customers to", output_file)