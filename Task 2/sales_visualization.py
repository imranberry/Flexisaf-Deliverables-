import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
url = "https://pynative.com/wp-content/uploads/2019/01/company_sales_data.csv"
data = pd.read_csv(url)

# Display the first few rows (optional, just to see the data)
print(data.head())

# Extract months and total profit
months = data['month_number']
total_profit = data['total_profit']

# Plot line graph
plt.plot(months, total_profit, marker='o', color='g', linewidth=2)

# Add labels and title
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

# Plot Bathing Soap sales
ax1.plot(months, bathing_soap, marker='o', color='b')
ax1.set_title("Bathing Soap Sales")
ax1.set_ylabel("Units Sold")
ax1.grid(True)

# Plot Facewash sales
ax2.plot(months, facewash, marker='o', color='r')
ax2.set_title("Facewash Sales")
ax2.set_xlabel("Month Number")
ax2.set_ylabel("Units Sold")
ax2.grid(True)

# Adjust layout
plt.tight_layout()
plt.show()