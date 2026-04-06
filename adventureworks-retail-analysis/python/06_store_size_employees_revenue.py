import pandas as pd
import matplotlib.pyplot as plt

# Export the result of 06_store_size_employees_revenue.sql to a CSV file, then update the path below.
file_path = "q6.csv"

df = pd.read_csv(file_path)

corr = df[["AnnualRevenue", "SquareFeet", "NumberEmployees"]].corr()
print(corr)

df["RevenuePerEmployee"] = df["AnnualRevenue"] / df["NumberEmployees"]
df["RevenuePerSqFt"] = df["AnnualRevenue"] / df["SquareFeet"]

plt.figure(figsize=(9, 6))
scatter = plt.scatter(
    df["SquareFeet"],
    df["AnnualRevenue"],
    s=df["NumberEmployees"] * 8,
    c=df["NumberEmployees"],
    alpha=0.7
)
plt.colorbar(scatter, label="Number of Employees")
plt.title("Revenue vs Store Size")
plt.xlabel("Square Feet")
plt.ylabel("Annual Revenue")
plt.tight_layout()
plt.show()
