import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.info(
    """
    - Web App URL: <insert web app details>
    - GitHub repository: <insert github repo>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
   Insert team details/contact
    """
)

st.title("R+D Expenditure, US and Worldwide")

st.markdown(
    """
    We made this multi-page web app to vizually explore science and R&D spending in the US with global comparisons. The project should aim to answer questions such as:
1.       How does science and R&D spending vary across different regions of the US and the world?
2.       What are the trends in higher education in science and engineering?
3.       What are the links between science and R&D spending with innovation?
4.       What are the trends in K-12 education?
5.       What influence has this had on the US labor force?
6.       How have public attitudes changed towards science and technology spending?

Much of this project was created using [streamlit](https://streamlit.io) and open-source mapping libraries, such as [leafmap](https://leafmap.org), [geemap](https://geemap.org)
    """
)

st.info("Click on the left sidebar menu to navigate through each topic.")

st.subheader("")
st.markdown(
    """
    insert more background text here - the gifs are a joke but we can add more text/video here
"""
)

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.image("https://github.com/jordancallahan/DPI852M-Group-1-Final-Project/blob/Andrew/data/gifs/chips.gif")
    st.image("https://github.com/jordancallahan/DPI852M-Group-1-Final-Project/blob/Andrew/data/gifs/science.gif")

with row1_col2:
    st.image("https://github.com/jordancallahan/DPI852M-Group-1-Final-Project/blob/Andrew/data/gifs/robot.gif")
    st.image("https://github.com/jordancallahan/DPI852M-Group-1-Final-Project/blob/Andrew/data/gifs/network.gif")