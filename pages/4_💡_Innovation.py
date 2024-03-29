import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import geopandas as gpd

st.set_page_config(layout="centered")

st.title("Measures of Innovation")

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

# Markdown section with hyperlink
st.markdown(
    """
Measuring patent activity is a common way to measure innovation. Patents are "one way
governments support invention by providing legal mechanisms for intellectual property
protection," according to the National Science Foundation.

Here, we've outlined patents at the international, national, and local levels, using
data collected by the National Science Foundation's work on [Invention, Knowledge Transfer, and Innovation](https://ncses.nsf.gov/pubs/nsb20204/invention-u-s-and-comparative-global-trends).
"""
)

st.subheader("Share of International Patents Granted by Country")

st.markdown(
    """
First, we'll look at the share of international patents granted by country. A
comparison beetween 2010 and 2020 demonstrate a shift in the nations leading in patent
grants, with massive patent growth in China in particular.
"""
)

# Data
patents = pd.read_excel(
    "https://github.com/jordancallahan/DPI852M-Group-1-Final-Project/blob/kendrick-branch/data/figures/patent_data.xlsx?raw=true",
    skiprows=3,
)
patents = patents.replace("EU-27", "EU")
patents = patents.replace("United States", "U.S.")
countries = patents["Country or economy"]
share_2010 = patents["2010"]
share_2020 = patents["2020"]

# Create subplots
polar_chart = make_subplots(
    rows=1, cols=2, specs=[[{"type": "polar"}, {"type": "polar"}]]
)

# Add 2010 data
polar_chart.add_trace(
    go.Barpolar(
        r=share_2010,
        theta=countries,
        name="2010",
        marker_color="blue",
        marker_line_color="black",
        marker_line_width=1,
        opacity=0.7,
        text=share_2010,
        textsrc="inside",
        hovertemplate="%{theta}: %{r:.0f}%<extra></extra>",
    ),
    row=1,
    col=1,
)

# Add 2020 data
polar_chart.add_trace(
    go.Barpolar(
        r=share_2020,
        theta=countries,
        name="2020",
        marker_color="red",
        marker_line_color="black",
        marker_line_width=1,
        opacity=0.7,
        text=share_2020,
        textsrc="inside",
        hovertemplate="%{theta}: %{r:.0f}%<extra></extra>",
    ),
    row=1,
    col=2,
)

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
        dict(text="2020", x=0.7, y=1.25, font_size=24, showarrow=False),
    ],
    margin=dict(l=50, r=50),
)

# Add chart to streamlit page
st.plotly_chart(polar_chart, use_container_width=True)

st.subheader("U.S. Patent Office Grants")

st.markdown(
    """
The U.S. Patent and Trademark Office (USPTO) grants patents in the U.S. both to
domestic and foreign inventors.

The chart below demonstrates that the overall number of patents granted by the office
increased by 53 percent between 2010 and 2020.

Looking at the breakdown of patent grants, we can also see that the share of patents
granted to foreign inventors increased slightly, accounting for just over half the
total number of patents granted in both years.

"""
)

uspto_data = pd.DataFrame(
    {
        "Year": [2010, 2020],
        "Patents": [107000, 164000],
        "Share to foreign inventors": [0.51, 0.54],
    }
)

uspto_data["Domestic Inventors"] = (
    1 - uspto_data["Share to foreign inventors"]
) * uspto_data["Patents"]
uspto_data["Foreign Inventors"] = (
    uspto_data["Share to foreign inventors"] * uspto_data["Patents"]
)

# Initialize figure
bar_chart = go.Figure()

# Add traces for foreign inventors
bar_chart.add_trace(
    go.Bar(
        x=uspto_data["Year"],
        y=uspto_data["Foreign Inventors"],
        name="Foreign Inventors",
        marker_color="red",
    )
)

# Add traces for domestic inventors
bar_chart.add_trace(
    go.Bar(
        x=uspto_data["Year"],
        y=uspto_data["Domestic Inventors"],
        name="Domestic Inventors",
        marker_color="blue",
    )
)

