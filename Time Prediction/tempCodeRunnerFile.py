
import joblib
import pandas as pd

# ============================================================
# 1. CONFIGURATION
# ============================================================

DATA_FILE = (
    r"C:\Users\ARYAN MAHAKUR\Desktop\VS CODE"
    r"\INT395-CA1-PROJECT\lpu_travel_time_model.pkl"
)

# ============================================================
# 2. LOAD SAVED DISTANCE AND TRAVEL TIME MATRICES
# ============================================================

print("Loading travel-time data...")

data = joblib.load(DATA_FILE)

distance_matrix = data["distance_matrix"]
travel_time_matrix = data["travel_time_matrix"]

print("Travel-time data loaded successfully.")

# ============================================================
# 3. CREATE NUMBERED LOCATION OPTIONS
# ============================================================

locations = list(distance_matrix.index)

# Map option numbers to actual block IDs
location_options = {
    i + 1: location
    for i, location in enumerate(locations)
}

# ============================================================
# 4. DISPLAY ALL AVAILABLE LOCATIONS
# ============================================================

def display_locations():
    print("\n========== AVAILABLE LOCATIONS ==========")

    for number, location in location_options.items():
        print(f"{number}. {location}")

    print("=========================================")


# ============================================================
# 5. GET PICKUP AND DROP INPUT
# ============================================================

display_locations()

try:
    pickup_number = int(input("\nEnter pickup location number: "))
    drop_number = int(input("Enter drop location number: "))

    if pickup_number not in location_options:
        print("\nError: Invalid pickup option.")

    elif drop_number not in location_options:
        print("\nError: Invalid drop option.")

    else:
        pickup = location_options[pickup_number]
        drop = location_options[drop_number]

        # ================================================
        # 6. GET DISTANCE AND TRAVEL TIME
        # ================================================

        distance = distance_matrix.loc[pickup, drop]
        travel_time = travel_time_matrix.loc[pickup, drop]

        if pd.isna(distance) or pd.isna(travel_time):
            print("\nError: Distance or travel time is unavailable.")

        elif distance < 0 or travel_time < 0:
            print("\nError: Invalid distance or travel time.")

        else:
            # ============================================
            # 7. DISPLAY RESULT
            # ============================================

            print("\n========== TRAVEL TIME RESULT ==========")
            print(f"Pickup Location: {pickup}")
            print(f"Drop Location: {drop}")
            print(f"Distance: {distance:.2f} meters")
            print(f"Distance: {distance / 1000:.3f} km")
            print(f"Estimated Travel Time: {travel_time:.2f} minutes")
            print("========================================")

except ValueError:
    print("\nError: Please enter valid numbers only.")
