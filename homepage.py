import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import subprocess

subprocess.run(["pip", "install", "plotly==5.3.1"])

#We set the page title, icon and layout to wide to make the dashboard more appealing

st.set_page_config(page_title='NISR LFS', page_icon=':bar_chart:', layout='wide')
excel_file = 'excel_data.xlsx' 
selected_sheet_name = 'Table 1'

# Loads the data from the excel and filters the data to remove empty rows and columns

selected_data = pd.read_excel(excel_file, sheet_name=selected_sheet_name)
selected_data = selected_data.fillna('')
selected_data= selected_data.drop_duplicates()
selected_data= selected_data.reset_index(drop=True)



menu = st.sidebar.selectbox('Menu', ['Home', 'Data', 'About'])

#We create a sidebar to display the menu options to ease access to all parts of the dashboard

if menu == 'Home':
    st.title('Welcome to the NISR LFS Dashboard')
    st.write("<p style= 'font-style: italic;'>This dashboard showcases the 2022 Laborforce Survey carried out by Nisr</p>", unsafe_allow_html=True)
    st.write('You can find the data and visual summary on the data menu or more details following the link/page below')
    st.markdown('[Detailed data](details)')
    st.title('Executive Summary')
    executive_summary = """Rwanda redesigned LFS from bi-annual to quarterly basis since February 2019 to provide estimates of labour market indicators and monitor labour market trends on a quarterly basis.
The data collection on the size and characteristics of the labour force, employment, unemployment and other labour market characteristics of the population was carried out through four quarters of 2022, specifically in February, May, August and November. The survey was also designed to measure different forms of work, in particular, own-use production work and other components of labour underutilization including time-related underemployment and potential labour force in line with the international standards, adopted by the 19th International Conference of Labour Statisticians (ICLS) in 2013. All the key concepts used henceforth in this report (employment, unemployment, time related underemployment, labour underutilization, potential labour force, discouraged job seekers etc) are defined in annexe A of this report. The current report presents the results of the annual report of 2022 LFS obtained by combining all quarters of LFS in 2022 (February, May, August and November ).
The survey covered all persons living in private households, excluding the institutional population permanently residing in places such as hostels, health resorts, correctional establishments etc., as well as persons living at their work-sites and in seasonal dwellings. The resulting estimates of the main labour force indicators at the national level from the combined datasets have standard errors of about 0.5 percent.
 You can find the full report [here](https://www.nisr.gov.rw/fileadmin/user_upload/LFS_2022_Annual_Report.pdf)"""
    st.write(executive_summary)

#The data menu displays the data summary and the charts of the basic data in 
# contrast to the data page which displays the detailed data 

elif menu == 'Data':
    st.title('Data Summary')
    st.write('<p style = "font-weight: bold; font-style: italic;", >Note: This dashboard is a prototype, some data may appear manipulated incorrectly. However after pending approval everything will look as it should</p>', unsafe_allow_html=True)
    summary_paragraph = """According to the survey results, the working age population (16 years and above) was 7,963,586 of which 4,463,296 persons (56.0 percent) were in the labour force, while 3,500,290 were outside the labour force. For those in the labour force, 3,546,352 were employed, while 916,944 were unemployed. Among those outside the labour force, 1,310,734 persons were engaged wholly or mostly in subsistence foodstuff production (not classified as employment according to the 2013 international standards on statistics of work, employment and labour underutilization).
The annual unemployment rate stood at 20.5 percent, indicating that roughly for five persons in the labour force there was one person unemployed. The unemployment rate was higher among females (23.7 percent) than among males (17.9 percent) and higher among youth (25.6) than among adults (17.1 percent). It was relatively the same in the urban and rural areas (20.4 and 20.6 percent respectively)."""
    st.write(summary_paragraph)
    if selected_data.empty:
        st.write('No data available.')
    else:
        st.write(f'Displaying data from: {selected_sheet_name}. Summary labour force indicators, RLFS 2022')
        st.write(selected_data.head(10))
        st.title('Data Vizualization')

        selected_row = 3
        males_data = selected_data.iloc[selected_row, 2]
        females_data = selected_data.iloc[selected_row, 3]

        labels = ['Males', 'Females']
        values = [males_data, females_data]
        
        pie1 = px.pie(selected_data, values=values, names=labels, title='Employment rate Females vs Males')
        st.plotly_chart(pie1, use_container_width=True)

        rural_data = selected_data.iloc[selected_row, 5]
        urban_data = selected_data.iloc[selected_row, 4]
        custom_colors = ['grey', 'black']

        pie2 = px.pie(selected_data, values=[rural_data, urban_data], names=['Rural', 'Urban'], title='Employment rate Rural vs Urban', color_discrete_sequence=custom_colors)
        st.plotly_chart(pie2, use_container_width=True)

        
#The about page displays the information about the dashboard and the data used  giving credit to all the involved parties

elif menu == 'About':
    st.title('NISR')
    paragraph1 = """The National Institute of Statistics of Rwanda (NISR) is a public institution with a legal personality operating under the supervision of the Ministry of Finance and Economic Planning (MINECOFIN).
      It was created by the law n° 04/2013 of 08/02/2013.
      The mission of NISR is to provide relevant, timely and reliable statistical information for evidence-based decision making.
        The vision of NISR is to be a center of excellence in providing statistical information for evidence-based decision making.
        This dashboard in particular fulfils the core mission of NISR as it provides an insight into the labor market in Rwanda
    . This dasboard also fulfils the vision of NISR as it provides a platform for the public to access the data and make informed decisions.
    """
    st.write(paragraph1)
    st.title('Blue Beatles')
    paragraph2 = """ Blue Beatles is a team of two aspiring programmers Ken Ganza and Tuyishime Johnson.
    Both Ken and Johnson are students at the African Leadership University pursuing a degree in Software Engineering and they share
    the love of programming and data science. In collaboration with NISR they designed this dashboard to help the public access the data"""
    st.write(paragraph2)

else:
    st.write('This is the home page')
    st.write('We will be adding more content soon')
    st.write('Please check back later')


#adding some css to style the dashboard

st.markdown( 
    """
    <style>
    body {
        background-color: #16213e; 
        color: #ffffff; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    h1 {
        font-size: 2.5rem; 
        text-align: center;
        margin-top: 2rem;
        color: #64a6bd;
    }

    p {
        font-size: 1.2rem; 
        font-family: 'Tahoma', sans-serif;
        line-height: 1.5;
        margin-bottom: 1.5rem;
    }

    .plotly-graph-div, .plot-container {
        display: flex;
        justify-content: center;
    }

    /* Add more styles as needed */

    @media (max-width: 768px) {
        
        h1 {
            font-size: 2rem; /* Adjust font size for smaller screens */
        }
    }
</style>

""", unsafe_allow_html=True)