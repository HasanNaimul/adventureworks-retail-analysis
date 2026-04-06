import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Export the result of 03_vacation_vs_bonus.sql to a CSV file, then update the path below.
file_path = "question2.csv"

df = pd.read_csv(file_path, sep="\t")
df["VacationHours"] = pd.to_numeric(df["VacationHours"], errors="coerce")
df["Bonus"] = pd.to_numeric(df["Bonus"], errors="coerce")
df = df.dropna()

corr = df["VacationHours"].corr(df["Bonus"])
print(f"Pearson correlation: {corr:.3f}")

plt.figure(figsize=(8, 6))
plt.scatter(df["VacationHours"], df["Bonus"])

x = df["VacationHours"].to_numpy()
y = df["Bonus"].to_numpy()
m, b = np.polyfit(x, y, 1)
x_line = np.linspace(x.min(), x.max(), 200)
y_line = m * x_line + b

plt.plot(x_line, y_line)
plt.title("Vacation Hours vs Bonus")
plt.xlabel("Vacation Hours")
plt.ylabel("Bonus")
plt.tight_layout()
plt.show()
