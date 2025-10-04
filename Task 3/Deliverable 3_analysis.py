import pandas as pd

# Load dataset
data = pd.read_csv("iris.csv")

# Exploring the data
print("First 5 rows of the dataset:")
print(data.head(), "\n")

print("Data types of each column:")
print(data.info(), "\n")

print("Summary statistics:")
print(data.describe(include="all"), "\n")

# Basic Statistics
print("Mean of each numerical feature:")
print(data.mean(numeric_only=True), "\n")

print("Median of each numerical feature:")
print(data.median(numeric_only=True), "\n")

print("Standard deviation of each numerical feature:")
print(data.std(numeric_only=True), "\n")

print("Mode of each feature:")
print(data.mode().iloc[0], "\n")  # iloc[0] to get the first mode in case of multiple modes

print("Correlation between numerical features:")
print(data.corr(numeric_only=True), "\n")