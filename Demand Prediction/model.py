

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor  # Switched to GBR
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# 1. Load Dataset
file_path = (
    r"C:\Users\ARYAN MAHAKUR\Downloads"
    r"\LPU_Campus_Demand_Prediction_Dataset_10000.xlsx"
)
TARGET_COLUMN = "Target_Passenger_Demand"

df = pd.read_excel(file_path)
df = df.drop_duplicates().reset_index(drop=True)

# DIAGNOSTIC: Print actual target stats to see if data itself is clustered between 40-50
print("--- ACTUAL TARGET STATISTICS IN EXCEL ---")
print(df[TARGET_COLUMN].describe())

X = df.drop(
    columns=[TARGET_COLUMN, "Target_Demand_Class", "Date"], errors="ignore"
).copy()
y = df[TARGET_COLUMN].copy()

# Convert booleans
for col in X.select_dtypes(include=["bool"]).columns:
  X[col] = X[col].astype(int)

numerical_cols = X.select_dtypes(include=["number"]).columns.tolist()
categorical_cols = X.select_dtypes(
    include=["object", "category", "string"]
).columns.tolist()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Preprocessing
numeric_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="median"))])
categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        (
            "onehot",
            OneHotEncoder(handle_unknown="ignore", sparse_output=False),
        ),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numerical_cols),
        ("cat", categorical_transformer, categorical_cols),
    ],
    remainder="drop",
)

# Gradient Boosting Regressor often captures feature sensitivity better than Random Forest
model_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "regressor",
            GradientBoostingRegressor(
                n_estimators=300,
                learning_rate=0.05,
                max_depth=5,
                random_state=42,
            ),
        ),
    ]
)

print("\nTraining Gradient Boosting model...")
model_pipeline.fit(X_train, y_train)

# Evaluate
test_predictions = model_pipeline.predict(X_test)
print(f"Test R2 Score: {r2_score(y_test, test_predictions):.4f}")
print(
    "Predicted Range on Test Set:"
    f" {test_predictions.min():.2f} to {test_predictions.max():.2f}"
)

# Save
joblib.dump(model_pipeline, "demand_prediction_pipeline.pkl")
print("\nPipeline saved successfully!")