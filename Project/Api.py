import requests
import pandas as pd
import mysql.connector

# -----------------------------------
# 1. Connect to MySQL
# -----------------------------------
mydb1 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)
mycursor1 = mydb1.cursor(buffered=True)
mycursor1.execute("DROP DATABASE IF EXISTS health_data;")
mycursor1.execute("CREATE DATABASE health_data")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="health_data"
)

mycursor = mydb.cursor(buffered=True)

# -----------------------------------
# 2. Fetch World Bank Child Mortality API
# -----------------------------------
url = "https://api.worldbank.org/v2/country/all/indicator/SH.DYN.MORT?format=json&per_page=20000"
response = requests.get(url).json()
records = response[1]

# Convert to DataFrame
df_child = pd.DataFrame([{
    "country": rec["country"]["value"],
    "country_code": rec["country"]["id"],
    "year": rec["date"],
    "child_mortality_rate": rec["value"]
} for rec in records])

# Convert year to numeric
df_child["year"] = pd.to_numeric(df_child["year"], errors="coerce")

# Filter years 2000–2025
df_child = df_child[df_child["year"].between(2000, 2025)]

# Reset index
df_child = df_child.reset_index(drop=True)

# -----------------------------------
# 3. Create MySQL table for child mortality
# -----------------------------------
table_name = "child_mortality"

mycursor.execute(f"DROP TABLE IF EXISTS {table_name}")
mycursor.execute(f"""
CREATE TABLE {table_name} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_code TEXT,
    country TEXT,
    year INT,
    child_mortality_rate FLOAT
)
""")

# -----------------------------------
# 4. Insert data into MySQL
# -----------------------------------
for _, row in df_child.iterrows():
    mycursor.execute(f"""
        INSERT INTO {table_name}
        (country_code, country, year, child_mortality_rate)
        VALUES (%s, %s, %s, %s)
    """, (
        row["country_code"],
        row["country"],
        int(row["year"]),
        row["child_mortality_rate"]
    ))

mydb.commit()

print("Child mortality data saved into MySQL database 'health_data' successfully.")
