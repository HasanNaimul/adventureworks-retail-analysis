import pandas as pd
import matplotlib.pyplot as plt

# Export the result of 05_store_duration_vs_revenue.sql to a CSV file, then update the path below.
file_path = "question5.csv"

revenue_vs_duration = pd.read_csv(file_path, sep="\t")

revenue_vs_duration.boxplot(
    column="store_duration_years",
    by="AnnualRevenue",
    rot=45
)

plt.title("Store Duration by Revenue Band")
plt.suptitle("")
plt.xlabel("Annual Revenue")
plt.ylabel("Store Duration (Years)")
plt.tight_layout()
plt.show()
