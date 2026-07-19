import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("../dataset/Crop_recommendation.csv")

# -----------------------------
# Features and Target
# -----------------------------
X = df.drop("label", axis=1)
y = df["label"]

# -----------------------------
# Encode Crop Labels
# -----------------------------
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)

print("="*60)
print("DATA PREPROCESSING COMPLETED")
print("="*60)

print(f"\nTraining Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

print("\nFeatures")

print(X.columns.tolist())

print("\nCrop Classes")

print(label_encoder.classes_)