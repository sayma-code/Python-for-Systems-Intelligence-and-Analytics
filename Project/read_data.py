import tabula
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# -----------------------------
# LOAD & CLEAN ALL DATA SOURCES
# -----------------------------

# PDF data
pdf_path = "air.pdf"
df_pdf = tabula.read_pdf(pdf_path, pages="all", multiple_tables=False)[0] # Please install java on your system to use tabula-py
df_pdf.columns = df_pdf.columns.str.lower()
df_pdf["country"] = df_pdf["country"].str.lower().str.strip().str.replace(r"[^a-z]", "", regex=True)
df_pdf = df_pdf.drop(columns=["pm2.5", "pm10", "code"], errors="ignore")
df_pdf["year"] = pd.to_numeric(df_pdf["year"], errors="coerce")
df_pdf = df_pdf[(df_pdf["year"] >= 2000) & (df_pdf["year"] <= 2025)]
df_pdf["year"] = df_pdf["year"].astype(str)

# API data (WHO)
mydb1 = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="health_data"
)
df_who = pd.read_sql("SELECT * FROM child_mortality", mydb1)
df_who["country"] = df_who["country"].str.lower().str.strip().str.replace(r"[^a-z]", "", regex=True)
df_who["year"] = df_who["year"].astype(str)
df_who = df_who.drop(columns=["country_code"], errors="ignore")

df_merged = df_who.merge(df_pdf, on=["country", "year"], how="left")

# Excel data (World Bank)
df_money = pd.read_excel("money.xlsx")
df_money = df_money.rename(columns={"date": "year", "country_name": "country"})
df_money["year"] = df_money["year"].astype(str)
df_money["country"] = df_money["country"].str.lower().str.strip().str.replace(r"[^a-z]", "", regex=True)
df_money = df_money.drop(columns=["country_code"], errors="ignore")

df_second_merge = df_merged.merge(
    df_money[["country", "year", "gdp_per_capita", "health_expenditure_pct_gdp"]],
    on=["country", "year"],
    how="left"
)

# CSV data (AQI)
df_aqi = pd.read_csv("data_date.csv")
df_aqi["year"] = pd.to_datetime(df_aqi["Date"]).dt.year.astype(str)
df_aqi = df_aqi.rename(columns={"Country": "country", "AQI Value": "AQI_Value"})
df_aqi["country"] = df_aqi["country"].str.lower().str.strip().str.replace(r"[^a-z]", "", regex=True)
df_aqi = df_aqi[["country", "year", "Status", "AQI_Value"]]

df_final = df_second_merge.merge(df_aqi, on=["country", "year"], how="left")

# -----------------------------
# CLEANING FOR ANALYSIS
# -----------------------------

numeric_cols = [
    "child_mortality_rate",
    "popdensity",
    "literacy",
    "gdp_per_capita",
    "health_expenditure_pct_gdp",
    "AQI_Value"
]

for col in numeric_cols:
    df_final[col] = pd.to_numeric(df_final[col], errors="coerce")
    df_final[col] = df_final.groupby("country")[col].transform(lambda x: x.fillna(x.mean()))

df_final[numeric_cols] = df_final[numeric_cols].fillna(df_final[numeric_cols].median())
df_final["Status"] = df_final["Status"].fillna("Unknown")

df_final.to_excel("final_health_dataset.xlsx", index=False)

# -----------------------------
# DESCRIPTIVE ANALYTICS
# -----------------------------

print(df_final.describe())


# -----------------------------
# PREDICTIVE ANALYTICS
# -----------------------------

X = df_final[[
    "popdensity",
    "literacy",
    "gdp_per_capita",
    "health_expenditure_pct_gdp",
    "AQI_Value"
]]
y = df_final["child_mortality_rate"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))

future_input = np.array([[50, 90, 15000, 7, 60]])
print("Predicted child mortality for 2026:", model.predict(future_input)[0])

# -----------------------------
# PRESCRIPTIVE ANALYTICS
# -----------------------------

target_reduction = 0.10
current_avg = df_final["child_mortality_rate"].mean()
target_value = current_avg * (1 - target_reduction)

coeffs = pd.Series(model.coef_, index=X.columns)
required_change = (target_value - model.intercept_) / coeffs["health_expenditure_pct_gdp"]

