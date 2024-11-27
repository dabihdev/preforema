from settings import *      # import global settings
from project import Project

class UI:
    def __init__(self):
        self.selected_day = selected_day


    def get_input(self):
        """Display to the user the available commands for this program, get input from user."""
        
        # display available commands
        print("")
        for key in commands.keys():
            print(f"- Digita [{key}] per {commands[key]}")
        
        # get input from user
        self.user_choice = input("> ")


    def select_forecast_day(self):
        """Change current forecast day."""
        # prompt user
        print()
        day = input("Digitare il giorno di previsione come un numero intero (1 per domani, 2 per dopodomani, ecc.)> ")
        
        # if input is valid, create new project for the selected day
        try:
            day = int(day)
        except :
            print()
            print ('Il valore inserito non è numerico!')
        else:
            self.selected_day = day


    def create_project(self):
        pass

    def export_to_html(self):
        pass

    def show_info(self):
        pass

    def exit_program(self):
        pass

    def run(self):
        pass