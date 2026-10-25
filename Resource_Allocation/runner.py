from datetime import datetime
import os
import joblib
import pandas as pd


def load_model_and_data():
    """Loads the trained ML pipeline and master dataset."""
    model_file = "demand_prediction_pipeline.pkl"
    data_file = "LPU_Transportation_Master_Dataset_10000.xlsx"
    if not os.path.exists(data_file):
        data_file = (
            r"C:\Users\ARYAN MAHAKUR\Downloads\LPU_Transportation_Master_Dataset_10000"
            " (1).xlsx"
        )

    try:
        pipeline = joblib.load(model_file)
        df = pd.read_excel(data_file, sheet_name="Ride Records")
        return pipeline, df
    except Exception as e:
        print(f"[❌ Error] Could not load model or dataset: {e}")
        return None, None


def get_user_route_and_resources():
    """Takes 2 locations and shuttle driver/capacity details from the user."""
    print("=" * 65)
    print("       LPU ROUTE DETAILED SUMMARY & RESOURCE ASSESSOR       ")
    print("=" * 65)

    # Comprehensive LPU Campus Locations Dictionary matching the dataset
    locations = {
        1: {"ID": "1", "Name": "School of Fashion Design", "Type": "Academic"},
        2: {"ID": "2 / 02A", "Name": "Mini Auditorium", "Type": "Auditorium"},
        3: {
            "ID": "3 / 03A",
            "Name": "School of Paramedical Sciences / Electrical Works",
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
        print("\n[1] Select Route Locations:")
        p_choice = int(input("Enter Pickup Index Number (1-47): "))
        d_choice = int(input("Enter Drop-off Index Number (1-47): "))

        if p_choice not in locations or d_choice not in locations:
            print("\n[❌ Error] Invalid location index selected.")
            return None, None

        pickup = locations[p_choice]
        drop = locations[d_choice]

        print("\n[2] Shuttle & Driver Resource Inputs:")
        total_drivers = int(
            input("Enter total available shuttle drivers/units: ")
        )
        bus_capacity = int(
            input("Enter average passenger capacity per shuttle (e.g., 30): ")
        )

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
            "Vehicle_Capacity": bus_capacity,
            "Vehicle_ID": "V001",
        }

        resources = {"total_drivers": total_drivers, "bus_capacity": bus_capacity}

        return pd.DataFrame([inputs]), resources

    except ValueError:
        print("\n[❌ Error] Please enter valid numeric inputs.")
        return None, None


def generate_detailed_summary(user_df, resources, master_df, prediction):
    """Generates a comprehensive summary and resource allocation breakdown for the route."""
    route_str = user_df["Route"].values[0]
    pickup_name = user_df["Pickup_Location_Name"].values[0]
    drop_name = user_df["Drop_Location_Name"].values[0]

    total_drivers = resources["total_drivers"]
    bus_capacity = resources["bus_capacity"]

    # Filter historical data for this route
    route_data = master_df[master_df["Route"] == route_str]
    if len(route_data) == 0:
        route_data = master_df  # Fallback to general dataset if route is rare

    print("\n" + "=" * 65)
    print(f"        DETAILED ANALYTICAL SUMMARY FOR ROUTE: {route_str}")
    print("=" * 65)
    print(f"📍 Origin: {pickup_name}")
    print(f"🏁 Destination: {drop_name}")
    print(f"🎯 Predicted Passenger Demand per Trip: {prediction:.2f} passengers")
    print("-" * 65)

    print("📊 Historical Route Analytics:")
    print(
        f"  • Total Historical Records for Route: {len(route_data):,} trips"
    )
    print(
        f"  • Average Historical Travel Time:"
        f" {route_data['Travel_Time_Min'].mean():.2f} mins"
    )
    print(
        f"  • Average Historical Distance:"
        f" {route_data['Distance_m'].mean():.2f} meters"
    )
    print(
        f"  • Dominant Traffic Condition:"
        f" {route_data['Traffic_Level'].mode()[0]}"
    )
    print(
        f"  • Peak vs Off-Peak Trend:"
        f" {route_data['Peak_Hour'].value_counts().idxmax()} hours dominate"
        " traffic"
    )

    print("\n🚌 Resource Allocation & Driver Assessment:")
    required_drivers = max(1, round((prediction * 3) / bus_capacity))
    print(f"  • Available Drivers / Shuttles: {total_drivers} units")
    print(f"  • Recommended Shuttles for Route: {required_drivers} unit(s)")
    print(f"  • Shuttle Capacity: {bus_capacity} passengers/bus")

    if required_drivers <= total_drivers:
        print(
            "  • Allocation Status: [✔] OPTIMAL. Sufficient driver resources"
            " available."
        )
        freq = max(5, round(60 / ((prediction * 3) / bus_capacity)))
        print(
            f"  • Suggested Operational Frequency: Dispatch 1 shuttle every"
            f" ~{freq} minutes."
        )
    else:
        print(
            "  • Allocation Status: [⚠️ WARNING] High demand exceeds available"
            f" driver pool ({total_drivers} drivers vs"
            f" {required_drivers} needed)."
        )
        print(
            "  • Recommendation: Increase shuttle capacity or reallocate"
            " spare drivers from low-demand routes."
        )
    print("=" * 65)


if __name__ == "__main__":
    pipeline, master_df = load_model_and_data()

    if pipeline is not None and master_df is not None:
        user_df, resources = get_user_route_and_resources()

        if user_df is not None and resources is not None:
            # Predict passenger demand using pipeline
            prediction = pipeline.predict(user_df)[0]

            # Generate summary
            generate_detailed_summary(
                user_df, resources, master_df, prediction
            )