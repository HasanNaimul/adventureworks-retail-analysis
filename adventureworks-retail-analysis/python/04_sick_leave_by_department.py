import pandas as pd
import matplotlib.pyplot as plt

# Export the department-level result from 04_sick_leave_analysis.sql to CSV, then update the path below.
file_path = "avgsickleave.csv"

df = pd.read_csv(file_path, sep="\t")
df = df.set_index("Department")

plt.figure(figsize=(10, 6))
df["avg_sick_leave"].sort_values().plot(kind="barh")
plt.title("Average Sick Leave by Department")
plt.xlabel("Average Sick Leave Hours")
plt.ylabel("Department")
plt.tight_layout()
plt.show()
