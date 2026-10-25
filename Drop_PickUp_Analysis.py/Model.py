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
file_path = r"C:\Users\ARYAN MAHAKUR\Downloads\LPU_Transportation_Master_Dataset_10000 (1).xlsx"
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
# 5. SAVE MODEL TO PKL FILE (Explicit Path)
# ============================================================
script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()
output_filename = os.path.join(script_dir, "demand_prediction_pipeline.pkl")

joblib.dump(model_pipeline, output_filename)
print(f"\n[✔] Pipeline successfully saved to: {output_filename}")
print("=" * 60)

# ============================================================
# 6. 10-POINT COMPREHENSIVE PICKUP, DROP & OPERATIONAL ANALYSIS
# ============================================================
print("\n" + "="*50)
print("     COMPREHENSIVE 10-POINT TRANSPORTATION ANALYSIS")
print("="*50)

# 1. Top Pickup Hotspots
print("\n[Analysis 1] Top 5 Pickup Hotspots")
analysis_1 = (
    df.groupby(["Pickup_Block", "Pickup_Location_Name", "Pickup_Location_Type"])
    .agg(Total_Trips=("Passengers", "count"), Total_Passengers=("Passengers", "sum"), Avg_Passengers=("Passengers", "mean"))
    .reset_index()
    .sort_values(by="Total_Passengers", ascending=False)
)
print(analysis_1.head(5).to_string(index=False))
analysis_1.to_csv("analysis_1_pickup_hotspots.csv", index=False)

# 2. Top Drop-off Hotspots
print("\n[Analysis 2] Top 5 Drop-off Hotspots")
analysis_2 = (
    df.groupby(["Drop_Block", "Drop_Location_Name", "Drop_Location_Type"])
    .agg(Total_Trips=("Passengers", "count"), Total_Passengers=("Passengers", "sum"), Avg_Passengers=("Passengers", "mean"))
    .reset_index()
    .sort_values(by="Total_Passengers", ascending=False)
)
print(analysis_2.head(5).to_string(index=False))
analysis_2.to_csv("analysis_2_drop_hotspots.csv", index=False)

# 3. Busiest Origin-Destination Routes
print("\n[Analysis 3] Top 5 Busiest Routes (Origin → Destination)")
analysis_3 = (
    df.groupby("Route")
    .agg(Trips=("Passengers", "count"), Total_Passengers=("Passengers", "sum"), Avg_Travel_Time_Min=("Travel_Time_Min", "mean"), Avg_Distance_m=("Distance_m", "mean"))
    .reset_index()
    .sort_values(by="Total_Passengers", ascending=False)
)
print(analysis_3.head(5).to_string(index=False))
analysis_3.to_csv("analysis_3_busiest_routes.csv", index=False)

# 4. Peak Hour vs Off-Peak Comparison
print("\n[Analysis 4] Peak Hour vs Off-Peak Transit Metrics")
analysis_4 = (
    df.groupby("Peak_Hour")
    .agg(Total_Trips=("Passengers", "count"), Avg_Passengers_Per_Trip=("Passengers", "mean"), Avg_Travel_Time_Min=("Travel_Time_Min", "mean"), Avg_Utilization_Pct=("Vehicle_Utilization_Percent", "mean"))
    .reset_index()
)
print(analysis_4.to_string(index=False))
analysis_4.to_csv("analysis_4_peak_vs_offpeak.csv", index=False)

# 5. Hourly Passenger Demand Trends
print("\n[Analysis 5] Hourly Passenger Demand Distribution")
analysis_5 = (
    df.groupby("Hour")
    .agg(Total_Trips=("Passengers", "count"), Total_Passengers=("Passengers", "sum"), Avg_Passengers_Per_Trip=("Passengers", "mean"))
    .reset_index()
    .sort_values(by="Hour")
)
print(analysis_5.to_string(index=False))
analysis_5.to_csv("analysis_5_hourly_demand.csv", index=False)

# 6. Day of the Week Passenger Analysis
print("\n[Analysis 6] Passenger Demand by Day of the Week")
analysis_6 = (
    df.groupby("Day_of_Week")
    .agg(Total_Trips=("Passengers", "count"), Total_Passengers=("Passengers", "sum"), Avg_Passengers_Per_Trip=("Passengers", "mean"))
    .reset_index()
)
print(analysis_6.to_string(index=False))
analysis_6.to_csv("analysis_6_weekday_trends.csv", index=False)

# 7. Traffic Level Impact on Travel Time & Passengers
print("\n[Analysis 7] Traffic Level Impact Analysis")
analysis_7 = (
    df.groupby("Traffic_Level")
    .agg(Total_Trips=("Passengers", "count"), Avg_Passengers=("Passengers", "mean"), Avg_Travel_Time_Min=("Travel_Time_Min", "mean"))
    .reset_index()
)
print(analysis_7.to_string(index=False))
analysis_7.to_csv("analysis_7_traffic_impact.csv", index=False)

# 8. Weather Condition Impact on Demand
print("\n[Analysis 8] Weather Condition Impact Analysis")
analysis_8 = (
    df.groupby("Weather")
    .agg(Total_Trips=("Passengers", "count"), Avg_Passengers=("Passengers", "mean"), Avg_Travel_Time_Min=("Travel_Time_Min", "mean"))
    .reset_index()
)
print(analysis_8.to_string(index=False))
analysis_8.to_csv("analysis_8_weather_impact.csv", index=False)

# 9. Location Type Breakdown (Academic, Hostel, etc.)
print("\n[Analysis 9] Pickup Location Type Distribution")
analysis_9 = (
    df.groupby("Pickup_Location_Type")
    .agg(Total_Trips=("Passengers", "count"), Total_Passengers=("Passengers", "sum"), Avg_Passengers_Per_Trip=("Passengers", "mean"))
    .reset_index()
    .sort_values(by="Total_Passengers", ascending=False)
)
print(analysis_9.to_string(index=False))
analysis_9.to_csv("analysis_9_location_types.csv", index=False)

# 10. Vehicle Capacity & Utilization Efficiency
print("\n[Analysis 10] Vehicle Capacity & Utilization Summary")
analysis_10 = (
    df.groupby("Vehicle_Capacity")
    .agg(Total_Trips=("Passengers", "count"), Avg_Passengers_Carried=("Passengers", "mean"), Avg_Utilization_Pct=("Vehicle_Utilization_Percent", "mean"))
    .reset_index()
)
print(analysis_10.to_string(index=False))
analysis_10.to_csv("analysis_10_vehicle_utilization.csv", index=False)

print("\n" + "="*60)
print("[✔] All 10 analytical reports successfully computed and exported to CSV!")
print("="*60)