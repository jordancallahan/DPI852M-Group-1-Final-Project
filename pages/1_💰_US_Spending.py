import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="centered")

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


# Load data
data = pd.read_excel("data/tables/R_and_D_by_state.xlsx")

# Replace state names with their two-letter abbreviations
state_abbr = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

data["State"] = data["State"].map(state_abbr)

# Create chloroplet map
st.title("R+D Spending by State Over Time")
st.markdown(
    """ This chart examines the change in R+D spending over time at aggregate levels from state sources. 
    This is based on data from the National Science Foundation's [Survey of State Government Research and Development](https://www.nsf.gov/statistics/srvystaterd/)
    """
    )

fig = px.choropleth(
    data,
    locations="State",
    locationmode="USA-states",
    scope="usa",
    color_continuous_scale="blues",
    title="Spend between 2009 - 2021 ($m)",
    animation_frame="Year",
    color="Spend",
    range_color=[0, 30000000],
)


# show map
st.plotly_chart(fig)

# per capita map
st.markdown(
    """ This chart examines the change in R+D spending over time at per capita levels from state sources. 
    This is based on data from the National Science Foundation's [Survey of State Government Research and Development](https://www.nsf.gov/statistics/srvystaterd/)
    """
    )
fig = px.choropleth(
    data,
    locations="State",
    locationmode="USA-states",
    scope="usa",
    color_continuous_scale="reds",
    title="Spend between 2009 - 2021 per capita ($)",
    animation_frame="Year",
    color="Per Capita Spend",
    range_color=[0, 50],
)

# show map
st.plotly_chart(fig)

st.markdown(
    """
From an overall national view, research and development (R&D) spending in the United
States grew considerably between 2006 and 2021. This expansion is likely becuase of 
various factors, including increased government investments, a growing
emphasis on technological innovation, and the rise of private sector R&D efforts. The
US has maintained its position as one of the world's top spenders on R&D,
with industries such as technology, pharma, and aerospace driving much of this
investment. Federal policies, tax incentives, and funding programs have
played a central role in promoting research in both public and private remits.

From a state-by-state perspective, there have been noticable differences in R&D spending
across the time period examined. States with strong technology and research sectors, such as
California, Massachusetts, and Washington, have been at the forefront of
R&D expenditure through this period. These states benefit from the presence of major technology companies,
well-funded research institutions, and a high-skilled workforce, which all collectively
contribute to their high levels of investment. In other states, such as Texas and North
Carolina, R&D spending has also seen snotworthy growth, driven by factors such as the
expansion of universities, some targeted development initiatives, and the
growth of sectors like biotechnology and renewable energy.

That being said, not all states have experienced the same level of growth in this area. Some
states have weathered economic challenges over this period or have not been able to attract the same level
of investment. Factors such as geographic location, availability of
skilled labor, and the volume of research-intensive industries can 
impact a state's ability to increase R&D spending. Overall, the landscape of R&D
spending in the United States between 2006 and 2021 has been one of both growth and
disparity, with some states outpacing others in their pursuit of research-driven
innovation.
    """
)
