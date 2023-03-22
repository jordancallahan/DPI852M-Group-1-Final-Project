import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


st.title("Higher Education in Science and Engineering")

st.sidebar.info(
    """
    - Web App [URL](https://jordancallahan-dpi852m-group-1-final-project-home-page-ld7qtk.streamlit.app/)
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

st.write("This Streamlit app displays interactive data visualizations based on the research and data from the "
         "[Higher Education in Science and Engineering](https://ncses.nsf.gov/pubs/nsb20223/executive-summary)")


##  U.S. Institutions Providing S&E Higher Education
st.write("## Institutions in S&E Higher Education")

st.write("These charts show the percent distribution of institutions providing S&E higher education by level of degree.")

data = pd.DataFrame({
        'Institutions and degrees': ['Institutions', 'All degrees', 'S&E degrees'],
        'Public': [48.1, 87.8, 92.9],
        'Private nonprofit': [29.1, 5.5, 3.2],
        'Private for-profit': [22.8, 6.7, 3.9]}).set_index('Institutions and degrees')

fig = px.bar(data, orientation='h', barmode='stack')
fig.update_layout(title='Associate\'s Degrees', xaxis_title='', yaxis_title='Institutions and degrees', legend_title=None, legend=dict(orientation="h"))
fig.update_layout(height=400)

st.plotly_chart(fig)

data = pd.DataFrame({
        'Institutions and degrees': ['Institutions', 'All degrees', 'S&E degrees'],
        'Public': [31.0, 66.3, 71.5],
        'Private nonprofit': [56.5, 28.8, 26.6],
        'Private for-profit': [12.5, 4.9, 1.9]}).set_index('Institutions and degrees')

fig = px.bar(data, orientation='h', barmode='stack')
fig.update_layout(title='Bachelor\'s  Degrees', xaxis_title='', yaxis_title='Institutions and degrees', legend_title=None, legend=dict(orientation="h"))
fig.update_layout(height=400)
st.plotly_chart(fig)

data = pd.DataFrame({
        'Institutions and degrees': ['Institutions', 'All degrees', 'S&E degrees'],
        'Public': [28.3, 46.1, 54.1],
        'Private nonprofit': [61.8, 45.9, 41.9],
        'Private for-profit': [9.9, 8.0, 4.1]}).set_index('Institutions and degrees')

fig = px.bar(data, orientation='h', barmode='stack')
fig.update_layout(title='Master\'s  Degrees', xaxis_title='', yaxis_title='Institutions and degrees', legend_title=None, legend=dict(orientation="h"))
fig.update_layout(height=400)
st.plotly_chart(fig)

data = pd.DataFrame({
        'Institutions and degrees': ['Institutions', 'All degrees', 'S&E degrees'],
        'Public': [40.7, 60.6, 66.4],
        'Private nonprofit': [55.2, 33.4, 29.0],
        'Private for-profit': [4.0, 6.0, 4.6]}).set_index('Institutions and degrees')

fig = px.bar(data, orientation='h', barmode='stack')
fig.update_layout(title='Doctoral Degrees', xaxis_title='', yaxis_title='Institutions and degrees', legend_title=None, legend=dict(orientation="h"))
fig.update_layout(height=400)
st.plotly_chart(fig)

st.write("## Cost of Undergraduate Education")

data = pd.DataFrame({
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    'State support for higher education per full-time equivalent student (2012 constant $)': [7360, 7346, 7126, 6648, 6218, 6222, 6565, 6766, 6908, 6266, 5634, 5533, 5198, 5285, 5598, 5928, 6073, 6230, 6212, 6407],
    'Average undergraduate charge at public 4-year institutions as a percentage of disposable personal income (%)': [31.5, 31.8, 32.6, 33.5, 34.8, 36.0, 36.1, 36.7, 37.4, 40.1, 41.1, 41.8, 42.2, 44.2, 43.6, 43.4, 43.7, 42.5, 41.6, 41.4]
})

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=data['Year'], y=data['State support for higher education per full-time equivalent student (2012 constant $)'], name='State support for higher education per full-time equivalent student (2012 constant $)'),
              secondary_y=False)
fig.add_trace(go.Scatter(x=data['Year'], y=data['Average undergraduate charge at public 4-year institutions as a percentage of disposable personal income (%)'], name='Average undergraduate charge at public 4-year institutions as a percentage of disposable personal income (%)'),
              secondary_y=True)

fig.update_layout(title='State support for higher education vs Average undergraduate charge at public 4-year institutions',
                  xaxis_title='Year', 
                  legend=dict(orientation="h"))

fig.update_yaxes(title_text='Dollar', secondary_y=False)
fig.update_yaxes(title_text='Percent', secondary_y=True)

st.plotly_chart(fig)

st.write("""

For many people, college affordability is still a matter of concern. The average cost of undergraduate education at public four-year 
institutions has risen as a percentage of disposable personal income, climbing from about 33% 
in the early 2000s to 41% in 2019. However, this figure peaked at approximately 44% 
in 2013 and has decreased since then. State support for higher education per full-time equivalent 
student has generally increased since 2012, but it remains lower in constant dollars than it was in most of the 2000s, with a value of $6,407 in 2019.

""")

## Demographic Attributes of Science and Engineering Degree Recipients
st.write("## Demographic Attributes of Science and Engineering Degree Recipients")

st.write("""

Regarding the demographic patterns outlined in this section, racial and ethnic groups are benchmarked against U.S. citizens and permanent residents, 
while sex is benchmarked  against the overall totals regardless of citizenship.

""")

data = pd.DataFrame({
    'Race': ['Black', 'Black', 'Black', 'Black', 'Black', 'Hispanic', 'Hispanic', 'Hispanic', 'Hispanic', 'Hispanic', 'American Indian or Alaska Native', 'American Indian or Alaska Native', 'American Indian or Alaska Native', 'American Indian or Alaska Native', 'American Indian or Alaska Native', 'Native Hawaiian or Other Pacific Islander', 'Native Hawaiian or Other Pacific Islander', 'Native Hawaiian or Other Pacific Islander', 'Native Hawaiian or Other Pacific Islander', 'Native Hawaiian or Other Pacific Islander', 'More than one race', 'More than one race', 'More than one race', 'More than one race', 'More than one race', 'Asian', 'Asian', 'Asian', 'Asian', 'Asian', 'White', 'White', 'White', 'White', 'White'],
    'Degree': ["U.S. population (ages 20–34)", "Associate's degree recipients", "Bachelor's degree recipients", "Master's degree recipients", "Doctoral degree recipients", "U.S. population (ages 20–34)", "Associate's degree recipients", "Bachelor's degree recipients", "Master's degree recipients", "Doctoral degree recipients", "U.S. population (ages 20–34)", "Associate's degree recipients", "Bachelor's degree recipients", "Master's degree recipients", "Doctoral degree recipients", "U.S. population (ages 20–34)", "Associate's degree recipients", "Bachelor's degree recipients", "Master's degree recipients", "Doctoral degree recipients", "U.S. population (ages 20–34)", "Associate's degree recipients", "Bachelor's degree recipients", "Master's degree recipients", "Doctoral degree recipients", "U.S. population (ages 20–34)", "Associate's degree recipients", "Bachelor's degree recipients", "Master's degree recipients", "Doctoral degree recipients", "U.S. population (ages 20–34)", "Associate's degree recipients", "Bachelor's degree recipients", "Master's degree recipients", "Doctoral degree recipients"],
    'Percent': [14.2, 10.1, 8.7, 11.3, 8.1, 21.3, 31.1, 16.3, 12.2, 8.4, 0.8, 1.0, 0.4, 0.4, 0.4, 0.2, 0.4, 0.2, 0.2, 0.2, 2.5, 4.1, 4.3, 3.6, 3.2, 6.6, 9.7, 11.3, 11.1, 10.6, 54.4, 43.7, 58.8, 61.2, 69.1]
})

data_pivot = data.pivot(index='Degree', columns='Race', values='Percent')

fig = px.bar(data_pivot, orientation='h', barmode='stack', title='Representation of race or ethnicity in the U.S. population and among S&E degree recipients: 2019')
fig.update_layout(xaxis_title ='Percent', 
                  yaxis_title ='Selected Population', 
                  legend_title = None,
                  legend=dict(orientation="h"))


st.plotly_chart(fig)

st.write("The proportion of certain demographic groups among S&E degree recipients varies from their respective shares in the overall U.S. population.")

data = pd.DataFrame({'Field': ['All fields', 'All S&E fields', 'Engineering', 'Agricultural sciences', 'Biological sciences', 'Computer sciences', 'Earth, atmospheric, and ocean sciences', 'Mathematics and statistics', 'Physical sciences', 'Psychology', 'Social sciences'],
        'Associate\'s degrees': [60.8, 47.7, 16.5, 44.6, 69.8, 20.0, 39.1, 30.9, 42.9, 76.5, 69.0],
        'Bachelor\'s degrees': [57.4, 49.7, 22.7, 58.3, 63.7, 20.6, 41.7, 42.3, 40.6, 79.1, 55.8],
        'Master\'s degrees': [60.9, 45.8, 26.3, 58.4, 60.3, 32.8, 44.2, 42.7, 35.8, 80.2, 57.9],
        'Doctoral degrees': [50.8, 45.8, 24.6, 49.7, 51.9, 22.9, 41.3, 29.6, 32.9, 71.8, 50.1]})

fig = px.bar(data, x=['Associate\'s degrees', 'Bachelor\'s degrees', 'Master\'s degrees', 'Doctoral degrees'], y='Field', orientation='h', barmode='group', title = 'S&E degrees awarded to women, by degree level and field: 2019')
fig.update_layout(xaxis_title ='Percent', yaxis_title ='Field', legend_title = None, legend=dict(orientation="h"))

fig.update_layout(height=800)

st.plotly_chart(fig)

st.write("On average, women earn more than half of all higher education degrees, but their attainment is lower in S&E fields. While some areas have seen a reduction or elimination of gender disparities, there are still persistent gaps in others.")


st.write("## International S&E Higher Education and Student Mobility")

st.write("This chart shows number of doctoral degree graduates per country.")

data = pd.DataFrame(
{'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018],
        'Brazil': [None, None, None, None, None, None, None, None, None, None, None, None, None, None, 9124, 9414, 10469, 10752, 11365],
        'China': [7766, 8153, 9523, 12238, 14858, 17595, 22953, 26582, 28439, 31423, 31410, 32208, 32331, 33490, 34103, 34440, 35147, 37506, 39768],
        'France': [6640, 6957, 6957, 5639, 5639, 6868, 6854, 7402, 7835, 8356, 9025, 9466, 9692, 9731, 10023, 10020, 9564, 9755, 8987],
        'Germany': [11888, 11271, 10618, 10340, 10107, 10740, 10871, 11084, 11887, 11691, 12576, 13281, 13666, 14936, 14912, 15957, 15871, 15761, 15061],
        'India': [5541, 5504, 5637, 6471, 7636, 7537, 7982, None, None, None, None, 14191, 15132, 15500, 13616, 15780, 17905, 23246, 26890],
        'Japan': [7089, 7401, 7461, 7581, 7912, 7658, 8122, 8017, 7761, 7396, 7470, 7100, 7100, 6791, 7357, 7540, 7391, 6745, 6754],
        'South Korea': [2914, 3013, 3294, 3280, 3629, 3817, 3943, 3796, 3867, 3994, 4421, 5454, 5713, 5963, 6087, 6104, 6557, 6903, 7077],
        'Span': [2937, 3124, 3394, 3741, 3965, 3659, 3684, 3825, 3852, 4167, 5101, 5576, 5812, 6474, 6708, 7174, 8373, 10711, 9480], 
        'United Kingdom': [7481, 8878, 8722, 8971, 9267, 9582, 9916, 10524, 9674, 10425, 11322, 11859, 12103, 14732, 14271, 15338, 15338, 15757, 17366], 
        'United States': [26086, 26060, 24992, 26011, 22797, 29216, 30289, 32394, 33423, 33953, 33672, 35113, 36356, 37951, 39682, 39933, 39710, 40319, 41071]
})

data = data.melt(id_vars=['Year'], var_name='Country', value_name='Value')

fig = px.line(data, x="Year", y="Value", color='Country')

fig.update_layout(xaxis_title ='Year', 
                  yaxis_title ='Number of Graduates', 
                  legend_title = None,
                  legend=dict(orientation="h"))

fig.update_layout(height=700)

st.plotly_chart(fig)

st.write("The United States has been awarding the most S&E doctorates in the world for many years (41,000 in 2018). However, China is getting closer to catching up (40,000 in 2018).")


