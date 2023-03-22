import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(layout="centered")

st.title(
    "The STEM Labor Force of Today: Scientists, Engineers, and Skilled Technical Workers"
)

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

st.write(
    "This page displays interactive data visualizations based on the research and data from the "
    "[The State of U.S. Science and Engineering 2022](https://ncses.nsf.gov/pubs/nsb20221/u-s-and-global-stem-education-and-labor-force#demographic-composition-of-the-stem-workforce)"
)


## The STEM Labor Market and the Economy
st.write("## The STEM Labor Market and the Economy")

st.write(
    "This chart shows the proportion of occupations in the STEM fields, based on educational attainment."
)

nodes = [
    "STEM",
    "Bachelor's degree or higher",
    "Without a bachelor's degree",
    "Non-STEM",
    "S&E",
    "S&E-Related",
    "Middle Skill",
]
links = [
    {"source": 0, "target": 1, "value": 16241},
    {"source": 0, "target": 2, "value": 19853},
    {"source": 3, "target": 1, "value": 40287},
    {"source": 3, "target": 2, "value": 79042},
    {"source": 1, "target": 4, "value": 6559},
    {"source": 1, "target": 5, "value": 7917},
    {"source": 1, "target": 6, "value": 1765},
    {"source": 2, "target": 4, "value": 2017},
    {"source": 2, "target": 5, "value": 5180},
    {"source": 2, "target": 6, "value": 12657},
]

fig = go.Figure(
    data=[
        go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=nodes,
                color=(
                    "#28847D",
                    "#740060",
                    "#E2523E",
                    "#A29171",
                    "#E1167A",
                    "#0D1444",
                    "yellow",
                ),
            ),
            link=dict(
                source=[link["source"] for link in links],
                target=[link["target"] for link in links],
                value=[link["value"] for link in links],
            ),
        )
    ]
)

fig.update_layout(
    title_text="U.S. Workforce (in thousands), by STEM occupational and educational level: 2019"
)

fig.update_layout(height=700)

st.plotly_chart(fig)

st.write(
    """

The STEM workforce in the U.S. includes over 36 million people who have jobs that need knowledge and 
skills in science, technology, engineering, and math. This is about 23% of all the jobs in the country. Some of these STEM jobs 
need a college degree, and these are called S&E occupations and S&E-related occupations. Around 76% of the 8.6 million people in S&E jobs 
have a college degree, while 2 million do not. Similarly, 60% of the 13.1 million people in S&E-related jobs have a college degree, while 5.2 million do not.
There are also middle-skill STEM jobs that don't need a college degree, like jobs in repair, construction, and production. Of the 14.4 million people in these 
jobs, 88% do not have a college degree.

"""
)


st.write("## Demographic Composition of the STEM Workforce")

data = {
    "Education and sex or race or ethnicity": [
        "Bachelor's degree or higher: women",
        "Bachelor's degree or higher: Hispanic",
        "Bachelor's degree or higher: Black",
        "Bachelor's degree or higher: AIAN",
        "Without a bachelor's degree: women",
        "Without a bachelor's degree: Hispanic",
        "Without a bachelor's degree: Black",
        "Without a bachelor's degree: AIAN",
    ],
    "2010": [41.9, 5.5, 6.0, 0.2, 26.1, 15.0, 8.7, 0.6],
    "2019": [44.2, 7.7, 7.1, 0.2, 25.8, 19.4, 9.7, 0.6],
}

df = pd.DataFrame(data)

fig = px.bar(
    df,
    x="Education and sex or race or ethnicity",
    y=["2010", "2019"],
    barmode="group",
    title="Education Between Race and Sex (in Percent)",
)

fig.update_layout(
    xaxis_title="",
    yaxis_title="Percent",
    legend_title=None,
    legend=dict(orientation="v"),
)
fig.update_layout(height=800)

st.plotly_chart(fig)

st.write(
    """

Women are underrepresented in the STEM workforce, accounting for 34% in 2019, despite their representation 
in the employed US population being 48%. Although the share of women with a bachelor's degree or higher in STEM has 
increased from 42% to 44%, their distribution across different STEM occupations remains uneven, with low representation 
in physical sciences, computer science, and engineering. Additionally, Blacks, Hispanics, and American Indians or Alaska Natives 
were underrepresented in STEM, with a collective representation of 23% in 2019, primarily due to underrepresentation among STEM workers 
with a bachelor's degree or higher.

"""
)


data = pd.DataFrame(
    {
        "Occupation": [
            "S&E workers",
            "S&E: computer and mathematical scientists",
            "S&E: life scientists",
            "S&E: engineers",
            "S&E: social and related scientists",
            "S&E: physical and related scientists",
            "S&E-related workers",
            "Non-S&E workers",
        ],
        "Bachelor's": [21.0, 24.6, 17.1, 17.2, 12.8, 11.4, 18.7, 12.9],
        "Master's": [38.2, 47.3, 30.1, 34.6, 16.2, 20.5, 19.4, 14.5],
        "Doctorate": [44.8, 60.3, 50.0, 57.1, 20.6, 42.4, 40.2, 23.2],
    }
)

fig = px.bar(
    data,
    x=["Bachelor's", "Master's", "Doctorate"],
    y="Occupation",
    title="Foreign-born college-educated workers by degree level and occupation in 2019",
    barmode="group",
    orientation="h",
)

fig.update_layout(
    xaxis_title="Percent",
    yaxis_title="Occuptation",
    legend_title=None,
    legend=dict(orientation="h"),
)

fig.update_layout(height=600)

st.plotly_chart(fig)

st.write(
    """

The percentage of foreign-born workers in the STEM workforce increased from 17% in 2010 to 19% in 2019, 
with those holding a bachelor’s degree or higher comprising a larger proportion (23%) than those without a bachelor’s degree (16%). 
Among foreign-born workers with a bachelor’s degree or higher, computer and mathematical scientists had the highest representation 
at all degree levels, accounting for 21% at the bachelor’s degree level, 38% at the master’s degree level, and 45% at the doctorate 
level in S&E occupations.

"""
)
