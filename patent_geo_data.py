import pandas as pd
import geopandas as gpd
import requests
import us

per_capita_patents = pd.read_excel(
    'https://github.com/jordancallahan/DPI852M-Group-1-Final-Project/blob/kendrick-branch/data/figures/per_capita_patents.xlsx?raw=true', skiprows=3)
per_capita_patents['Full Name'] = per_capita_patents['County'] + \
    ', ' + per_capita_patents['State']

# Fetch GeoJSON data from the URL
url = 'https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_050_00_20m.json'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    geojson_data = response.json()
    us_counties = gpd.GeoDataFrame.from_features(geojson_data['features'])
    us_counties['STATE'] = us_counties['STATE'].apply(
        lambda x: us.states.lookup(x).name)
    us_counties["Full Name"] = us_counties["NAME"] + " " + \
        us_counties["LSAD"] + ", " + us_counties["STATE"]
else:
    print(f"Error fetching GeoJSON data: {response.status_code}")

# Merge the GeoJSON data with the patent data
merged_data = us_counties.merge(per_capita_patents, on='Full Name', how='left')

# Create a new column 'color_group' in the merged_data DataFrame
merged_data['color_group'] = merged_data['Quintile'].apply(
    lambda x: '0' if pd.isna(
        x) or x == 0 else f"Quartile {int(x)}"
)

# Export the merged data to a GeoJSON file that is stored in the 'data' folder
merged_data.to_file('data/figures/merged_data.geojson', driver='GeoJSON')