# Update layout to stack bars
bar_chart.update_layout(
    barmode="stack",
    title="Total Patents Granted by USPTO (2010 vs 2020)",
    xaxis_title="Year",
    yaxis_title="Number of Patents",
)

# Match colors of polar chart
bar_chart.update_traces(marker_line_color="black", marker_line_width=1.5, opacity=0.7)

bar_chart.add_annotation(
    x=2010,
    y=uspto_data["Foreign Inventors"][0] / 2,
    text=str(round(uspto_data["Share to foreign inventors"][0] * 100, 1)) + "%",
    showarrow=False,
    font=dict(size=16, color="white"),
)
bar_chart.add_annotation(
    x=2020,
    y=uspto_data["Foreign Inventors"][1] / 2,
    text=str(round(uspto_data["Share to foreign inventors"][1] * 100, 1)) + "%",
    showarrow=False,
    font=dict(size=16, color="white"),
)

bar_chart.add_annotation(
    x=2010,
    y=uspto_data["Patents"][0] + 10000,
    text=str(uspto_data["Patents"][0]),
    showarrow=False,
    font=dict(size=16, color="white"),
)
bar_chart.add_annotation(
    x=2020,
    y=uspto_data["Patents"][1] + 10000,
    text=str(uspto_data["Patents"][1]),
    showarrow=False,
    font=dict(size=16, color="white"),
)

bar_chart.update_xaxes(tickvals=[2010, 2020])

# Change tooltip to remove year
bar_chart.update_traces(hovertemplate="%{y:.0f}<extra></extra>")

# Add chart to streamlit page
st.plotly_chart(bar_chart, use_container_width=True)

# Map of patents per 1000 residents by county
st.subheader("Patents per 1000 Residents by U.S. County")

st.markdown(
    """
    At the local level, we can visualize the number of patents per 1,000 residents in
    U.S. counties to see which areas of the country feature high levels of innovation.
    The map below confirms well-known hubs of innovation such as the San Francisco Bay
    Area and Boston feature many patent grants. But it also shows how other areas of
    the country, like near the Great Lakes for instance, also have high levels of
    innovation.
"""
)

# Load data
file_path = "https://github.com/jordancallahan/DPI852M-Group-1-Final-Project/blob/kendrick-branch/data/figures/merged_data.geojson?raw=true"
patent_geo_data = gpd.read_file(file_path)

# Create the choropleth map
map_plot = px.choropleth_mapbox(
    patent_geo_data,
    geojson=patent_geo_data.geometry,
    locations=patent_geo_data.index,
    color="color_group",
    hover_name="County",
    hover_data=["State", "Patents", "Population"],
    category_orders={
        "color_group": ["0", "Quartile 1", "Quartile 2", "Quartile 3", "Quartile 4"]
    },
    color_discrete_map={
        "0": "#d3d3d3",
        "Quartile 1": "#FFFFC2",
        "Quartile 2": "#37A9B8",
        "Quartile 3": "#256AAA",
        "Quartile 4": "#1C2182",
    },
    center={"lat": 37.0902, "lon": -95.7129},
    mapbox_style="carto-positron",
    zoom=3,
    labels={"color_group": "Patent Concentration"},
)

# Update the layout
map_plot.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# Adjust figure tooltip to show number of patents, population, and State
map_plot.update_traces(
    hovertemplate="<b>%{hovertext}</b><br><br>"
    + "State: %{customdata[0]}<br>"
    + "Population: %{customdata[2]}<br>"
    + "Patents: %{customdata[1]}<br>"
)

st.plotly_chart(map_plot, use_container_width=True)

st.markdown(
    """
    This Streamlit app displays data visualizations based on the research and data from
[The State of U.S. Science and Engineering 2022](https://ncses.nsf.gov/pubs/nsb20221/u-s-and-global-science-and-technology-capabilities),
a report published by the National Science Foundation.
    """
)
