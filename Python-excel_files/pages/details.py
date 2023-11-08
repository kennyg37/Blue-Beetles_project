import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import random


st.set_page_config(page_title='Detailed LFS Data', page_icon=':pie_chart:', layout='wide')
st.title("detailed Labor force data")
excel_file = 'excel_data.xlsx'

if excel_file is not None:
    #all_sheets = pd.ExcelFile(excel_file)
    all_sheets = pd.read_excel(excel_file, sheet_name=None)

    selected_option = st.selectbox('select a type of presentation', ['Table', 'Chart'])

    if selected_option == 'Table':
        selected_sheet = st.selectbox("Select a sheet:", list(all_sheets.keys()), key='tables')
        selected_data = all_sheets[selected_sheet]
    
        selected_data = selected_data.fillna('')
        selected_data= selected_data.drop_duplicates()
        selected_data= selected_data.reset_index(drop=True)
    
        st.write(selected_data)

        if selected_sheet == 'Table 8':
            st.write(selected_data.head(10))
            st.title('Data Vizualization')

    elif selected_option == 'Chart':
        selected_chart = st.selectbox("Select a chart:", list(all_sheets.keys()), key='charts')
        selected_chart_data = all_sheets[selected_chart]
        if selected_chart == 'List Of Tables':
            selected_chart_data = selected_chart_data.fillna('')
            selected_chart_data= selected_chart_data.drop_duplicates()
            selected_chart_data= selected_chart_data.reset_index(drop=True)
            st.write(selected_chart_data)
        else:
            for sheet_name, sheet_data in all_sheets.items():
                if sheet_name == selected_chart:
                    st.subheader(f"Displaying chart for {sheet_name}")
                    if len(sheet_data.columns) >= 2:
                        column_names = list(sheet_data.columns)
                        x_column = column_names[0]
                        y_column = column_names[2]
                        fig = px.scatter(sheet_data, x=x_column, y=y_column, title=f"Chart for {sheet_name}")
                        st.plotly_chart(fig, use_container_width=True)

                        x_column = column_names[0]
                        y_column = column_names[3]
                        urban_column = column_names[4]
                        fig2 = px.scatter(sheet_data, x=x_column, y=y_column, title=f"Chart for {sheet_name}")
                        st.plotly_chart(fig2, use_container_width=True)
                        fig3 = px.scatter(sheet_data, x=x_column, y=urban_column, title=f"Chart for {sheet_name}")
                        st.plotly_chart(fig3, use_container_width=True)
            
                else:
                    pass