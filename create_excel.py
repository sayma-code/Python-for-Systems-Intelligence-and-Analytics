import requests
import pandas as pd

# ----------------------------------------------------
# 1. API URLs
# ----------------------------------------------------
gdp_url = "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.PCAP.CD?format=json&per_page=20000"
health_url = "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.CHEX.GD.ZS?format=json&per_page=20000"

# ----------------------------------------------------
# 2. Fetch GDP per capita
# ----------------------------------------------------
gdp_json = requests.get(gdp_url).json()
gdp_data = gdp_json[1]   # index 1 contains actual data

df_gdp = pd.DataFrame(gdp_data)

# Extract nested fields
df_gdp["country_name"] = df_gdp["country"].apply(lambda x: x["value"])
df_gdp["country_code"] = df_gdp["country"].apply(lambda x: x["id"])

# Keep only useful columns
df_gdp = df_gdp[["country_name", "country_code", "date", "value"]]
df_gdp = df_gdp.rename(columns={"value": "gdp_per_capita"})

# ----------------------------------------------------
# 3. Fetch Health Expenditure (% of GDP)
# ----------------------------------------------------
health_json = requests.get(health_url).json()
health_data = health_json[1]

df_health = pd.DataFrame(health_data)

# Extract nested fields
df_health["country_name"] = df_health["country"].apply(lambda x: x["value"])
df_health["country_code"] = df_health["country"].apply(lambda x: x["id"])

# Keep only useful columns
df_health = df_health[["country_name", "country_code", "date", "value"]]
df_health = df_health.rename(columns={"value": "health_expenditure_pct_gdp"})

# ----------------------------------------------------
# 4. Merge both datasets on country + year
# ----------------------------------------------------
df_merged = pd.merge(
    df_gdp,
    df_health,
    on=["country_name", "country_code", "date"],
    how="inner"
)

# ----------------------------------------------------
# 5. Save merged data into ONE Excel file, ONE sheet
# ----------------------------------------------------
df_merged.to_excel("merged_economic_health_data.xlsx", index=False)

print("Merged data saved to merged_economic_health_data.xlsx")
