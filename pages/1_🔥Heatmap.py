import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import json
from collections import OrderedDict

st.set_page_config(layout="wide")

st.sidebar.info(
    """
   
    - Web App URL: <insert home link here>
    - GitHub repository: <insert github link here>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
   Add team info here
    """
)

st.title("Heatmap of R&D Spending by State")

import pandas as pd

filepath = "https://raw.githubusercontent.com/jordancallahan/DPI852M-Group-1-Final-Project/main/data/tables/R_and_D_by_state.csv"
df = pd.read_csv(filepath)
df = df.replace(",", "", regex=True).fillna("0")

with st.expander("See source code"):
    with st.echo():
        filepath = df
        m = leafmap.Map(center=[40, -100], zoom=4, tiles="stamentoner")

        # Load the CSV data and preprocess the data
        df = pd.read_csv(filepath)
        df = df.replace("NA", "0")
        for year in range(2006, 2022):
            col_name = str(year)
            df[col_name] = df[col_name].str.replace(",", "").astype(int)

        # Add a slider to select the year
        min_year = 2006
        max_year = 2021
        selected_year = st.sidebar.slider("Select year", min_year, max_year, max_year)
        selected_column = f"{selected_year}"

        m.add_heatmap(
            data=df,
            latitude="Latitude",
            longitude="Longitude",
            value=selected_column,
            name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)

st.title("Animated Heatmap of R&D Spending by State")

# Create the animated heatmap
m_animated = leafmap.Map(center=[40, -100], zoom=4, tiles="stamentoner")

# Prepare the data for the time_slider_choropleth() function
data = []
for year in range(min_year, max_year + 1):
    year_data = df[["State", "Latitude", "Longitude", str(year)]]
    year_data_dict = year_data.to_dict(orient="records")
    year_data_json = json.dumps(year_data_dict, ensure_ascii=False)
    data.append(OrderedDict({"time": str(year), "data": year_data_json}))

# Add the time_slider_choropleth() function to create the animated heatmap
m_animated.time_slider_choropleth(
    data=data,
    latitude="Latitude",
    longitude="Longitude",
    weight=str(year),
    time_interval=1000,
    auto_play=True,
    radius=20,
)

m_animated.to_streamlit(height=700)


st.markdown(
       """
From a national perspective, research and development (R&D) spending in the United States has experienced considerable growth between 2006 and 2021. This expansion can be attributed to various factors, including increased government investments, a growing emphasis on technological innovation, and the rise of private sector R&D efforts. The United States has maintained its position as one of the world's top spenders on R&D, with industries such as technology, pharmaceuticals, and aerospace driving much of this investment. Additionally, federal policies, tax incentives, and funding programs have played a crucial role in promoting research in both the public and private sectors. This continuous growth in R&D spending has helped to fuel advancements in technology, healthcare, and other areas, further solidifying the United States' position as a global leader in innovation.

From a state-by-state perspective, there have been notable differences in R&D spending throughout the years. States with strong technology and research sectors, such as California, Massachusetts, and Washington, have consistently been at the forefront of R&D expenditure. These states benefit from the presence of major technology companies, prestigious research institutions, and a highly skilled workforce, which collectively contribute to their high levels of investment. In other states, such as Texas and North Carolina, R&D spending has also seen substantial growth, driven by factors such as the expansion of research universities, targeted economic development initiatives, and the growth of industries like biotechnology and renewable energy.

However, not all states have experienced the same level of growth in R&D spending. Some states have faced economic challenges or have not been able to attract the same level of investment as others. Factors such as geographic location, the availability of skilled labor, and the presence of research-intensive industries can significantly impact a state's ability to increase R&D spending. Overall, the landscape of R&D spending in the United States between 2006 and 2021 has been one of both growth and disparity, with some states outpacing others in their pursuit of research-driven innovation.

    """
)
