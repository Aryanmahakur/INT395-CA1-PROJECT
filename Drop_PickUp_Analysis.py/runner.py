from datetime import datetime
import os
import joblib
import pandas as pd


def load_model():
    """Loads the trained transport ML pipeline from the pkl file."""
    filename = "demand_prediction_pipeline.pkl"
    try:
        pipeline = joblib.load(filename)
        print(f"Model loaded successfully from {filename}\n")
        return pipeline
    except FileNotFoundError:
        print(
            f"Error: {filename} not found! Please make sure you ran your training script first to generate the pkl file."
        )
        return None


def load_dataset():
    """Loads the master dataset for contextual route analysis."""
    file_path = "LPU_Transportation_Master_Dataset_10000.xlsx"
    if not os.path.exists(file_path):
        # Fallback path if stored in downloads
        file_path = r"C:\Users\ARYAN MAHAKUR\Downloads\LPU_Transportation_Master_Dataset_10000 (1).xlsx"
    try:
        return pd.read_excel(file_path, sheet_name="Ride Records")
    except Exception:
        return None


def get_user_pickup_drop():
    """Takes only Pickup and Drop-off selections from the user across all LPU blocks."""
    print("=" * 65)
    print("      LPU CAMPUS PICKUP & DROP TRANSPORT PREDICTION SYSTEM      ")
    print("=" * 65)

    # Comprehensive LPU Campus Locations Dictionary matching the transport dataset
    locations = {
        1: {"ID": "1", "Name": "School of Fashion Design", "Type": "Academic"},
        2: {"ID": "2 / 02A", "Name": "Mini Auditorium", "Type": "Auditorium"},
        3: {
            "ID": "3 / 03A",
            "Name": "School of Paramedical Sciences / Electrical Works / DG Office",
            "Type": "Academic",
        },
        4: {
            "ID": "8A",
            "Name": "School of Architecture & Design",
            "Type": "Academic",
        },
        5: {"ID": "8B", "Name": "School of Pharmacy", "Type": "Academic"},
        6: {
            "ID": "8C",
            "Name": "Uni Hospital / Fine Arts / Animation",
            "Type": "Medical/Arts",
        },
        7: {"ID": "9", "Name": "Girl's Hostel 1", "Type": "Hostel"},
        8: {"ID": "10", "Name": "Girl's Hostel 2", "Type": "Hostel"},
        9: {"ID": "11", "Name": "Girl's Hostel 3", "Type": "Hostel"},
        10: {"ID": "12", "Name": "Girl's Hostel 4", "Type": "Hostel"},
        11: {"ID": "13", "Name": "Division of Student Affairs", "Type": "Admin"},
        12: {
            "ID": "14",
            "Name": "School of Business / Management / Commerce",
            "Type": "Academic",
        },
        13: {"ID": "15A", "Name": "Unicenter", "Type": "Commercial"},
        14: {
            "ID": "15B",
            "Name": "School of Hotel Management",
            "Type": "Academic",
        },
        15: {
            "ID": "18",
            "Name": "School of Arts & Languages / Physical Education",
            "Type": "Academic",
        },
        16: {
            "ID": "19",
            "Name": "Sh. Baldev Raj Mittal Main Stage",
            "Type": "Auditorium",
        },
        17: {"ID": "20", "Name": "School of Law", "Type": "Academic"},
        18: {"ID": "21A", "Name": "Girl's Hostel 5", "Type": "Hostel"},
        19: {"ID": "21B", "Name": "Girl's Hostel 6", "Type": "Hostel"},
        20: {
            "ID": "25",
            "Name": "Computer Science Area (Block 25)",
            "Type": "Academic",
        },
        21: {
            "ID": "26",
            "Name": "Computer Science Area (Block 26)",
            "Type": "Academic",
        },
        22: {
            "ID": "27",
            "Name": "Computer Science Area (Block 27)",
            "Type": "Academic",
        },
        23: {
            "ID": "28",
            "Name": "Computer Science Area (Block 28)",
            "Type": "Academic",
        },
        24: {
            "ID": "29",
            "Name": "Computer Science Area (Block 29)",
            "Type": "Academic",
        },
        25: {
            "ID": "30",
            "Name": "Computer Science Area (Block 30)",
            "Type": "Academic",
        },
        26: {
            "ID": "31",
            "Name": "Computer Science Area (Block 31)",
            "Type": "Academic",
        },
        27: {
            "ID": "32",
            "Name": "Computer Science Area (Block 32)",
            "Type": "Academic",
        },
        28: {
            "ID": "33",
            "Name": "Computer Science Area (Block 33)",
            "Type": "Academic",
        },
        29: {"ID": "34", "Name": "Block 34 (CSE Dept)", "Type": "Academic"},
        30: {
            "ID": "35",
            "Name": "Computer Science Area (Block 35)",
            "Type": "Academic",
        },
        31: {
            "ID": "36",
            "Name": "Computer Science Area (Block 36)",
            "Type": "Academic",
        },
        32: {
            "ID": "37",
            "Name": "Computer Science Area (Block 37)",
            "Type": "Academic",
        },
        33: {
            "ID": "38",
            "Name": "Computer Science Area (Block 38)",
            "Type": "Academic",
        },
        34: {"ID": "56B", "Name": "Block 56B", "Type": "Academic"},
        35: {"ID": "57", "Name": "School of Polytechnic", "Type": "Academic"},
        36: {"ID": "Boys Apartments", "Name": "Boys Apartments", "Type": "Hostel"},
        37: {"ID": "BH1", "Name": "Boys Hostel 1", "Type": "Hostel"},
        38: {"ID": "BH2", "Name": "Boys Hostel 2", "Type": "Hostel"},
        39: {"ID": "BH3", "Name": "Boys Hostel 3", "Type": "Hostel"},
        40: {"ID": "BH4", "Name": "Boys Hostel 4", "Type": "Hostel"},
        41: {"ID": "BH5", "Name": "Boys Hostel 5", "Type": "Hostel"},
        42: {"ID": "BH6", "Name": "Boys Hostel 6", "Type": "Hostel"},
        43: {"ID": "BH7", "Name": "Boys Hostel 7", "Type": "Hostel"},
        44: {
            "ID": "Indoor Sports Complex",
            "Name": "Indoor Sports Complex",
            "Type": "Sports",
        },
        45: {"ID": "Boys Studio 11", "Name": "Boys Studio 11", "Type": "Hostel"},
        46: {"ID": "Boys Studio 12", "Name": "Boys Studio 12", "Type": "Hostel"},
        47: {"ID": "Boys Studio 13", "Name": "Boys Studio 13", "Type": "Hostel"},
    }

    print("\n--- Campus Locations Directory ---")
    for key, val in locations.items():
        print(f"  {key:2d}. [{val['ID']}] {val['Name']} ({val['Type']})")

    try:
        print("\n[1] Select Pickup Location:")
        p_choice = int(input("Enter Pickup Index Number (1-47): "))

        print("\n[2] Select Drop-off Location:")
        d_choice = int(input("Enter Drop-off Index Number (1-47): "))

        if p_choice not in locations or d_choice not in locations:
            print("\n[❌ Error] Invalid location index selected.")
            return None

        pickup = locations[p_choice]
        drop = locations[d_choice]

        # Map to columns expected by the trained pipeline
        inputs = {
            "Pickup_Block": pickup["ID"],
            "Pickup_Location_Name": pickup["Name"],
            "Pickup_Location_Type": pickup["Type"],
            "Drop_Block": drop["ID"],
            "Drop_Location_Name": drop["Name"],
            "Drop_Location_Type": drop["Type"],
            "Route": f"{pickup['ID']} → {drop['ID']}",
            "Day_of_Week": datetime.now().strftime("%A"),
            "Is_Weekend": (
                "Yes"
                if datetime.now().strftime("%A") in ["Saturday", "Sunday"]
                else "No"
            ),
            "Month": datetime.now().strftime("%B"),
            "Week_Number": 10,
            "Hour": 10,
            "Start_Time": "10:00",
            "Time_Slot": "Morning",
            "Weather": "Normal",
            "Traffic_Level": "Medium",
            "Peak_Hour": "Yes",
            "Demand_Level": "High",
            "Distance_m": 500.0,
            "Travel_Time_Min": 3.0,
            "Vehicle_Capacity": 30,
            "Vehicle_ID": "V001",
        }

    except ValueError:
        print("\n[❌ Error] Please enter a valid integer number choice.")
        return None

    return pd.DataFrame([inputs]), pickup, drop


