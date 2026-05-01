import requests
import pandas as pd

# ----------------------------------------------------
# 1. API URLs
# ----------------------------------------------------
pop_density_url = "https://api.worldbank.org/v2/country/all/indicator/EN.POP.DNST?format=json&per_page=20000"
literacy_url = "https://api.worldbank.org/v2/country/all/indicator/SE.ADT.LITR.FE.ZS?format=json&per_page=20000"

# Air quality API (example: Helsinki coordinates)
air_url = "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=60.17&longitude=24.94&hourly=pm10,pm2_5"

# ----------------------------------------------------
# 2. Fetch Population Density (World Bank)
# ----------------------------------------------------
pop_json = requests.get(pop_density_url).json()
pop_data = pop_json[1]

df_pop = pd.DataFrame(pop_data)

# Extract nested fields
df_pop["country_name"] = df_pop["country"].apply(lambda x: x["value"])
df_pop["country_code"] = df_pop["country"].apply(lambda x: x["id"])

df_pop = df_pop[["country_name", "country_code", "date", "value"]]
df_pop = df_pop.rename(columns={"value": "population_density"})

# ----------------------------------------------------
# 3. Fetch Female Literacy Rate (World Bank)
# ----------------------------------------------------
lit_json = requests.get(literacy_url).json()
lit_data = lit_json[1]

df_lit = pd.DataFrame(lit_data)

df_lit["country_name"] = df_lit["country"].apply(lambda x: x["value"])
df_lit["country_code"] = df_lit["country"].apply(lambda x: x["id"])

df_lit = df_lit[["country_name", "country_code", "date", "value"]]
df_lit = df_lit.rename(columns={"value": "female_literacy_rate"})

# ----------------------------------------------------
# 4. Fetch Air Quality (Open-Meteo)
# ----------------------------------------------------
air_json = requests.get(air_url).json()

df_air = pd.DataFrame({
    "date": air_json["hourly"]["time"],
    "pm10": air_json["hourly"]["pm10"],
    "pm2_5": air_json["hourly"]["pm2_5"]
})

# Add country info manually (Open-Meteo is coordinate-based)
df_air["country_name"] = "Finland"
df_air["country_code"] = "FIN"

# Extract year from timestamp
df_air["date"] = df_air["date"].str.slice(0, 4)

# Aggregate yearly average air quality
df_air = df_air.groupby(["country_name", "country_code", "date"]).mean().reset_index()

# ----------------------------------------------------
# 5. Merge all datasets
# ----------------------------------------------------
df_merged = df_pop.merge(
    df_lit,
    on=["country_name", "country_code", "date"],
    how="inner"
)

df_merged = df_merged.merge(
    df_air,
    on=["country_name", "country_code", "date"],
    how="left"
)

# ----------------------------------------------------
# 6. Save merged data to Excel (optional)
# ----------------------------------------------------
df_merged.to_excel("merged_population_air_literacy.xlsx", index=False)

print("Merged dataset created successfully.")
print(df_merged.head())
