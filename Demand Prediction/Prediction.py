from datetime import datetime
import joblib
import pandas as pd


def load_model():
  """Loads the trained ML pipeline from the pkl file."""
  filename = "demand_prediction_pipeline.pkl"
  try:
    pipeline = joblib.load(filename)
    print(f"Model loaded successfully from {filename}\n")
    return pipeline
  except FileNotFoundError:
    print(
        f"Error: {filename} not found! Please run `train_model.py` first to"
        " generate the model."
    )
    return None


def get_user_input():
  """Takes only Location, Date, and Time inputs from the user across all LPU blocks."""
  print("=" * 65)
  print("     LPU CAMPUS SHUTTLE & PASSENGER DEMAND PREDICTION SYSTEM      ")
  print("=" * 65)

  inputs = {}

  try:
    # Comprehensive LPU Campus Locations Dictionary (All blocks & hostels)
    locations = {
        1: {
            "ID": "1",
            "Name": "School of Fashion Design",
            "Type": "Academic",
        },
        2: {"ID": "2 / 02A", "Name": "Mini Auditorium", "Type": "Auditorium"},
        3: {
            "ID": "3 / 03A",
            "Name": (
                "School of Paramedical Sciences / Electrical Works / DG Office"
            ),
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
        11: {
            "ID": "13",
            "Name": "Division of Student Affairs",
            "Type": "Admin",
        },
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
        20: {"ID": "25", "Name": "Computer Science Area (Block 25)", "Type": "Academic"},
        21: {"ID": "26", "Name": "Computer Science Area (Block 26)", "Type": "Academic"},
        22: {"ID": "27", "Name": "Computer Science Area (Block 27)", "Type": "Academic"},
        23: {"ID": "28", "Name": "Computer Science Area (Block 28)", "Type": "Academic"},
        24: {"ID": "29", "Name": "Computer Science Area (Block 29)", "Type": "Academic"},
        25: {"ID": "30", "Name": "Computer Science Area (Block 30)", "Type": "Academic"},
        26: {"ID": "31", "Name": "Computer Science Area (Block 31)", "Type": "Academic"},
        27: {"ID": "32", "Name": "Computer Science Area (Block 32)", "Type": "Academic"},
        28: {"ID": "33", "Name": "Computer Science Area (Block 33)", "Type": "Academic"},
        29: {"ID": "34", "Name": "Block 34 (CSE Dept)", "Type": "Academic"},
        30: {"ID": "35", "Name": "Computer Science Area (Block 35)", "Type": "Academic"},
        31: {"ID": "36", "Name": "Computer Science Area (Block 36)", "Type": "Academic"},
        32: {"ID": "37", "Name": "Computer Science Area (Block 37)", "Type": "Academic"},
        33: {"ID": "38", "Name": "Computer Science Area (Block 38)", "Type": "Academic"},
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

    print("\n[1] Select Campus Location / Block:")
    for key, val in locations.items():
      print(f"  {key:2d}. [{val['ID']}] {val['Name']} ({val['Type']})")

    loc_choice = int(input("\nEnter Location Index Number (1-47): "))
    if loc_choice in locations:
      inputs["Location_ID"] = locations[loc_choice]["ID"]
      inputs["Location_Name"] = locations[loc_choice]["Name"]
      inputs["Location_Type"] = locations[loc_choice]["Type"]
    else:
      print("Invalid choice, defaulting to Block 34.")
      inputs["Location_ID"] = "34"
      inputs["Location_Name"] = "Block 34 (CSE Dept)"
      inputs["Location_Type"] = "Academic"

    # 2. Date & Time Selection
    date_str = input(
        "\nEnter Date (YYYY-MM-DD) [Press Enter for Today's Date]: "
    ).strip()
    if date_str == "":
      dt = datetime.now()
    else:
      dt = datetime.strptime(date_str, "%Y-%m-%d")

    inputs["Month"] = dt.month
    inputs["Day_of_Week"] = dt.strftime("%A")
    inputs["Is_Weekend"] = 1 if inputs["Day_of_Week"] in ["Saturday", "Sunday"] else 0

    hour = int(
        input(
            "Enter Hour in 24-hour format (0-23, e.g., 9 for 9 AM, 15 for 3 PM):"
            " "
        )
    )
    inputs["Hour"] = hour

    # Automatically derive Time Slot based on hour
    if 6 <= hour < 12:
      inputs["Time_Slot"] = "Morning"
    elif 12 <= hour < 17:
      inputs["Time_Slot"] = "Afternoon"
    elif 17 <= hour < 21:
      inputs["Time_Slot"] = "Evening"
    else:
      inputs["Time_Slot"] = "Night"

    # Automatically set standard/default values for background environmental/operational columns
    inputs["Weather"] = "Clear"
    inputs["Temperature_C"] = 28.0
    inputs["Is_Peak_Hour"] = (
        1 if (8 <= hour <= 10) or (16 <= hour <= 18) else 0
    )
    inputs["Is_Exam_Period"] = 0
    inputs["Is_Event_Day"] = 0
    inputs["Available_Shuttles"] = 5
    inputs["Avg_Wait_Time_Min"] = 5.0

  except (ValueError, IndexError):
    print(
        "\n[❌ Error] Invalid input entered. Please restart the script and"
        " follow the format."
    )
    return None

  return pd.DataFrame([inputs])


if __name__ == "__main__":
  pipeline = load_model()

  if pipeline:
    user_df = get_user_input()

    if user_df is not None:
      predicted_demand = pipeline.predict(user_df)[0]
      print("\n" + "=" * 55)
      print(
          f"🎯 Predicted Passenger Demand: {round(predicted_demand, 2)} passengers"
      )
      print("=" * 55)