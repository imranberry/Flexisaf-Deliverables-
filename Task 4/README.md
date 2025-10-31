# Week 4: Data Visualization with Matplotlib and Seaborn

## Overview

This week’s deliverable focuses on **data visualization** using Python’s powerful libraries — **Matplotlib** and **Seaborn**.
The goal is to create different types of plots that help interpret and understand the structure and patterns in the dataset.

The dataset used here is the classic **Iris dataset**, which contains sepal and petal measurements for three species of iris flowers.

## Objectives

1. Create a **Line Plot** and **Scatter Plot** using Matplotlib.
2. Visualize data distributions using **Histograms** and **Box Plots** with Seaborn.
3. Demonstrate an understanding of how data visualization can reveal trends, relationships, and outliers.


## Tools and Libraries

* **Python 3.13**
* **Pandas** – for data manipulation and loading
* **Matplotlib** – for basic visualizations (line and scatter plots)
* **Seaborn** – for advanced statistical plots (histograms and box plots)

To install required packages:

bash
pip install pandas matplotlib seaborn

## Dataset

The project uses the [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris), which includes:

* **SepalLengthCm**
* **SepalWidthCm**
* **PetalLengthCm**
* **PetalWidthCm**
* **Species**

Make sure `iris.csv` is saved in the same folder as this script:

Task 4/
 ├── Deliverable4_visualization.py
 ├── iris.csv
 └── README.md

## Visualizations Created

### 1. Line Plot

Displays the trend of **Sepal Length** and **Sepal Width** across all samples.

```python
plt.plot(data["SepalLengthCm"], label="Sepal Length")
plt.plot(data["SepalWidthCm"], label="Sepal Width")
```

### 2. Scatter Plot

Shows the relationship between **Petal Length** and **Petal Width**.

```python
plt.scatter(data["PetalLengthCm"], data["PetalWidthCm"], c='purple')
```

### 3. Histogram

Illustrates the frequency distribution of **Sepal Length**.

```python
sns.histplot(data["SepalLengthCm"], bins=20, kde=True)
```

### 4. Box Plot

Compares **Petal Length** across the three **Species**.

```python
sns.boxplot(x="Species", y="PetalLengthCm", data=data)

## Results Summary

* The **line plot** shows variation in sepal measurements between samples.
* The **scatter plot** highlights the clear correlation between petal length and width.
* The **histogram** demonstrates how most flowers have mid-range sepal lengths.
* The **box plot** shows that *Iris setosa* generally has shorter petals, while *Iris virginica* has the longest.

## How to Run

1. Open the project folder in **VS Code**.
2. Run the script:

   ```bash
   python Deliverable4_visualization.py
   ```
3. The visualizations will open in separate plot windows.


## Author

**Malik Imran**
Data Science and Generative AI Intern – Task 4 Submission
