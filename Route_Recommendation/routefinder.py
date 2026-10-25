
import os
import webbrowser
import requests
import pandas as pd
import folium

# =========================================================
# 1. CONFIGURATION
# =========================================================

EXCEL_FILE = r"C:\Users\ARYAN MAHAKUR\Downloads\LPU_All_Locations.xlsx"

OSRM_URL = "https://router.project-osrm.org"

# CARTO API key provided by you
CARTO_API_KEY = "cb1_4uc1_1_9e921e35e164b1723654c071"

OUTPUT_HTML = "lpu_route_map.html"


# =========================================================
# 2. LOAD COORDINATES FROM EXCEL
# =========================================================

def load_locations():
    if not os.path.exists(EXCEL_FILE):
        raise FileNotFoundError(
            f"Excel file not found: {EXCEL_FILE}\n"
            "Check the Excel file path."
        )

    blocks = pd.read_excel(
        EXCEL_FILE,
        sheet_name="LPU Locations"
    )

    named = pd.read_excel(
        EXCEL_FILE,
        sheet_name="Named Locations"
    )

    blocks = blocks.rename(columns={
        "Block / Location ID": "ID"
    })

    blocks = blocks[
        ["ID", "Location Name", "Latitude", "Longitude"]
    ]

    named = named.rename(columns={
        "Location ID": "ID"
    })

    named = named[
        ["ID", "Location Name", "Latitude", "Longitude"]
    ]

    locations = pd.concat(
        [blocks, named],
        ignore_index=True
    )

    locations = locations.dropna(
        subset=["ID", "Latitude", "Longitude"]
    ).copy()

    locations["ID"] = (
        locations["ID"].astype(str).str.strip()
    )

    locations["Location Name"] = (
        locations["Location Name"].astype(str).str.strip()
    )

    locations["Latitude"] = pd.to_numeric(
        locations["Latitude"], errors="coerce"
    )

    locations["Longitude"] = pd.to_numeric(
        locations["Longitude"], errors="coerce"
    )

    locations = locations.dropna(
        subset=["Latitude", "Longitude"]
    )

    return locations


# =========================================================
# 3. FIND LOCATION BY ID OR NAME
# =========================================================

def find_location(user_input, locations):
    query = user_input.strip().casefold()

    matches = locations[
        (locations["ID"].str.casefold() == query)
        | (
            locations["Location Name"].str.casefold()
            == query
        )
    ]

    # Support compound IDs, e.g. "2 / 02A".
    if matches.empty:
        matches = locations[
            locations["ID"].apply(
                lambda value: query in [
                    part.strip().casefold()
                    for part in value.split("/")
                ]
            )
        ]

    matches = matches.drop_duplicates(
        subset=[
            "ID",
            "Location Name",
            "Latitude",
            "Longitude"
        ]
    )

    if matches.empty:
        raise ValueError(
            f"Location '{user_input}' was not found in Excel."
        )

    if len(matches) > 1:
        print("\nMultiple locations matched:")
        print(
            matches[
                ["ID", "Location Name", "Latitude", "Longitude"]
            ].to_string(index=False)
        )
        raise ValueError(
            "Enter a more specific location ID or name."
        )

    return matches.iloc[0]


# =========================================================
# 4. GET ROUTES FROM OSRM
# =========================================================

def get_routes(start, end):
    # OSRM expects longitude,latitude.
    coordinates = (
        f"{start['Longitude']},{start['Latitude']};"
        f"{end['Longitude']},{end['Latitude']}"
    )

    url = f"{OSRM_URL}/route/v1/driving/{coordinates}"

    params = {
        "alternatives": "true",
        "overview": "full",
        "geometries": "geojson",
        "steps": "false"
    }

    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    response.raise_for_status()
    data = response.json()

    if data.get("code") != "Ok" or not data.get("routes"):
        raise ValueError(
            f"OSRM could not find a route: {data.get('code')}"
        )

    return data["routes"]


# =========================================================
# 5. CREATE CAMPUS ROUTE MAP
# =========================================================

