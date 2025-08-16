# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
# For demonstration, we'll use the built-in seaborn 'tips' dataset via URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# Display first few rows
print("📄 First 5 rows of the dataset:")
print(df.head())

# Basic info and summary
print("\n📊 Dataset Info:")
print(df.info())

print("\n📈 Summary Statistics:")
print(df.describe())

# Check for missing values
print("\n🔍 Missing Values:")
print(df.isnull().sum())

# Value counts for categorical column
print("\n👥 Gender Distribution:")
print(df['sex'].value_counts())

# Visualization 1: Histogram of total bill
plt.figure(figsize=(8, 5))
plt.hist(df['total_bill'], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill ($)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()

# Visualization 2: Scatter plot of total bill vs tip
plt.figure(figsize=(8, 5))
plt.scatter(df['total_bill'], df['tip'], alpha=0.7, color='green')
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Visualization 3: Bar chart of average tip by day
avg_tip_by_day = df.groupby('day')['tip'].mean()
avg_tip_by_day.plot(kind='bar', color='coral', figsize=(8, 5))
plt.title("Average Tip by Day")
plt.xlabel("Day of Week")
plt.ylabel("Average Tip ($)")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Findings
print("\n📌 Observations:")
print("- Most total bills fall between $10 and $20.")
print("- There's a positive correlation between total bill and tip amount.")
print("- Saturday and Sunday have higher average tips compared to other days.")