import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import numpy as np


st.title("Public Opinion on Science and Technology")

st.write(
    "This Streamlit app displays interactive data visualizations based on the research and data from the "
    "[NSB 2020 Science and Engineering Indicators Report](https://ncses.nsf.gov/pubs/nsb20207/executive-summary), specifically from Chapter 7."
)

st.write("## Public Confidence in Leaders of Institutions (2018)")

st.write(
    "This chart shows the percentage of people expressing a great deal of confidence in leaders of various institutions, based on the 2018 General Social Survey."
)

# Data for Public Confidence in Leaders of Institutions (2018)
confidence_data = pd.DataFrame(
    {
        "Institution": [
            "Scientific community",
            "The military",
            "The Supreme Court",
            "Organized religion",
            "Banks and financial institutions",
            "The press",
            "Congress",
        ],
        "Percentage": [44, 33, 26, 20, 14, 9, 8],
    }
)

# Bar chart for Public Confidence in Leaders of Institutions (2018)
confidence_chart = go.Figure(
    go.Bar(
        x=confidence_data["Institution"],
        y=confidence_data["Percentage"],
        marker_color="mediumseagreen",
    )
)
confidence_chart.update_layout(
    title="Percentage of People Expressing a Great Deal of Confidence in Leaders of Institutions (2018)",
    xaxis_title="Institution",
    yaxis_title="Percentage",
    showlegend=False,
)

st.plotly_chart(confidence_chart)

st.write(
    "As shown in the chart, leaders of the scientific community rank highest in terms of public confidence, with 44% of respondents expressing a great deal of confidence in them. Congress ranks lowest, with only 8% of respondents expressing the same level of confidence."
)

st.write("## Public Opinion on Federal Funding for Scientific Research (2006-2018)")

st.write(
    "The chart below shows public opinion on federal funding for scientific research between 2006 and 2018, based on the General Social Survey."
)

# Data for Public Opinion on Federal Funding for Scientific Research (2006-2018)
funding_data = pd.DataFrame(
    {
        "Year": [2006, 2008, 2010, 2012, 2014, 2016, 2018],
        "Too little": [41, 39, 42, 44, 43, 41, 45],
        "About right": [43, 46, 45, 44, 45, 46, 44],
        "Too much": [11, 10, 10, 10, 9, 11, 9],
    }
)

# Line chart for Public Opinion on Federal Funding for Scientific Research (2006-2018)
funding_chart = go.Figure()

funding_chart.add_trace(
    go.Scatter(
        x=funding_data["Year"],
        y=funding_data["Too little"],
        mode="lines+markers",
        name="Too little",
        marker_color="royalblue",
    )
)
funding_chart.add_trace(
    go.Scatter(
        x=funding_data["Year"],
        y=funding_data["About right"],
        mode="lines+markers",
        name="About right",
        marker_color="firebrick",
    )
)
funding_chart.add_trace(
    go.Scatter(
        x=funding_data["Year"],
        y=funding_data["Too much"],
        mode="lines+markers",
        name="Too much",
        marker_color="orange",
    )
)

funding_chart.update_layout(
    title="Public Opinion on Federal Funding for Scientific Research (2006-2018)",
    xaxis_title="Year",
    yaxis_title="Percentage",
)
st.plotly_chart(funding_chart)

st.write("## Interest in S&T News (2006-2018)")

st.write(
    "This chart shows the percentage of people who report being very or moderately interested in news about science and technology from 2006 to 2018."
)

# Data for Interest in S&T News (2006-2018)
interest_data = pd.DataFrame(
    {
        "Year": [2006, 2008, 2010, 2012, 2014, 2016, 2018],
        "Percentage": [75, 73, 76, 79, 74, 76, 74],
    }
)

# Line chart for Interest in S&T News (2006-2018)
interest_chart = go.Figure(
    go.Scatter(
        x=interest_data["Year"],
        y=interest_data["Percentage"],
        mode="lines+markers",
        marker_color="blue",
    )
)
interest_chart.update_layout(
    title="Interest in S&T News (2006-2018)",
    xaxis_title="Year",
    yaxis_title="Percentage",
)
st.plotly_chart(interest_chart)

st.write("## Views on the Promise and Concerns of Science and Technology (2018)")

st.write(
    "This chart shows the percentage of people who believe that the benefits of science and technology outweigh the potential harms or vice versa, based on the 2018 General Social Survey."
)

# Data for Views on the Promise and Concerns of S&T (2018)
views_data = pd.DataFrame(
    {
        "Aspect": ["Benefits > Harms", "Benefits = Harms", "Benefits < Harms"],
        "Percentage": [49, 34, 17],
    }
)

# Pie chart for Views on the Promise and Concerns of S&T (2018)
views_chart = px.pie(
    views_data,
    values="Percentage",
    names="Aspect",
    title="Views on the Promise and Concerns of Science and Technology (2018)",
)
st.plotly_chart(views_chart)

