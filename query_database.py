import sqlite3

with sqlite3.connect("marketing_campaign.db") as connection:
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            Marital_Status,
            COUNT(*) AS customers,
            SUM(Response) AS responders,
            ROUND(100.0 * SUM(Response) / COUNT(*), 2) AS response_rate,
            ROUND(AVG(Total_Spend), 2) AS average_spend
        FROM customers
        GROUP BY Marital_Status
        ORDER BY response_rate DESC
    """)

    results = cursor.fetchall()

for row in results:
    print(
        row[0],
        "| customers:", row[1],
        "| responders:", row[2],
        "| response rate:", row[3], "%",
        "| average spend:", row[4]
    )