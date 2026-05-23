Exploratory Data Analysis — E-Commerce Sales Datase
Prepared by Haadiya Farhan | DecodeLabs Internship 2026 | Project 2

---
What This Project Is About

This project performs an Exploratory Data Analysis on a cleaned e-commerce sales dataset containing 1,200 orders and 14 columns. The goal was to understand customer purchasing behavior, identify revenue trends, detect outliers, and surface business insights using Python.
---

Files in This Repository

EDA.py — the main Python script that runs the full analysis

Cleaned_Dataset.xlsx — the dataset used for this project

EDA_Report.pdf — the final report with all findings, charts, and business recommendations

---
What the Analysis Covers

The script performs the following steps in order:

Descriptive Statistics — mean, median, count, and standard deviation for all numerical columns

Trend Analysis — monthly sales grouped by date to identify seasonal patterns

Distribution Analysis — histogram of TotalPrice to understand data shape and skewness

Outlier Detection — IQR method to find unusually high or low transactions, visualized with a box plot

Correlation Analysis — Pearson correlation matrix across all numerical variables, visualized with a heatmap

Skewness Analysis — skewness values for each numerical column

---

Key Findings

June 2024 was the highest revenue month at $68,069. A recurring mid-year sales peak was observed across 2023 and 2024, suggesting a seasonal pattern.

UnitPrice is the strongest driver of TotalPrice with a correlation of 0.717. Higher priced products directly lead to higher order values.

41.4% of orders were either cancelled or returned, which is the most critical risk identified in this dataset.

TotalPrice is right-skewed with a skewness of 0.891. The median ($823.62) is a more accurate representation of typical customer spend than the mean ($1,053.97).

Instagram is the top customer acquisition channel with 259 orders, followed closely by Email at 250.

Chair and Printer are the top revenue-generating products at approximately $195,000 each.

---

How to Run

Make sure you have Python installed along with the following libraries:

pandas, matplotlib, seaborn, openpyxl

Install them with this command:

```
pip install pandas matplotlib seaborn 
```

Then update the file path in EDA.py to point to your local copy of Cleaned_Dataset.xlsx and run:

```
python EDA.py
```

---

Tools Used

Python 3, Pandas, Matplotlib, Seaborn