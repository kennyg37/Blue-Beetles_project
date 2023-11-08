import pandas as pd 
import sys
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from simple_term_menu import TerminalMenu
from rich.console import Console
from os import system, name as os_name
from time import sleep
from home import home
from detailed_view import data
from about import about



welcome_screen = """

 ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄               ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌             ▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌░▌     ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌             ▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌▐░▌    ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌             ▐░▌          ▐░▌          ▐░▌          
▐░▌ ▐░▌   ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ 
▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌   ▐░▌ ▐░▌     ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀  ▀▀▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌
▐░▌    ▐░▌▐░▌     ▐░▌               ▐░▌▐░▌     ▐░▌               ▐░▌          ▐░▌                    ▐░▌
▐░▌     ▐░▐░▌ ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌              ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌           ▄▄▄▄▄▄▄▄▄█░▌
▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌             ▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌
 ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀               ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                                                        
"""
version = "(Version 1.0.0)"
product_intro =""" NISR-LFS dashboard provides the basic data of the 2022 Labor Force Survey carried out by
The National Institute of Statistics of Rwanda. This dashboard is a product of the Blue Beatles team and NISR.
The dashboard has two menus, the home menu which displays the summary and the Details section that displays the detailed data."""

exit_message = "01100010 01111001 01100101 which is binary for 'bye'..."


flags = {
    'exit_program': False
}


def show_terminal_menu(options = [], menu_title = ""):
    centered_options = map(lambda option: option.center(73), options)
    terminal_menu = TerminalMenu(centered_options, menu_cursor="", title=menu_title)
    terminal_menu_selection_index = terminal_menu.show()

    return terminal_menu_selection_index
def clear_screen():
    if os_name == "posix":
        system("clear")
    else:
        system("cls")
    

def trigger_exit():
    flags['exit_program'] = True


while True:
    try:
        
        if flags['exit_program']:
            clear_screen()
            print(exit_message)
            sleep(1)
            break

        clear_screen()

        print(welcome_screen)
        print(version)

        main_menu_options = {
            "Home" : home,
            "Data" : data,
            "About": about,
            "Exit": trigger_exit
        }

        options_list = list(main_menu_options.keys())


        selection = show_terminal_menu(options_list, "Main Menu")

        main_menu_options[selection].__call__()

        print("")
        print("")
        print("")
        exit_options = ["Back to Main Menu", "Exit"]

        selection = show_terminal_menu(exit_options, "Exit Options")

        if selection == "Exit":
            trigger_exit()

        else:
            flags['exit_program'] = False
    
    except:
        print("An error occured while running the program.")
        sleep(1.5)

