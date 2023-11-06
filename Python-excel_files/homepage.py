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
        st.title('Data summary')
        bar1 = px.bar(selected_data, x='Labour force indicators', y='Total', color='Male',  title='Summary labour force indicators, RLFS 2022')
        st.plotly_chart(bar1, use_container_width=True)

#The about page displays the information about the dashboard and the data used  giving credit to all the involved parties

elif menu == 'About':
    st.write('This is the about page')
    st.write('We will be adding more content soon')
    st.write('Please check back later')
else:
    st.write('This is the home page')
    st.write('We will be adding more content soon')
    st.write('Please check back later')


