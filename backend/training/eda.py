import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create results folder if it doesn't exist
os.makedirs("../results", exist_ok=True)

# Load dataset
df = pd.read_csv("../dataset/Crop_recommendation.csv")

print(df.head())

# Dataset information
print(df.info())

# Missing values
print(df.isnull().sum())

# Statistics
print(df.describe())

# -----------------------------
# Crop Distribution
# -----------------------------

plt.figure(figsize=(12,6))
sns.countplot(x="label", data=df)
plt.xticks(rotation=90)
plt.title("Crop Distribution")
plt.tight_layout()
plt.savefig("../results/crop_distribution.png")
plt.show()

# -----------------------------
# Correlation Heatmap
# -----------------------------

plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap="YlGnBu")

plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("../results/correlation_matrix.png")
plt.show()