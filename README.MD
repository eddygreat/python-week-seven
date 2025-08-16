# 📊 Data Analysis Assignment

## 🎯 Objective

This assignment demonstrates how to:
- Load and explore a dataset using **pandas**
- Perform basic data analysis
- Visualize data using **matplotlib**

---

## 📁 Dataset

We use the **Tips** dataset from the Seaborn library, which contains information about restaurant bills, tips, and customer demographics.

📦 **Source**: [Seaborn GitHub Repository](https://github.com/mwaskom/seaborn-data)

---

## 🧪 Analysis Steps

### 1. Data Loading
- Loaded the dataset using `pandas.read_csv()`
- Displayed the first few rows

### 2. Data Exploration
- Checked data types and structure with `.info()`
- Generated summary statistics with `.describe()`
- Checked for missing values
- Analyzed categorical distributions (e.g., gender)

### 3. Visualizations
- **Histogram** of total bill amounts
- **Scatter plot** of total bill vs tip
- **Bar chart** of average tip by day

---

## 📌 Observations

- Most total bills fall between **$10 and $20**
- There's a **positive correlation** between total bill and tip amount
- **Saturday and Sunday** show higher average tips than other days

---

## 🚀 How to Run

### Requirements

Install required libraries:

```bash
pip install pandas matplotlib


## To run script use 
 python week-7.py