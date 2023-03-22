import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd
import folium
from folium.features import GeoJsonTooltip
from streamlit_folium import folium_static
import pycountry

st.set_page_config(page_title="Global R&D Expenditures", layout="centered")

st.markdown("# Global R&D Expenditures")
st.write(
    "This visualization shows the worldwide R&D expenditures by selected countries."
)

st.sidebar.info(
    """
    - Web App [URL](https://dpi852m-group-1-final-project.streamlit.app/)
    - GitHub [repository](https://github.com/jordancallahan/DPI852M-Group-1-Final-Project)
    """
)

st.sidebar.title("Team Members")
st.sidebar.info(
    """
    * Andrew Trzcinski
    * Jordan Callahan
    * Sammy Cervantes
    * May Braverman
    * Kendrick McDonald
    """
)

df = pd.read_csv("data/tables/global_domestic_RD_spend.csv")

# Drop the INDICATOR, SUBJECT, FREQUENCY, and Flag Codes columns
df = df.drop(columns=["INDICATOR", "SUBJECT", "FREQUENCY", "Flag Codes"])

# Convert the TIME column to int
df["TIME"] = df["TIME"].astype(int)

# Only go to 2020
df = df[df["TIME"] <= 2020]

# Data source: https://data.oecd.org/rd/gross-domestic-spending-on-r-d.htm


# Since the names don't match between datasets (e.g. "United States" vs "United States of America"),
# we need to standardize the names
@st.cache_data
def standardize_country_name(name):
    try:
        # Convert the country name to the three-letter country code
        alpha_3 = pycountry.countries.search_fuzzy(name)[0].alpha_3
        # Convert the three-letter country code back to the official country name
        country_name = pycountry.countries.get(alpha_3=alpha_3).name
        return country_name
    except LookupError:
        # Return the original name if the country is not found
        return name


# Convert three-letter country code to country name
@st.cache_data
def alpha3_to_country_name(alpha3_code):
    country = pycountry.countries.get(alpha_3=alpha3_code)
    if country:
        return country.name
    else:
        return None


# Add country name column to df
df["name"] = df["LOCATION"].apply(alpha3_to_country_name)  # type: ignore

# Read the GeoJSON data for countries
url_geojson = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
world_geojson = gpd.read_file(url_geojson)

# Standardize names
world_geojson["name"] = world_geojson["name"].apply(standardize_country_name)

# Merge the GeoJSON data with the country_data DataFrame using the country_name column
merged_data = world_geojson.merge(df, left_on="name", right_on="name", how="left")

merged_data = merged_data.sort_values(by="TIME", ascending=True)

# Total R&D Expenditures by Country
# Filter the data by MEASURE: "MLN_USD"
country_data_mln = merged_data[merged_data["MEASURE"] == "MLN_USD"]

# Create the heatmap using Plotly
fig_1 = px.choropleth(
    country_data_mln,
    locations="LOCATION",
    color="Value",
    hover_name="name",
    color_continuous_scale="Viridis",
    scope="world",
    projection="natural earth",
    animation_frame="TIME",
    height=600,
    title="R&D Expenditures by Country (Millions USD)",
)

# Update the layout properties of the figure
fig_1.update_geos(
    showcountries=True,
    countrycolor="Black",
    showcoastlines=True,
    coastlinecolor="Black",
)

# Percent of GDP R&D Expenditures by Country
# Filter the data by MEASURE: "PC_GDP" and extract the required columns
country_data_pc = merged_data[merged_data["MEASURE"] == "PC_GDP"]

# Create the heatmap using Plotly
fig_2 = px.choropleth(
    country_data_pc,
    locations="LOCATION",
    color="Value",
    hover_name="name",
    color_continuous_scale="Viridis",
    scope="world",
    projection="natural earth",
    animation_frame="TIME",
    height=600,
    title="R&D Expenditures by Country (Percent of GDP)",
)

# Update the layout properties of the figure
fig_2.update_geos(
    showcountries=True,
    countrycolor="Black",
    showcoastlines=True,
    coastlinecolor="Black",
)

# Create the map using Folium
# Look at 2020 only
data_2020 = country_data_pc[country_data_pc["TIME"] == 2020]

# Create a new GeoDataFrame with the filtered data
gdf_2020 = gpd.GeoDataFrame(data_2020, geometry=data_2020.geometry)  # type: ignore

# Convert the new GeoDataFrame to a GeoJSON object
data_2020_geojson = gdf_2020.to_json()

# Create a Folium map centered on the world
folium_map_2 = folium.Map(location=[50, -50], zoom_start=2)

# Create a tooltip for the choropleth layer
tooltip = GeoJsonTooltip(
    fields=["name", "Value"],
    aliases=["Country", "R&D Expenditure (% of GDP)"],
    localize=True,
    sticky=False,
    labels=True,
    style="""
        background-color: #F0EFEF;
        border: 2px solid black;
        border-radius: 3px;
        box-shadow: 3px;
    """,
    max_width=800,
)


# Add a choropleth layer using the GeoJSON object
chloropleth = folium.Choropleth(
    geo_data=data_2020_geojson,
    data=data_2020,
    columns=["name", "Value"],
    key_on="feature.properties.name",
    fill_color="YlGnBu",
    fill_opacity=0.7,
    line_opacity=0.2,  # type: ignore
    legend_name="R&D Expenditure (% of GDP)",
    # Add a title
    name="R&D Expenditure (% of GDP) in 2020",
).add_to(folium_map_2)

# Add tooltip to the choropleth layer
chloropleth.geojson.add_child(tooltip)
# Add a layer control element to the map
chloropleth.add_to(folium_map_2)

# Add a layer control element to the map
folium.LayerControl().add_to(folium_map_2)

# Streamlit app
# Display the Folium map in Streamlit
st.write("R&D Expenditures by Country (% of GDP) in 2020")
folium_static(folium_map_2)
st.plotly_chart(fig_1)
st.plotly_chart(fig_2)


if __name__ == "__main__":
    st.write("Running Streamlit App")
