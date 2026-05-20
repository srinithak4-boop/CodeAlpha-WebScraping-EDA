import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.switch_backend('Agg')

# Load dataset
df = pd.read_csv("books_data.csv")

# Show first 5 rows
print("\nFIRST 5 ROWS")
print(df.head())

# Dataset information
print("\nDATASET INFO")
print(df.info())

# Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Convert price column if needed
if 'price' in df.columns:
    df['price'] = df['price'].replace('[^0-9.]', '', regex=True).astype(float)

# -----------------------------
# PRICE DISTRIBUTION
# -----------------------------
if 'price' in df.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(df['price'], bins=20)
    plt.title("Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Count")
    plt.savefig("price_distribution.png")
    plt.show()

if 'rating' in df.columns:
    plt.figure(figsize=(8,5))
    sns.countplot(x='rating', data=df)
    plt.title("Rating Distribution")
    plt.savefig("rating_distribution.png")
    plt.show()

numeric_df = df.select_dtypes(include=['float64', 'int64'])

if not numeric_df.empty:
    plt.figure(figsize=(8,5))
    sns.heatmap(numeric_df.corr(), annot=True)
    plt.title("Correlation Heatmap")
    plt.savefig("heatmap.png")
    plt.show()

print("\nEDA COMPLETED SUCCESSFULLY")