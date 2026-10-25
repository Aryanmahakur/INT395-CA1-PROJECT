import os
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ============================================================
# 1. LOAD DATASET
# ============================================================
file_path = "LPU_Transportation_Master_Dataset_10000.xlsx"
if not os.path.exists(file_path):
  file_path = (
      r"C:\Users\ARYAN MAHAKUR\Downloads\LPU_Transportation_Master_Dataset_10000"
      " (1).xlsx"
  )

print("Loading dataset for location clustering & heatmaps...")
df = pd.read_excel(file_path, sheet_name="Ride Records")
print(f"Total Ride Records Loaded: {len(df)}")
print("=" * 60)

# ============================================================
# 2. AGGREGATE METRICS PER PICKUP LOCATION
# ============================================================
location_df = (
    df.groupby(
        ["Pickup_Block", "Pickup_Location_Name", "Pickup_Location_Type"]
    )
    .agg(
        Total_Trips=("Passengers", "count"),
        Total_Passengers=("Passengers", "sum"),
        Avg_Passengers_Per_Trip=("Passengers", "mean"),
        Avg_Distance_m=("Distance_m", "mean"),
        Avg_Travel_Time_Min=("Travel_Time_Min", "mean"),
    )
    .reset_index()
)

location_df.rename(
    columns={
        "Pickup_Block": "Block",
        "Pickup_Location_Name": "Location_Name",
        "Pickup_Location_Type": "Location_Type",
    },
    inplace=True,
)

print(f"Total Unique Locations Identified: {len(location_df)}")

# ============================================================
# 3. FEATURE SCALING & K-MEANS CLUSTERING
# ============================================================
features = [
    "Total_Trips",
    "Total_Passengers",
    "Avg_Passengers_Per_Trip",
    "Avg_Distance_m",
    "Avg_Travel_Time_Min",
]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(location_df[features])

# Apply K-Means with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
location_df["Cluster"] = kmeans.fit_predict(X_scaled)

# Map cluster IDs to descriptive operational names
cluster_means = (
    location_df.groupby("Cluster")["Total_Passengers"].mean().sort_values()
)
sorted_clusters = cluster_means.index.tolist()

cluster_labels = {
    sorted_clusters[0]: "Low-Demand / Peripheral Zone",
    sorted_clusters[1]: "Moderate Transit Hub",
    sorted_clusters[2]: "High-Density Core Hub",
}

location_df["Cluster_Name"] = location_df["Cluster"].map(cluster_labels)

# Display Cluster Summary in Console
print("\n========== CLUSTER SUMMARY BREAKDOWN ==========")
print(
    location_df[["Block", "Location_Name", "Total_Passengers", "Cluster_Name"]]
    .sort_values(by="Total_Passengers", ascending=False)
    .to_string(index=False)
)

# Export Clustered Data to CSV
location_df.to_csv("lpu_location_clusters.csv", index=False)
print(f"\n[✔] Location clustering results successfully exported to CSV.")

# ============================================================
# 4. GENERATE SCATTER PLOT
# ============================================================
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=location_df,
    x="Total_Trips",
    y="Total_Passengers",
    hue="Cluster_Name",
    style="Location_Type",
    s=120,
    palette="Set1",
)

plt.title(
    "LPU Campus Location Clustering (Trips vs Passenger Volume)",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Total Trips Generated", fontsize=12)
plt.ylabel("Total Passengers Carried", fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

plt.savefig("lpu_location_clusters_plot.png", dpi=300)
print(f"[✔] Cluster scatter plot saved successfully.")
plt.close()

# ============================================================
# 5. GENERATE LOCATION DEMAND HEATMAP
# ============================================================
plt.figure(figsize=(12, 8))

# Sort locations by total passengers for a cleaner heatmap view
heatmap_data = location_df.sort_values(
    by="Total_Passengers", ascending=False
).head(25)

# Set index to location name for heatmap matrix
matrix_data = heatmap_data.set_index("Location_Name")[
    [
        "Total_Trips",
        "Total_Passengers",
        "Avg_Passengers_Per_Trip",
        "Avg_Travel_Time_Min",
    ]
]

# Normalize columns for balanced heatmap color scaling
normalized_matrix = (matrix_data - matrix_data.min()) / (
    matrix_data.max() - matrix_data.min()
)

sns.heatmap(
    normalized_matrix,
    annot=matrix_data,
    fmt=".1f",
    cmap="YlOrRd",
    linewidths=0.5,
    cbar_kws={"label": "Normalized Intensity Scale (0 to 1)"},
)

plt.title(
    "Top 25 LPU Campus Locations - Demand Heatmap & Operational Metrics",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Performance Metrics", fontsize=12)
plt.ylabel("Campus Location Name", fontsize=12)
plt.xticks(rotation=20)
plt.tight_layout()

heatmap_filename = "lpu_demand_heatmap.png"
plt.savefig(heatmap_filename, dpi=300)
print(f"[✔] Location demand heatmap successfully saved to: {heatmap_filename}")
plt.show()