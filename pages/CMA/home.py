# this file uses matplotlib becasuse plotly works in a erratic way on the terminal
# it also uses numpy to help pandas format numbers automatically

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#this is the home function and it displays the summary of the data that is the the detailed_view.py data

def home():
    excel_file = 'excel_data.xlsx'
    selected_sheet_name = 'Table 1'

#checks if the excel file is not empty, if it is empty it displays a message and if it is not it filters the data

    if excel_file is not None:
        all_sheets = pd.read_excel(excel_file, sheet_name=None, skiprows=[0])
        selected_data = all_sheets[selected_sheet_name]
        selected_data = selected_data.fillna('')
        selected_data = selected_data.drop_duplicates()
        selected_data = selected_data.reset_index(drop=True)
        selected_data.rename(columns={'Unnamed: 0': 'Indicator'}, inplace=True)

        if selected_data.empty:
            print('No data available.')
        else:
            print('Below is the summary of the 2022 LFS data')

            second_summary = """ According to the survey results, the working age population (16 years and above) was 7,963,586 of which 4,463,296 persons (56.0 percent) were in the labour force, while 3,500,290 were outside the labour force. For those in the labour force, 3,546,352 were employed, while 916,944 were unemployed. Among those outside the labour force, 1,310,734 persons were engaged wholly or mostly in subsistence foodstuff production (not classified as employment according to the 2013 international standards on statistics of work, employment and labour underutilization).
The annual unemployment rate stood at 20.5 percent, indicating that roughly for five persons in the labour force there was one person unemployed. The unemployment rate was higher among females (23.7 percent) than among males (17.9 percent) and higher among youth (25.6) than among adults (17.1 percent). It was relatively the same in the urban and rural areas (20.4 and 20.6 percent respectively)."""

            print('\n {}'.format(second_summary))

            print(
                f'Displaying data from: {selected_sheet_name}. Summary labour force indicators, RLFS 2022')

            selected_row = 3
            males_data = selected_data.loc[selected_data['Category']
                                           == 'Males', 'Value'].values[0]
            females_data = selected_data.loc[selected_data['Category']
                                             == 'Females', 'Value'].values[0]

            labels = ['Males', 'Females']
            values = [males_data, females_data]

            plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.title('Employment rate Females vs Males')
            plt.show()

            rural_data = selected_data.loc[selected_data['Category']
                                           == 'Rural', 'Value'].values[0]
            urban_data = selected_data.loc[selected_data['Category']
                                           == 'Urban', 'Value'].values[0]

            custom_colors = ['grey', 'black']

            plt.pie([rural_data, urban_data], labels=['Rural', 'Urban'],
                    autopct='%1.1f%%', startangle=140, colors=custom_colors)
            plt.title('Employment rate Rural vs Urban')
            plt.show()

    else:
        print('No data available.')
        return
