import pandas as pd
import matplotlib.pyplot as plt

# Export the result of 02_us_regional_sales.sql to a CSV file, then update the path below.
file_path = "question1_part2.csv"

sales_us = pd.read_csv(file_path, sep="\t")
sales_us["sales_pct"] = sales_us["sales_ytd"] * 100 / sales_us["sales_ytd"].sum()

plt.figure(figsize=(10, 6))
plt.bar(sales_us["region_name"], sales_us["sales_pct"])
plt.title("Regional Sales Share in the US")
plt.xlabel("Region")
plt.ylabel("Sales Share (%)")
plt.tight_layout()
plt.show()