def create_map(start, end, routes):
    start_point = [
        float(start["Latitude"]),
        float(start["Longitude"])
    ]

    end_point = [
        float(end["Latitude"]),
        float(end["Longitude"])
    ]

    # Best alternatives returned by OSRM.
    shortest = min(routes, key=lambda r: r["distance"])
    fastest = min(routes, key=lambda r: r["duration"])

    campus_map = folium.Map(
        location=start_point,
        zoom_start=16,
        tiles=None
    )

    # CARTO Voyager raster map tiles.
    tile_url = (
        "https://basemaps.cartocdn.com/rastertiles/"
        "voyager/{z}/{x}/{y}.png"
        f"?key={CARTO_API_KEY}"
    )

    folium.TileLayer(
        tiles=tile_url,
        name="CARTO Voyager",
        attr="© OpenStreetMap contributors © CARTO",
        overlay=False,
        control=True
    ).add_to(campus_map)

    # Pickup marker.
    folium.Marker(
        start_point,
        tooltip=f"Pickup: {start['ID']}",
        popup=str(start["Location Name"]),
        icon=folium.Icon(
            color="green",
            icon="play"
        )
    ).add_to(campus_map)

    # Drop marker.
    folium.Marker(
        end_point,
        tooltip=f"Drop: {end['ID']}",
        popup=str(end["Location Name"]),
        icon=folium.Icon(
            color="red",
            icon="stop"
        )
    ).add_to(campus_map)

    # Draw routes.
    for route in routes:
        is_shortest = route is shortest
        is_fastest = route is fastest

        if is_shortest and is_fastest:
            color = "purple"
            label = "Shortest and fastest"
        elif is_shortest:
            color = "green"
            label = "Shortest distance"
        elif is_fastest:
            color = "blue"
            label = "Fastest time"
        else:
            color = "orange"
            label = "Alternative"

        # GeoJSON uses longitude,latitude.
        points = [
            [lat, lon]
            for lon, lat in route["geometry"]["coordinates"]
        ]

        folium.PolyLine(
            points,
            color=color,
            weight=7 if is_shortest or is_fastest else 4,
            opacity=0.85,
            tooltip=(
                f"{label} | "
                f"{route['distance'] / 1000:.2f} km | "
                f"{route['duration'] / 60:.1f} minutes"
            )
        ).add_to(campus_map)

    # Zoom to the selected route.
    campus_map.fit_bounds(
        [start_point, end_point],
        padding=(40, 40)
    )

    folium.LayerControl().add_to(campus_map)

    return campus_map, shortest, fastest


# =========================================================
# 6. MAIN PROGRAM
# =========================================================

def main():
    print("=" * 55)
    print("          LPU CAMPUS ROUTE FINDER")
    print("=" * 55)

    locations = load_locations()

    print(
        f"\nLoaded {len(locations)} location records from Excel."
    )

    print(
        "Examples: 25, 38, 57, BH1, Boys Studio 11\n"
    )

    pickup_input = input(
        "Enter pickup block/location: "
    )

    drop_input = input(
        "Enter drop block/location: "
    )

    start = find_location(pickup_input, locations)
    end = find_location(drop_input, locations)

    if (
        start["Latitude"] == end["Latitude"]
        and start["Longitude"] == end["Longitude"]
    ):
        raise ValueError(
            "Pickup and drop have identical coordinates. "
            "Check the Excel data."
        )

    print(
        f"\nPickup: {start['ID']} - {start['Location Name']}"
    )

    print(
        f"Drop: {end['ID']} - {end['Location Name']}"
    )

    print("\nRequesting routes from OSRM...")

    routes = get_routes(start, end)

    campus_map, shortest, fastest = create_map(
        start, end, routes
    )

    print("\n" + "=" * 55)
    print("ROUTE COMPARISON")
    print("=" * 55)

    print(f"Routes returned by OSRM: {len(routes)}")

    print("\nSHORTEST DISTANCE ROUTE")
    print(f"Distance: {shortest['distance'] / 1000:.3f} km")
    print(f"Time: {shortest['duration'] / 60:.2f} minutes")

    print("\nFASTEST ROUTE")
    print(f"Distance: {fastest['distance'] / 1000:.3f} km")
    print(f"Time: {fastest['duration'] / 60:.2f} minutes")

    campus_map.save(OUTPUT_HTML)

    full_path = os.path.abspath(OUTPUT_HTML)

    print(f"\nMap saved to: {full_path}")
    print("Opening map in your browser...")

    webbrowser.open("file://" + full_path)


if __name__ == "__main__":
    try:
        main()

    except (ValueError, FileNotFoundError) as error:
        print(f"\nError: {error}")

    except requests.RequestException as error:
        print(f"\nRequest failed: {error}")