def display_route_analysis(df, pickup_id, drop_id, route_str):
    """Displays the 10-point analytical breakdown tailored to the selected route."""
    if df is None:
        print(
            "\n[ℹ] Dataset not found for detailed route analytics breakdown."
        )
        return

    route_df = df[df["Route"] == route_str]

    print("\n" + "=" * 60)
    print(f"       10-POINT ANALYTICAL REPORT FOR ROUTE: {route_str}")
    print("=" * 60)

    if len(route_df) == 0:
        print(
            "\n[ℹ] Note: Direct historical records for this specific route are limited in the sample dataset."
        )
        print(
            "Showing overall campus metrics and trends mapped to this route's characteristics instead:\n"
        )
        route_df = df  # Fallback to general dataset distribution for comparative stats

    # 1. Total Historical Trips on this Route
    print(
        f"1. Total Historical Trips Recorded: {len(route_df):,} ride records"
    )

    # 2. Average Passenger Count per Trip
    print(
        f"2. Average Passenger Load per Trip:"
        f" {route_df['Passengers'].mean():.2f} passengers"
    )

    # 3. Peak vs Off-Peak Distribution
    peak_counts = route_df["Peak_Hour"].value_counts().to_dict()
    print(
        "3. Peak Hour Distribution (Yes/No):"
        f" {peak_counts.get('Yes', 0)} Peak vs"
        f" {peak_counts.get('No', 0)} Off-Peak trips"
    )

    # 4. Average Travel Time
    print(
        f"4. Average Transit Travel Time:"
        f" {route_df['Travel_Time_Min'].mean():.2f} minutes"
    )

    # 5. Route Distance
    print(
        f"5. Average Route Distance:"
        f" {route_df['Distance_m'].mean():.2f} meters"
    )

    # 6. Dominant Traffic Level Impact
    top_traffic = route_df["Traffic_Level"].mode()[0]
    print(f"6. Dominant Traffic Level Condition: {top_traffic}")

    # 7. Weather Sensitivity
    top_weather = route_df["Weather"].mode()[0]
    print(f"7. Most Common Weather Condition: {top_weather}")

    # 8. Vehicle Capacity Utilization
    print(
        f"8. Average Vehicle Capacity Utilization:"
        f" {route_df['Vehicle_Utilization_Percent'].mean():.2f}%"
    )

    # 9. Busiest Day of the Week for this Route/Campus
    busiest_day = route_df["Day_of_Week"].mode()[0]
    print(f"9. Peak Demand Day of the Week: {busiest_day}")

    # 10. Operational Demand Tier Classification
    avg_passengers = route_df["Passengers"].mean()
    tier = (
        "High Demand (Critical)"
        if avg_passengers > 20
        else "Moderate Demand (Normal)"
    )
    print(f"10. Operational Traffic Tier: {tier}")
    print("=" * 60)


if __name__ == "__main__":
    pipeline = load_model()
    master_df = load_dataset()

    if pipeline:
        result = get_user_pickup_drop()

        if result is not None:
            user_df, pickup_loc, drop_loc = result
            route_str = user_df["Route"].values[0]

            print(
                f"\nRoute Selected: {route_str} "
                f"({pickup_loc['Name']} ➔ {drop_loc['Name']})"
            )

            # Predict passenger demand using the trained pipeline
            prediction = pipeline.predict(user_df)[0]
            print("\n" + "=" * 60)
            print(
                f"🎯 Predicted Passenger Demand: {round(prediction, 2)}"
                " passengers"
            )
            print("=" * 60)

            # Display the 10-point analysis for this route
            display_route_analysis(
                master_df, pickup_loc["ID"], drop_loc["ID"], route_str
            )