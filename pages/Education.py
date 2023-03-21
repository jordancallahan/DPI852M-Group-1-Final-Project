import streamlit as st
import pandas as pd
import plotly.express as px



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

st.title("Science and Technology in Education")


st.markdown(
    """
    Research and development (R&D) spending and science and technology education in schools are closely linked in the United States. R&D is a key driver of innovation, which in turn fuels economic growth and prosperity. Science and technology education provides the foundation for a workforce that can effectively participate in R&D activities. When schools prioritize science and technology education, they help to create a pipeline of skilled workers who can contribute to R&D efforts in various fields. Additionally, R&D spending can help to support science and technology education initiatives in schools, providing funding for equipment, resources, and training programs.
    """
)

#College Enrollment

st.subheader(" College Enrollment in the US")

st.markdown(        
    """ College enrollment and R&D efforts are closely linked in the United States. Colleges and universities are critical hubs for R&D activities, with many institutions conducting cutting-edge research across a wide range of fields. At the same time, college enrollment plays a crucial role in fostering a skilled workforce that can effectively contribute to R&D efforts. By pursuing advanced degrees in fields such as science, technology, engineering, and mathematics (STEM), students can develop the knowledge and skills needed to engage in innovative research and development work. Additionally, colleges and universities can serve as important incubators for new ideas and technologies, with students and faculty often collaborating to bring new products and services to market.
    """
)

html = """
<div class='tableauPlaceholder' id='viz1679435084441' style='position: relative'><noscript><a href='#'><img alt='Immediate college enrollment rates among high school completers, by institution type: 2008–18  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;CollegeEnrollment_16794151625150&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CollegeEnrollment_16794151625150&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;CollegeEnrollment_16794151625150&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1679435084441');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""

st.components.v1.html(html, width=800, height=600)

#PISA scores

st.subheader("PISA Scores in the US")

st.markdown(        
    """ The average scores of US 15-year-old students on the Program for International Student Assessment (PISA) math and science scales are important indicators of the country's competitiveness in the global economy. These scores are used to compare the performance of US students with their peers in other countries and provide insight into the effectiveness of education policies and practices. Improving PISA scores in math and science is crucial for developing a workforce that can compete in the fields of science, technology, engineering, and mathematics (STEM).
    """
)


html = """
<div class='tableauPlaceholder' id='viz1679435493649' style='position: relative'><noscript><a href='#'><img alt='Average scores of U.S. 15-year-old students on the PISA mathematics and science literacy scales: 2003–18 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Av&#47;AverageScoresofUS15YOStudentsonthePISAMathandScienceScales03-18&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='AverageScoresofUS15YOStudentsonthePISAMathandScienceScales03-18&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Av&#47;AverageScoresofUS15YOStudentsonthePISAMathandScienceScales03-18&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1679435493649');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""
st.components.v1.html(html, width=800, height=600)

#NEAP scores

st.subheader("NEAP Scores in the US")

st.markdown(        
    """ The average scores of US students in grades 4 and 8 on the National Assessment of Educational Progress (NAEP) mathematics assessment are important indicators of the country's progress in improving math education. These scores are used to track improvements over time and identify areas where additional resources and support are needed. Improving NAEP math scores is critical for developing a skilled workforce that can compete in the global economy, as math skills are essential in many fields, including science, engineering, and technology.
    """
)


html = """
<div class='tableauPlaceholder' id='viz1679435718807' style='position: relative'><noscript><a href='#'><img alt='Average scores of students in grades 4 and 8 on the NAEP mathematics assessment: 1990–2019 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Av&#47;AverageScoresGrades4and8&#47;Sheet2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='AverageScoresGrades4and8&#47;Sheet2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Av&#47;AverageScoresGrades4and8&#47;Sheet2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1679435718807');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""
st.components.v1.html(html, width=800, height=600)