st.write("## Public Understanding of the Scientific Method (2006-2018)")

st.write(
    "This chart shows the percentage of people who were able to correctly identify the scientific method as 'testing ideas with evidence from experiments,' based on the General Social Survey from 2006 to 2018."
)

# Data for Public Understanding of the Scientific Method (2006-2018)
understanding_data = pd.DataFrame(
    {
        "Year": [2006, 2008, 2010, 2012, 2014, 2016, 2018],
        "Percentage": [42, 46, 45, 47, 49, 50, 50],
    }
)

# Line chart for Public Understanding of the Scientific Method (2006-2018)
understanding_chart = go.Figure(
    go.Scatter(
        x=understanding_data["Year"],
        y=understanding_data["Percentage"],
        mode="lines+markers",
        marker_color="darkorange",
    )
)
understanding_chart.update_layout(
    title="Public Understanding of the Scientific Method (2006-2018)",
    xaxis_title="Year",
    yaxis_title="Percentage",
)
st.plotly_chart(understanding_chart)

st.write("## Opinion on Science's Effect on the Environment (2018)")

st.write(
    "This chart displays the percentage of people who believe that science has made the environment better, has had no effect, or has made it worse. Data is based on the 2018 General Social Survey."
)

# Data for Opinion on Science's Effect on the Environment (2018)
environment_data = pd.DataFrame(
    {
        "Opinion": ["Better", "No effect", "Worse"],
        "Percentage": [65, 18, 17],
    }
)

# Bar chart for Opinion on Science's Effect on the Environment (2018)
environment_chart = go.Figure(
    go.Bar(
        x=environment_data["Opinion"],
        y=environment_data["Percentage"],
        marker_color="dodgerblue",
    )
)
environment_chart.update_layout(
    title="Opinion on Science's Effect on the Environment (2018)",
    xaxis_title="Opinion",
    yaxis_title="Percentage",
    showlegend=False,
)

st.plotly_chart(environment_chart)

st.write(
    "According to the 2018 General Social Survey, 65% of respondents believe that science has made the environment better, while 17% think it has made the environment worse. A smaller group of 18% believe science has had no effect on the environment."
)

st.write("## Importance of Government Funding by Field (2018)")

st.write(
    "This chart presents the percentage of people who think the government spends too little on various fields of research. Data is based on the 2018 General Social Survey."
)

# Data for Importance of Government Funding by Field (2018)
funding_field_data = pd.DataFrame(
    {
        "Field": ["Health", "Environment", "Basic science", "Space exploration"],
        "Percentage": [70, 62, 51, 33],
    }
)

# Bar chart for Importance of Government Funding by Field (2018)
funding_field_chart = go.Figure(
    go.Bar(
        x=funding_field_data["Field"],
        y=funding_field_data["Percentage"],
        marker_color="teal",
    )
)
funding_field_chart.update_layout(
    title="Importance of Government Funding by Field (2018)",
    xaxis_title="Field",
    yaxis_title="Percentage",
    showlegend=False,
)

st.plotly_chart(funding_field_chart)

st.write(
    "The 2018 General Social Survey data shows that a majority of respondents believe the government spends too little on health (70%) and environmental (62%) research. In contrast, a smaller percentage of respondents feel the same way about basic science (51%) and space exploration (33%)."
)

st.write("## Public Knowledge of Selected Scientific Facts (2018)")

st.write(
    "This heatmap illustrates the percentage of correct responses by the public to various scientific questions. Data is based on the 2018 General Social Survey."
)

# Data for Public Knowledge of Selected Scientific Facts (2018)
knowledge_data = pd.DataFrame(
    {
        "Question": [
            "Antibiotics",
            "Evolution",
            "Astronomy",
            "Geology",
            "Radiation",
            "Vaccines",
            "Genetics",
        ],
        "Percentage": [84, 81, 75, 71, 68, 59, 48],
    }
)

# Heatmap for Public Knowledge of Selected Scientific Facts (2018)
knowledge_matrix = np.outer(np.array(knowledge_data["Percentage"]), np.ones((1, 1)))
knowledge_chart = px.imshow(
    knowledge_matrix,
    labels=dict(x="", y=""),
    x=[0],
    y=knowledge_data["Question"],
    color_continuous_scale="viridis",
)
knowledge_chart.update_xaxes(showticklabels=False)
knowledge_chart.update_yaxes(tickfont=dict(size=12))
knowledge_chart.update_layout(
    title="Public Knowledge of Selected Scientific Facts (2018)",
    xaxis_title="",
    yaxis_title="Question",
    coloraxis_colorbar=dict(title="Percentage"),
)

st.plotly_chart(knowledge_chart)

st.write(
    "According to the 2018 General Social Survey, the public had the highest level of understanding in the area of antibiotics, with 84% of respondents answering the relevant question correctly. In contrast, the area with the lowest level of understanding was genetics, with only 48% of respondents answering the related question correctly."
)
