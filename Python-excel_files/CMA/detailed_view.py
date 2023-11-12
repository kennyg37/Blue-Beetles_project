import numpy as np
import pandas as pd
import plotly.express as px

def data():
    excel_file = 'excel_data.xlsx'
    if excel_file is not None:
        all_sheets = pd.read_excel(excel_file, sheet_name=None, skiprows=[0])
        sheet_list = list(all_sheets.keys())

        while True:
            print('\nChoose an option:')
            print('1. View Table')
            print('2. View Chart')
            print('3. Exit program')

            selected_option = input('Enter the option number: ')

            if selected_option == '1':
                print('\nList of Tables:')
                for i, sheet_name in enumerate(sheet_list, start=1):
                    print(f'{i}. {sheet_name}')

                while True:
                    selected_sheet_number = input('Select a table number (or type "back" to return): ')
                    
                    if selected_sheet_number.lower() == 'back':
                        break

                    try:
                        selected_sheet_number = int(selected_sheet_number)
                        if 1 <= selected_sheet_number <= len(sheet_list):
                            selected_sheet = sheet_list[selected_sheet_number - 1]
                            selected_data = all_sheets[selected_sheet]
                            
                            if selected_sheet == 'Table 1':
                                selected_data = selected_data.fillna('')
                                selected_data = selected_data.drop_duplicates()
                                selected_data = selected_data.reset_index(drop=True)
                                print(selected_data)
                            else:
                                selected_data = selected_data.fillna('')
                                selected_data = selected_data.drop_duplicates()
                                selected_data = selected_data.reset_index(drop=True)
                                selected_data.rename(columns={'Unnamed: 0': 'Indicator'}, inplace=True)
                                print(selected_data)
                            break
                        else:
                            print("Invalid table number. Please enter a valid number.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

            elif selected_option == '2':
                print('\nList of Charts:')
                for i, sheet_name in enumerate(sheet_list, start=1):
                    print(f'{i}. {sheet_name}')

                while True:
                    selected_chart_number = input('Select a chart number (or type "back" to return): ')
                    
                    if selected_chart_number.lower() == 'back':
                        break

                    try:
                        selected_chart_number = int(selected_chart_number)
                        if 1 <= selected_chart_number <= len(sheet_list):
                            selected_chart = sheet_list[selected_chart_number - 1]
                            selected_chart_data = all_sheets[selected_chart]
                            
                            if selected_chart == 'List Of Tables':
                                selected_chart_data = selected_chart_data.fillna('')
                                selected_chart_data = selected_chart_data.drop_duplicates()
                                selected_chart_data = selected_chart_data.reset_index(drop=True)
                                selected_chart_data.rename(columns={'Unnamed: 0': 'Indicator'}, inplace=True)
                                print(selected_chart_data)
                            else:
                                for sheet_name, sheet_data in all_sheets.items():
                                    if sheet_name == selected_chart:
                                        print(f"Displaying chart for {sheet_name}")
                                        if len(sheet_data.columns) >= 2:
                                            column_names = list(sheet_data.columns)
                                            x_column = column_names[0]
                                            y_column = column_names[1]
                                            chart = px.line(sheet_data, x=x_column, y=y_column, title=f"{sheet_name}")
                                            chart.show()
                                        else:
                                            print("The sheet does not have enough columns to display a chart")
                                        break
                                else:
                                    print("Invalid sheet name")
                            break
                        else:
                            print("Invalid chart number. Please enter a valid number.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

            elif selected_option == '3':
                print("Exiting the program.")
                break

            else:
                print("Invalid option. Please enter 1, 2, or 3.")
    else:
        print('No data available.')