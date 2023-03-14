import streamlit as st
import leafmap.foliumap as leafmap

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

st.title("Heatmap")

with st.expander("See source code"):
    with st.echo():
        filepath = "https://raw.githubusercontent.com/jordancallahan/DPI852M-Group-1-Final-Project/Andrew/data/tables/R_and_D_by_state.csv"
        m = leafmap.Map(center=[40, -100], zoom=4, tiles="stamentoner")
        m.add_heatmap(
            filepath,
            latitude="Latitude",
            longitude="Longitude",
            value="2021",
            name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)