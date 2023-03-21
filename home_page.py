import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")

st.sidebar.info(
    """
   GitHub Repository: [Click Here](https://github.com/jordancallahan/DPI852M-Group-1-Final-Project)

    Take a look behind the scenes at our code and data with the link above!
    """
)

st.sidebar.title("Team Members")
st.sidebar.info(
    """
    Andrew Trzcinski\
    Jordan Callahan\
    Sammy Cervantes\
    May Braverman\
    Kendrick McDonald

    """
)

st.title("R+D Expenditure - US and Worldwide")

st.subheader("Introduction")
st.markdown(
    """
    Welcome to our website, folks! We are a group of six students from the Harvard Kennedy School, taking an Advanced Data Visualization course with Professor Hong Qu. Our project focuses on research and development (R&D) spending, with a view to exploring the trends and patterns of R&D spending both in the United States and worldwide. We will also look at the distribution of R&D spending across the US and its impact on several related topics.

We believe in presenting our research in a way that everyone can understand, so we have utilized a wide variety data visualization techniques (all in one simple webpage) to create visuals that will help convey our insights in a simple and accessible way. Our hope is that this will help policymakers or anyone interested in better understanding the R+D spending landscape can get a good introduction with these visuals.

We're thrilled to have this opportunity to showcase our findings on this platform, and we hope you find our research and analysis interesting and informative. So go ahead, take a look around, and feel free to explore the data sets that we used to make our discoveries. Thanks for stopping by, and we hope you enjoy the website!
"""
)

st.info("Click on the left sidebar menu to navigate through each topic.")







