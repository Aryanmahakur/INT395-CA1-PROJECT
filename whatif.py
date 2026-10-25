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


def run_what_if_simulation():
    """Interactively takes route selections and what-if parameter overrides from the user."""
    pipeline, master_df = load_model_and_data()
    if pipeline is None or master_df is None:
        return

    print("=" * 65)
    print("        LPU TRANSPORTATION WHAT-IF SCENARIO SIMULATOR       ")
    print("=" * 65)

    # Comprehensive LPU Campus Locations Dictionary
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
            return

        pickup = locations[p_choice]
        drop = locations[d_choice]

        print("\n[2] Define What-If Scenario Overrides:")
        print(
            "Configure operational conditions to test how passenger demand"
            " shifts:"
        )

        weather_choice = (
            input("Enter Weather condition [Normal / Rain / Fog / Extreme]: ")
            or "Normal"
        )
        traffic_choice = (
            input("Enter Traffic Level [Low / Medium / High / Heavy]: ")
            or "Medium"
        )
        peak_choice = (
            input("Is it Peak Hour? [Yes / No]: ") or "Yes"
        )
        bus_capacity = int(
            input("Enter Shuttle Seating Capacity [default 30]: ") or 30
        )

        # Baseline Input Template
        base_inputs = {
            "Pickup_Block": pickup["ID"],
            "Pickup_Location_Name": pickup["Name"],
            "Pickup_Location_Type": pickup["Type"],
            "Drop_Block": drop["ID"],
            "Drop_Location_Name": drop["Name"],
            "Drop_Location_Type": drop["Type"],
            "Route": f"{pickup['ID']} → {drop['ID']}",
            "Day_of_Week": "Monday",
            "Is_Weekend": "No",
            "Month": "October",
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

        # Baseline DataFrame (Standard Normal Conditions)
        df_baseline = pd.DataFrame([base_inputs])
        baseline_pred = pipeline.predict(df_baseline)[0]

        # Simulation Scenario DataFrame (User What-If Overrides)
        sim_inputs = base_inputs.copy()
        sim_inputs["Weather"] = weather_choice
        sim_inputs["Traffic_Level"] = traffic_choice
        sim_inputs["Peak_Hour"] = peak_choice
        sim_inputs["Vehicle_Capacity"] = bus_capacity

        df_simulation = pd.DataFrame([sim_inputs])
        sim_pred = pipeline.predict(df_simulation)[0]

        # Output Results Comparison
        print("\n" + "=" * 65)
        print(f"        WHAT-IF SIMULATION RESULTS FOR: {sim_inputs['Route']}")
        print("=" * 65)
        print(f"📍 Origin: {pickup['Name']}")
        print(f"🏁 Destination: {drop['Name']}")
        print("-" * 65)
        print(f"📊 Baseline Predicted Demand (Normal Conditions): {baseline_pred:.2f} passengers")
        print(f"🔮 Simulated Predicted Demand (What-If Scenario):  {sim_pred:.2f} passengers")
        
        diff = sim_pred - baseline_pred
        pct_change = (diff / baseline_pred) * 100 if baseline_pred > 0 else 0
        print(f"📈 Net Demand Shift: {diff:+.2f} passengers ({pct_change:+.1f}%)")
        print("-" * 65)
        print("💡 Operational Insight:")
        if diff > 0:
            print(f"  • This scenario increases transit strain. Consider deploying extra shuttles.")
        elif diff < 0:
            print(f"  • This scenario reduces passenger load. Fleet resources can be optimized.")
        else:
            print(f"  • Passenger load remains stable under these conditions.")
        print("=" * 65)

    except ValueError:
        print("\n[❌ Error] Please enter valid numeric choices or text options.")


if __name__ == "__main__":
    run_what_if_simulation()