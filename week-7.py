# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset with error handling
try:
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
    missing = df.isnull().sum()
    print(missing)

    if missing.any():
        print("⚠️ Missing values detected. Filling with default values.")
        df.fillna(0, inplace=True)

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

    # Visualization 4: Line chart of average total bill by day
    avg_bill_by_day = df.groupby('day')['total_bill'].mean().sort_index()

    plt.figure(figsize=(8, 5))
    plt.plot(avg_bill_by_day.index, avg_bill_by_day.values, marker='o', linestyle='-', color='blue')
    plt.title("Average Total Bill by Day")
    plt.xlabel("Day of Week")
    plt.ylabel("Average Total Bill ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Pie chart of smoker vs non-smoker
    smoker_counts = df['smoker'].value_counts()

    plt.figure(figsize=(6, 6))
    plt.pie(smoker_counts, labels=smoker_counts.index, autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#ff9999'])
    plt.title("Proportion of Smokers")
    plt.axis('equal')  # Ensures pie is a circle
    plt.tight_layout()
    plt.show()

    # Pair plot of numerical features
    sns.pairplot(df[['total_bill', 'tip', 'size']], diag_kind='kde', corner=True)
    plt.suptitle("Pair Plot of Total Bill, Tip, and Size", y=1.02)
    plt.show()

    # Heatmap of correlations
    plt.figure(figsize=(8, 6))
    corr_matrix = df[['total_bill', 'tip', 'size']].corr()

    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

    # Findings
    print("\n📌 Observations:")
    print("- Most total bills fall between $10 and $20.")
    print("- There's a positive correlation between total bill and tip amount.")
    print("- Saturday and Sunday have higher average tips compared to other days.")

except FileNotFoundError:
    print("❌ Error: Dataset file not found. Please check the URL or file path.")
except pd.errors.ParserError:
    print("❌ Error: Failed to parse the dataset. Please check the file format.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")