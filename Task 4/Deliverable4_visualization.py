# Deliverable4_visualization.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("iris.csv")

# LINE PLOT
plt.figure(figsize=(8, 5))
plt.plot(data["SepalLengthCm"], label="Sepal Length", color='b')
plt.plot(data["SepalWidthCm"], label="Sepal Width", color='r')
plt.title("Line Plot of Sepal Length and Width")
plt.xlabel("Sample Index")
plt.ylabel("Measurement (cm)")
plt.legend()
plt.show()

# SCATTER PLOT
plt.figure(figsize=(6, 5))
plt.scatter(data["SepalLengthCm"], data["PetalLengthCm"], color='green')
plt.title("Scatter Plot: Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()

# HISTOGRAM (Seaborn) 
plt.figure(figsize=(6, 5))
sns.histplot(data["PetalLengthCm"], bins=20, kde=True, color='purple')
plt.title("Distribution of Petal Length")
plt.show()

# BOX PLOT (Seaborn)
plt.figure(figsize=(6, 5))
sns.boxplot(x="Species", y="PetalLengthCm", data=data)
plt.title("Box Plot of Petal Length by Species")
plt.show()

