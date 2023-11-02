import streamlit as st
import pandas as pd
import numpy as np
#import plotly.express as px


st.set_page_config(page_title='NISR LFS', page_icon=':bar_chart:', layout='wide')
class Basic:
    #creating a class Basic for more organisation throught the app

    def __init__(self):
        
        #initialising the class

        self.data = pd.read_excel('excel_data.xlsx')
        self.data = self.data.dropna()
        self.data = self.data.drop_duplicates()
        self.data = self.data.reset_index(drop=True)

    def menuBar(self):
        
        #creating a menu bar for the application for navigation and better user experience
        
        self.menu = st.sidebar.selectbox('Menu', ['Home', 'Data', 'About'])
        return self.menu
    

basic_app = Basic()

#creating an instance of the class Basic, so that we can use it's methods

menu = basic_app.menuBar()
if menu == 'Home':
    st.title('Welcome to the NISR LFS Dashboard')
    st.write("<p style= 'font-style: italic;'>This dashboard showcases the 2022 Laborforce Survey carried out by Nisr</p>", unsafe_allow_html=True)
    st.write('You can find the summary on the data menu or more details following the link below')
    st.markdown('[Detailed data](details)')
elif menu == 'Data':
    st.write('This is the data page')
    st.write('We will be adding more content soon')
    st.write('Please check back later')
elif menu == 'About':
    st.write('This is the about page')
    st.write('We will be adding more content soon')
    st.write('Please check back later')
else:
    st.write('This is the home page')
    st.write('We will be adding more content soon')
    st.write('Please check back later')


