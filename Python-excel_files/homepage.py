import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

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
    st.write('You can find the summary on the data menu or more details following the link below')
    st.markdown('[Detailed data](details)')

#The data menu displays the data summary and the charts of the basic data in 
# contrast to the data page which displays the detailed data 

elif menu == 'Data':
    st.title('Data Summary')

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
    st.image()
    paragraph2 = """ Blue Beatles is a team of two aspiring programmers Ken Ganza and Tuyishime Johnson.
    Both Ken and Johnson are students at the African Leadership University pursuing a degree in Software Engineering and they share
    the love of programming and data science. In collaboration with NISR they designed this dashboard to help the public access the data"""
    st.write(paragraph2)

else:
    st.write('This is the home page')
    st.write('We will be adding more content soon')
    st.write('Please check back later')


