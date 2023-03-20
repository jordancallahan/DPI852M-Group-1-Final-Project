import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import geopandas as gpd

st.title("Measures of Innovation")

# Title with hyperlink
st.write("This Streamlit app displays data visualizations based on the research and data from "
         "[The State of U.S. Science and Engineering 2022](https://ncses.nsf.gov/pubs/nsb20221/u-s-and-global-science-and-technology-capabilities),\
            a report published by the National Science Foundation.")

st.write("## Share of International Patents Granted by Country")

# Data
patents = pd.read_excel(
    "https://github.com/jordancallahan/DPI852M-Group-1-Final-Project/blob/kendrick-branch/data/figures/patent_data.xlsx?raw=true", skiprows=3)
patents = patents.replace("EU-27", "EU")
patents = patents.replace("United States", "U.S.")
countries = patents["Country or economy"]
share_2010 = patents["2010"]
share_2020 = patents["2020"]

# Create subplots
polar_chart = make_subplots(rows=1, cols=2, specs=[
    [{'type': 'polar'}, {'type': 'polar'}]])

# Add 2010 data
polar_chart.add_trace(go.Barpolar(
    r=share_2010,
    theta=countries,
    name="2010",
    marker_color='blue',
    marker_line_color="black",
    marker_line_width=1,
    opacity=0.7,
    text=share_2010,
    textsrc="inside",
    hovertemplate="%{theta}: %{r:.0f}%<extra></extra>",
), row=1, col=1)

# Add 2020 data
polar_chart.add_trace(go.Barpolar(
    r=share_2020,
    theta=countries,
    name="2020",
    marker_color='red',
    marker_line_color="black",
    marker_line_width=1,
    opacity=0.7,
    text=share_2020,
    textsrc="inside",
    hovertemplate="%{theta}: %{r:.0f}%<extra></extra>",
), row=1, col=2)

polar_chart.update_layout(
    showlegend=False,
    polar=dict(
        domain=dict(x=[0, 0.4], y=[0, 1]),
        radialaxis=dict(visible=False, range=[0, max(share_2010) * 1.1]),
    ),
    polar2=dict(
        domain=dict(x=[0.6, 1], y=[0, 1]),
        radialaxis=dict(visible=False, range=[0, max(share_2020) * 1.1]),
    ),
    annotations=[
        dict(text="2010", x=0.05, y=1.25, font_size=24, showarrow=False),
        dict(text="2020", x=0.7, y=1.25, font_size=24, showarrow=False)
    ],
    margin=dict(l=50, r=50)
)

# Add chart to streamlit page
st.plotly_chart(polar_chart, use_container_width=True)

st.write("## U.S. Patent Office Grants")

uspto_data = pd.DataFrame(
    {'Year': [2010, 2020],
     'Patents': [107000, 164000],
     'Share to foreign inventors': [0.51, 0.54]}
)

uspto_data["Domestic Inventors"] = (
    1 - uspto_data["Share to foreign inventors"]) * uspto_data["Patents"]
uspto_data["Foreign Inventors"] = uspto_data["Share to foreign inventors"] * \
    uspto_data["Patents"]

# Initialize figure
bar_chart = go.Figure()

# Add traces for foreign inventors
bar_chart.add_trace(go.Bar(
    x=uspto_data['Year'],
    y=uspto_data['Foreign Inventors'],
    name='Foreign Inventors',
    marker_color='red'
))

# Add traces for domestic inventors
bar_chart.add_trace(go.Bar(
    x=uspto_data['Year'],
    y=uspto_data['Domestic Inventors'],
    name='Domestic Inventors',
    marker_color='blue'
))

# Update layout to stack bars
bar_chart.update_layout(
    barmode='stack',
    title='Total Patents Granted by USPTO (2010 vs 2020)',
    xaxis_title='Year',
    yaxis_title='Number of Patents'
)

# Match colors of polar chart
bar_chart.update_traces(marker_line_color='black',
                        marker_line_width=1.5, opacity=0.7)

bar_chart.add_annotation(
    x=2010,
    y=uspto_data["Foreign Inventors"][0] / 2,
    text=str(
        round(uspto_data["Share to foreign inventors"][0] * 100, 1)) + "%",
    showarrow=False,
    font=dict(
        size=16,
        color="white"
    )
)
bar_chart.add_annotation(
    x=2020,
    y=uspto_data["Foreign Inventors"][1] / 2,
    text=str(
        round(uspto_data["Share to foreign inventors"][1] * 100, 1)) + "%",
    showarrow=False,
    font=dict(
        size=16,
        color="white"
    )
)

bar_chart.add_annotation(
    x=2010,
    y=uspto_data["Patents"][0] + 10000,
    text=str(uspto_data["Patents"][0]),
    showarrow=False,
    font=dict(
        size=16,
        color="white"
    )
)
bar_chart.add_annotation(
    x=2020,
    y=uspto_data["Patents"][1] + 10000,
    text=str(uspto_data["Patents"][1]),
    showarrow=False,
    font=dict(
        size=16,
        color="white"
    )
)

bar_chart.update_xaxes(tickvals=[2010, 2020])

# Change tooltip to remove year
bar_chart.update_traces(hovertemplate="%{y:.0f}<extra></extra>")

# Add chart to streamlit page
st.plotly_chart(bar_chart, use_container_width=True)

# Map of patents per 1000 residents by county
st.write("## Patents per 1000 Residents by County")

# Load data
file_path = 'https://github.com/jordancallahan/DPI852M-Group-1-Final-Project/blob/kendrick-branch/data/figures/merged_data.geojson?raw=true'
patent_geo_data = gpd.read_file(file_path)

# Create the choropleth map
map_plot = px.choropleth_mapbox(
    patent_geo_data,
    geojson=patent_geo_data.geometry,
    locations=patent_geo_data.index,
    color='color_group',
    hover_name='County',
    hover_data=['State', 'Patents', 'Population'],
    category_orders={'color_group': [
        '0', 'Quartile 1', 'Quartile 2', 'Quartile 3', 'Quartile 4']},
    # Set lowest to grey and others as increasingly dark blue colors
    color_discrete_map={
        '0': '#d3d3d3',
        'Quartile 1': '#FFFFC2',
        'Quartile 2': '#37A9B8',
        'Quartile 3': '#256AAA',
        'Quartile 4': '#1C2182'
    },
    center={"lat": 37.0902, "lon": -95.7129},
    mapbox_style="carto-positron",
    zoom=3,
    labels={'color_group': 'Patent Concentration'}
)

# Update the layout
map_plot.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# Adjust figure tooltip to show number of patents, population, and State
map_plot.update_traces(
    hovertemplate="<b>%{hovertext}</b><br><br>" +
    "State: %{customdata[0]}<br>" +
    "Population: %{customdata[2]}<br>" +
    "Patents: %{customdata[1]}<br>"
)

st.plotly_chart(map_plot, use_container_width=True)
