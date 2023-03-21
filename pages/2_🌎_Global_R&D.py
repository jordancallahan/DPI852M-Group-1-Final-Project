import streamlit as st
import pandas as pd
import plotly.express as px

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
country_data = df[df["MEASURE"] == "MLN_USD"][["LOCATION", "TIME", "Value"]]

# Create the heatmap using Plotly
fig = px.choropleth(
    country_data,
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
country_data = df[df["MEASURE"] == "PC_GDP"][["LOCATION", "TIME", "Value"]]

# Create the heatmap using Plotly
fig2 = px.choropleth(
    country_data,
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

# Streamlit app
st.plotly_chart(fig)
st.plotly_chart(fig2)

if __name__ == "__main__":
    st.write("Running Streamlit App")
