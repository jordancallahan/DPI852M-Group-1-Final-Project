import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")

st.sidebar.info(
    """
    - Web App URL: <insert web app details>
    - GitHub repository: <https://github.com/jordancallahan/DPI852M-Group-1-Final-Project>
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

st.markdown(
    """
    We made this multi-page web app to vizually explore science and R&D spending - the project aims to consider questions such as:
1.       How does science and R&D spending vary across different regions of the US and the world?
2.       What are the trends in higher education in science and engineering?
3.       What are the links between science and R&D spending with innovation?
4.       What are the trends in K-12 education?
5.       What influence has this had on the US labor force?
6.       How have public attitudes changed towards science and technology spending?

Much of this project was created using [streamlit](https://streamlit.io) and open-source mapping libraries, such as [leafmap](https://leafmap.org), [geemap](https://geemap.org)
    """
)
