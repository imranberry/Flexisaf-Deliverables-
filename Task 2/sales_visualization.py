import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
data = pd.read_csv("company_sales_data.csv")

# Displaying first few rows
print(data.head())

# Extract months and total profit
months = data['month_number']
total_profit = data['total_profit']

# line graph Plot
plt.plot(months, total_profit, marker='o', color='g', linewidth=2)

# Adding labels and title
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.title("Company Profit per Month")
plt.grid(True)
plt.show()

# Extract data
bathing_soap = data['bathingsoap']
facewash = data['facewash']

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

# Bathing Soap sales Plot
ax1.plot(months, bathing_soap, marker='o', color='b')
ax1.set_title("Bathing Soap Sales")
ax1.set_ylabel("Units Sold")
ax1.grid(True)

# Facewash sales Plot
ax2.plot(months, facewash, marker='o', color='r')
ax2.set_title("Facewash Sales")
ax2.set_xlabel("Month Number")
ax2.set_ylabel("Units Sold")
ax2.grid(True)

# Adjust layout
plt.tight_layout()
plt.show()