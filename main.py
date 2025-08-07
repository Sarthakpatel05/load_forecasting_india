import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv("/Users/sarthakpatel/python/load_forecasting_india/data/official_india_power_demand.csv")
print(df.head())

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="Year", y="Total_Consumption_BU", marker='o')
plt.title("Electricity Consumption in India (2013–2022)")
plt.ylabel("Total Consumption (Billion Units)")
plt.grid(True)
plt.tight_layout()
plt.savefig("consumption_trend.png")
plt.show()

X = df[["Year"]]
y = df["Total_Consumption_BU"]

model = LinearRegression()
model.fit(X, y)

future_years = pd.DataFrame({"Year": [2023, 2024, 2025]})
predictions = model.predict(future_years)

for year, pred in zip(future_years["Year"], predictions):
    print(f"Forecast for {year}: {pred:.2f} Billion Units")

future_df = pd.DataFrame({
    "Year": future_years["Year"],
    "Total_Consumption_BU": predictions
})

combined = pd.concat([df, future_df], ignore_index=True)

plt.figure(figsize=(10, 6))
sns.lineplot(data=combined, x="Year", y="Total_Consumption_BU", marker='o', label="Forecast")
plt.axvline(x=2022, color='red', linestyle='--', label='Forecast Begins')
plt.title("Forecast of Electricity Consumption in India (2013–2025)")
plt.ylabel("Total Consumption (BU)")
plt.legend()
plt.tight_layout()
plt.savefig("forecast.png")
plt.show()


df = pd.read_csv("/Users/sarthakpatel/python/load_forecasting_india/data/state_wise_consumption_2013_to_2022.csv")
df = df.drop_duplicates()

print(df.isnull().sum())

top_states = df.groupby("State")["Total_Consumption_BU"].sum().sort_values(ascending=False).head(5)
print(top_states)

top_states_list = top_states.index.tolist()
filtered_df = df[df['State'].isin(top_states_list)]

plt.figure(figsize=(12, 6))
sns.barplot(data=filtered_df, x='Year', y='Total_Consumption_BU', hue='State', dodge='True')
plt.title("Top 5 States by Electricity Consumption")
plt.xlabel("Year")
plt.ylabel("Consumption (BU)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

pivot_df = df.pivot(index='State', columns='Year', values='Total_Consumption_BU')
plt.figure(figsize=(16, 10))
sns.heatmap(pivot_df, cmap='YlGnBu')
plt.title("State-wise Electricity Consumption Heatmap")
plt.xlabel("Year")
plt.ylabel("State")
plt.tight_layout()
plt.show()

state_name = "Maharashtra"
state_data = df[df['State'] == state_name].sort_values(by="Year")

X = state_data["Year"].values.reshape(-1, 1)
y = state_data["Total_Consumption_BU"].values

model = LinearRegression()
model.fit(X, y)

future_years = np.array([[2023], [2024], [2025]])
predictions = model.predict(future_years)

for i, year in enumerate([2023, 2024, 2025]):
    print(year, ":", round(predictions[i], 2), "BU")

plt.figure(figsize=(8, 5))
plt.plot(X.flatten(), y, marker='o', label='Historical')
plt.plot(future_years.flatten(), predictions, marker='x', linestyle='--', color='red', label='Forecast')
plt.title(f"Electricity Forecast for {state_name}")
plt.xlabel("Year")
plt.ylabel("Consumption (BU)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

df_sector = pd.read_csv("/Users/sarthakpatel/python/load_forecasting_india/data/sector_wise_consumption_2013_to_2022.csv")

plt.figure(figsize=(12,6))
sns.lineplot(data=df_sector, x="Year", y="Consumption_BU", hue="Sector", marker="o")
plt.title("Electricity Consumption by Sector (2013–2022)")
plt.xlabel("Year")
plt.ylabel("Consumption (BU)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n----- Residential Sector Forecast (2023–2025) -----")

res_data = df_sector[df_sector["Sector"] == "Residential"]
X = res_data["Year"].values.reshape(-1, 1)
y = res_data["Consumption_BU"].values

model = LinearRegression()
model.fit(X, y)

future_years = np.array([[2023], [2024], [2025]])
predictions = model.predict(future_years)

for i, year in enumerate([2023, 2024, 2025]):
    print(year, "Residential Forecast:", round(predictions[i], 2), "BU")

df = pd.read_csv("/Users/sarthakpatel/python/load_forecasting_india/data/official_india_power_demand.csv")
df["Growth_Rate"] = df["Total_Consumption_BU"].pct_change() * 100
print(df)

plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["Growth_Rate"], marker='o')
plt.title("India Year-on-Year Electricity Growth Rate (%)")
plt.xlabel("Year")
plt.ylabel("Growth Rate (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

df = pd.read_csv("/Users/sarthakpatel/python/load_forecasting_india/data/state_wise_consumption_2013_to_2022.csv")
top_states = df.groupby("State")["Total_Consumption_BU"].sum().sort_values(ascending=False).head(5).index.tolist()
df_top = df[df["State"].isin(top_states)]
pivot_top = df_top.pivot(index="Year", columns="State", values="Total_Consumption_BU")
growth_top = pivot_top.pct_change() * 100

growth_top.plot(figsize=(12, 6), marker='o')
plt.title("Growth Rate of Top 5 States")
plt.xlabel("Year")
plt.ylabel("Growth Rate (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

df_sector = pd.read_csv("/Users/sarthakpatel/python/load_forecasting_india/data/sector_wise_consumption_2013_to_2022.csv")
pivot_sector = df_sector.pivot(index="Year", columns="Sector", values="Consumption_BU")
growth_sector = pivot_sector.pct_change() * 100

growth_sector.plot(figsize=(12, 6), marker='o')
plt.title("Sector-wise Electricity Growth Rate (%)")
plt.xlabel("Year")
plt.ylabel("Growth Rate (%)")
plt.grid(True)
plt.tight_layout()
plt.show()
