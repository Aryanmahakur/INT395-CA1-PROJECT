import os
import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# ============================================================
# 1. LOAD DATASET
# ============================================================
file_path = "LPU_Transportation_Master_Dataset_10000.xlsx"
if not os.path.exists(file_path):
    file_path = (
        r"C:\Users\ARYAN MAHAKUR\Downloads\LPU_Transportation_Master_Dataset_10000"
        " (1).xlsx"
    )

print("Loading dataset...")
df = pd.read_excel(file_path, sheet_name="Ride Records")

print(f"Total Ride Records Loaded: {len(df)}")
print(f"Dataset Shape: {df.shape}")
print("=" * 60)

# ============================================================
# 2. FEATURE ENGINEERING & DATA PREPROCESSING
# ============================================================
TARGET_COLUMN = "Passengers"

if TARGET_COLUMN not in df.columns:
    raise ValueError(f"Target column '{TARGET_COLUMN}' not found in dataset.")

# Drop target and any leakage or unnecessary columns
X = df.drop(
    columns=[TARGET_COLUMN, "Date", "Vehicle_Utilization_Percent", "Revenue_INR"],
    errors="ignore"
).copy()
y = df[TARGET_COLUMN].copy()

# Dynamically separate numerical and categorical features
numerical_cols = X.select_dtypes(include=["number"]).columns.tolist()
categorical_cols = X.select_dtypes(include=["object", "category", "string"]).columns.tolist()

print(f"\nNumerical Features ({len(numerical_cols)}): {numerical_cols}")
print(f"Categorical Features ({len(categorical_cols)}): {categorical_cols}")

# Preprocessing Pipelines
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numerical_cols),
        ("cat", categorical_transformer, categorical_cols)
    ],
    remainder="drop"
)

# ============================================================
# 3. BUILD MODEL PIPELINE & TRAIN
# ============================================================
model_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=150, max_depth=None, random_state=42, n_jobs=-1))
])

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nTraining Random Forest model on transportation data...")
model_pipeline.fit(X_train, y_train)

# ============================================================
# 4. EVALUATE MODEL PERFORMANCE
# ============================================================
train_preds = model_pipeline.predict(X_train)
test_preds = model_pipeline.predict(X_test)

print("\n========== MODEL EVALUATION RESULTS ==========")
print(f"Training R2 Score: {r2_score(y_train, train_preds):.4f}")
print(f"Testing R2 Score:  {r2_score(y_test, test_preds):.4f}")
print(f"Testing MAE:       {mean_absolute_error(y_test, test_preds):.4f}")
print(f"Testing RMSE:      {np.sqrt(mean_squared_error(y_test, test_preds)):.4f}")

# ============================================================
# 5. SAVE MODEL TO PKL FILE
# ============================================================
script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()
output_filename = os.path.join(script_dir, "demand_prediction_pipeline.pkl")

joblib.dump(model_pipeline, output_filename)
print(f"\n[✔] Pipeline successfully saved to: {output_filename}")
print("=" * 60)