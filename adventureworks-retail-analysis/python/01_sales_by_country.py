import pandas as pd
import matplotlib.pyplot as plt

# Export the result of 01_revenue_by_country.sql to a CSV file, then update the path below.
file_path = "question1_part1.csv"

sales_by_country = pd.read_csv(file_path, sep="\t")
sales_by_country = sales_by_country.set_index("country_name")

plt.figure(figsize=(10, 6))
plt.bar(sales_by_country.index, sales_by_country["total_sales"])
plt.title("Sales YTD by Country")
plt.xlabel("Country")
plt.ylabel("Sales YTD")
plt.tight_layout()
plt.show()
