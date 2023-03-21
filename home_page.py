import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide", page_title="R+D Expenditure - US and Worldwide")

st.sidebar.info(
    """
   GitHub Repository: [Click Here](https://github.com/jordancallahan/DPI852M-Group-1-Final-Project)

    Take a look behind the scenes at our code and data with the link above!
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

st.title("Science, Technology, Research, and Development Indicators - US and Worldwide")

st.subheader("Introduction")
st.markdown(
    """
    Welcome to our website, folks! We are a group of five students from the Harvard Kennedy School, taking an Advanced Data Visualization course with Professor Hong Qu. Our project focuses on indicators related to Science, Technology, Research, and Development, with a view to exploring the trends and patterns both in the United States and worldwide.

We believe in presenting our research in a way that everyone can understand, so we have utilized a wide variety data visualization techniques (all in one simple webpage) to create visuals that will help convey our insights in a simple and accessible way. Our hope is that this will help policymakers or anyone interested in better understanding the R+D spending landscape can get a good introduction with these visuals. We have a mix of skillsets on the team so have also worked in a way that allowed for both collaboration and comfort - helping eachother where we we able to and working on ways to harmonize multiple platforms.

We're thrilled to have this opportunity to showcase our findings on this platform, and we hope you find our research and analysis interesting and informative. So go ahead, take a look around, and feel free to explore the data sets that we used to make our discoveries (please explore our GitHub too - that architecture was a fair amount of the project on its own!). Thanks for stopping by, and we hope you enjoy the website!
"""
)


giphy_url = "https://giphy.com/embed/f9NaK0iIjpY5Vm80a0"

st.components.v1.html(
    f'<div style="display:flex; justify-content:center;"><iframe src="{giphy_url}" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'
)


st.info("Click on the left sidebar menu to navigate through each topic.")
