import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static

st.set_page_config(page_title="Global R&D Expenditures", layout="wide")

st.markdown("# Global R&D Expenditures")
st.sidebar.header("")
st.write("This visualization shows the worldwide R&D expenditures by region.")

st.sidebar.info(
    """
    - Web App [URL](TBU)
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

# Data source: https://data.oecd.org/rd/gross-domestic-spending-on-r-d.htm

# Filter the data by MEASURE: "MLN_USD" and extract the required columns
country_data_mln = df[df["MEASURE"] == "MLN_USD"][["LOCATION", "TIME", "Value"]]

# Create the heatmap using Plotly
fig = px.choropleth(
    country_data_mln,
    locations="LOCATION",
    color="Value",
    hover_name="LOCATION",
    color_continuous_scale="Viridis",
    scope="world",
    projection="natural earth",
    animation_frame="TIME",
    height=600,
    title="R&D Expenditures by Country (Millions USD)",
)

# Filter the data by MEASURE: "PC_GDP" and extract the required columns
country_data_pc = df[df["MEASURE"] == "PC_GDP"][["LOCATION", "TIME", "Value"]]

# Create the heatmap using Plotly
fig2 = px.choropleth(
    country_data_pc,
    locations="LOCATION",
    color="Value",
    hover_name="LOCATION",
    color_continuous_scale="Viridis",
    scope="world",
    projection="natural earth",
    animation_frame="TIME",
    height=600,
    title="R&D Expenditures by Country (Percent of GDP)",
)

# Create the map using Folium
# Read the GeoJSON data for countries
url_geojson = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"

# Map the LOCATION column to the ISO_A3 column in the GeoJSON data
# This is bugged out for now
# country_data_mln["LOCATION"] = country_data_mln["LOCATION"].map(
#     {
#         "United States": "USA",
#         "Canada": "CAN",
#         "Mexico": "MEX",
#         "Korea": "KOR",
#         "Japan": "JPN",
#         "China": "CHN",
#         "Germany": "DEU",
#         "France": "FRA",
#         "United Kingdom": "GBR",
#         "Italy": "ITA",
#         "Spain": "ESP",
#         "Netherlands": "NLD",
#         "Belgium": "BEL",
#         "Switzerland": "CHE",
#         "Austria": "AUT",
#         "Sweden": "SWE",
#         "Norway": "NOR",
#         "Finland": "FIN",
#         "Denmark": "DNK",
#         "Ireland": "IRL",
#         "Luxembourg": "LUX",
#         "Portugal": "PRT",
#         "Greece": "GRC",
#         "Iceland": "ISL",
#         "Poland": "POL",
#         "Czech Republic": "CZE",
#         "Hungary": "HUN",
#         "Slovak Republic": "SVK",
#         "Slovenia": "SVN",
#         "Estonia": "EST",
#         "Latvia": "LVA",
#         "Lithuania": "LTU",
#         "Romania": "ROU",
#         "Bulgaria": "BGR",
#         "Cyprus": "CYP",
#         "Malta": "MLT",
#         "Turkey": "TUR",
#         "Russian Federation": "RUS",
#         "Ukraine": "UKR",
#         "Belarus": "BLR",
#         "Moldova": "MDA",
#         "Armenia": "ARM",
#         "Azerbaijan": "AZE",
#         "Georgia": "GEO",
#         "Kazakhstan": "KAZ",
#         "Kyrgyz Republic": "KGZ",
#         "Tajikistan": "TJK",
#         "Turkmenistan": "TKM",
#         "Uzbekistan": "UZB",
#         "Bosnia and Herzegovina": "BIH",
#         "Croatia": "HRV",
#         "Montenegro": "MNE",
#         "Serbia": "SRB",
#         "Albania": "ALB",
#     }
# )

# Create the base map
m = folium.Map(location=[20, 0], zoom_start=2, tiles="cartodbpositron")

# Add the choropleth layer
folium.Choropleth(
    geo_data=url_geojson,
    name="choropleth",
    data=country_data_mln,
    columns=["LOCATION", "Value"],
    key_on="feature.id",
    fill_color="YlGnBu",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="R&D Expenditure (Million USD)",
    highlight=True,
    hover_name="LOCATION",
).add_to(m)

# Streamlit app
st.plotly_chart(fig)
st.plotly_chart(fig2)
folium_static(m)

if __name__ == "__main__":
    st.write("Running Streamlit App")
