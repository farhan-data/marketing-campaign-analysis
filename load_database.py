import csv
import sqlite3

input_file = "marketing_campaign_enriched.csv"
database_file = "marketing_campaign.db"

create_table_sql = """
CREATE TABLE customers (
    ID INTEGER PRIMARY KEY,
    Year_Birth INTEGER,
    Education TEXT,
    Marital_Status TEXT,
    Income REAL,
    Kidhome INTEGER,
    Teenhome INTEGER,
    Dt_Customer TEXT,
    Recency INTEGER,
    MntWines INTEGER,
    MntFruits INTEGER,
    MntMeatProducts INTEGER,
    MntFishProducts INTEGER,
    MntSweetProducts INTEGER,
    MntGoldProds INTEGER,
    NumDealsPurchases INTEGER,
    NumWebPurchases INTEGER,
    NumCatalogPurchases INTEGER,
    NumStorePurchases INTEGER,
    NumWebVisitsMonth INTEGER,
    AcceptedCmp3 INTEGER,
    AcceptedCmp4 INTEGER,
    AcceptedCmp5 INTEGER,
    AcceptedCmp1 INTEGER,
    AcceptedCmp2 INTEGER,
    Response INTEGER,
    Complain INTEGER,
    Country TEXT,
    Age INTEGER,
    Total_Spend INTEGER,
    Total_Purchases INTEGER,
    Children INTEGER
)
"""

with open(input_file, "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    columns = reader.fieldnames

    with sqlite3.connect(database_file) as connection:
        cursor = connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS customers")
        cursor.execute(create_table_sql)

        placeholders = ", ".join("?" for column in columns)
        column_names = ", ".join(columns)
        insert_sql = (
            f"INSERT INTO customers ({column_names}) "
            f"VALUES ({placeholders})"
        )

        customer_rows = (
            tuple(row[column] for column in columns)
            for row in reader
        )
        cursor.executemany(insert_sql, customer_rows)

        cursor.execute("SELECT COUNT(*) FROM customers")
        customer_count = cursor.fetchone()[0]

print("Customers loaded into database:", customer_count)