print("Current avg mortality:", current_avg)
print("Target mortality:", target_value)
print("Required health expenditure level:", required_change)

# -----------------------------
# KPI CALCULATIONS
# -----------------------------

kpis = {
    "avg_child_mortality_rate": df_final["child_mortality_rate"].mean(),
    "avg_aqi": df_final["AQI_Value"].mean(),
    "avg_gdp_per_capita": df_final["gdp_per_capita"].mean(),
    "avg_literacy_rate": df_final["literacy"].mean(),
    "avg_health_expenditure_pct_gdp": df_final["health_expenditure_pct_gdp"].mean()
}

pd.DataFrame([kpis]).to_csv("kpis.csv", index=False)
print("KPIs saved to kpis.csv")


#trend
plt.figure(figsize=(10,5))
df_final.groupby("year")["child_mortality_rate"].mean().plot()
plt.title("Trend: Child Mortality Rate (2000–2025)")
plt.xlabel("Year") 
plt.ylabel("Mortality Rate")
plt.grid(True)
plt.savefig("Project/plots/trend_child_mortality.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10,5))
df_final.groupby("child_mortality_rate")["gdp_per_capita"].mean().plot()
plt.title("Trend: GDP per Capita (2000–2025)")
plt.xlabel("Child Mortality Rate")
plt.ylabel("GDP per Capita")
plt.grid(True)
plt.savefig("Project/plots/trend_gdp.png", dpi=300, bbox_inches="tight")
plt.close()


plt.figure(figsize=(10,5))
df_final.groupby("child_mortality_rate")["AQI_Value"].mean().plot()
plt.title("Trend: AQI Levels (2000–2025)")
plt.xlabel("Child Mortality Rate")
plt.ylabel("AQI")
plt.grid(True)
plt.savefig("Project/plots/trend_aqi.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10,5))
df_final.groupby("child_mortality_rate")["literacy"].mean().plot()
plt.title("Trend: Literacy Rate (2000–2025)")
plt.xlabel("Child Mortality Rate")
plt.ylabel("Literacy Rate")
plt.grid(True)
plt.savefig("Project/plots/trend_literacy.png", dpi=300, bbox_inches="tight")
plt.close()


plt.figure(figsize=(10,6))
sns.heatmap(df_final[[
    "child_mortality_rate",
    "popdensity",
    "literacy",
    "gdp_per_capita",
    "health_expenditure_pct_gdp",
    "AQI_Value"
]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("Project/plots/correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(8,5))
sns.scatterplot(data=df_final, x="gdp_per_capita", y="child_mortality_rate")
plt.title("GDP per Capita vs Child Mortality Rate")
plt.xlabel("GDP per Capita")
plt.ylabel("Child Mortality Rate")
plt.savefig("Project/plots/gdp_child_mortality.png", dpi=300, bbox_inches="tight")
plt.close()


plt.figure(figsize=(8,5))
sns.scatterplot(data=df_final, x="literacy", y="child_mortality_rate", color="green")
plt.title("Literacy Rate vs Child Mortality Rate")
plt.xlabel("Literacy Rate")
plt.ylabel("Child Mortality Rate")
plt.savefig("Project/plots/literacy_child_mortality.png", dpi=300, bbox_inches="tight")
plt.close()


# -----------------------------
# Benchmarking: Compare with WHO data

print("Benchmarking:")
print("WHO Global Child Mortality Benchmark: ~37 per 1000")
print("Dataset Average Child Mortality:", df_final["child_mortality_rate"].mean())

print("WHO Safe AQI Benchmark: < 50")
print("Dataset Average AQI:", df_final["AQI_Value"].mean())

print("OECD GDP per Capita Benchmark: ~45000 USD")
print("Dataset Average GDP per Capita:", df_final["gdp_per_capita"].mean())

print("Child mortality in my dataset is better than the global average, but some countries still need improvement. AQI levels are worse than WHO recommendations, indicating environmental risks. GDP per capita is below OECD levels, explaining why some health indicators lag behind. To improve the topic, countries should focus on increasing health expenditure, improving literacy, reducing air pollution, and strengthening economic development.")

