from settings import *      # import global settings

class UI:
    def __init__(self):
        pass


    def get_input(self):
        """Display to the user the available commands for this program, get input from user."""
        
        # display available commands
        print("")
        for key in commands.keys():
            print(f"- Digita [{key}] per {commands[key]}")
        
        # get input from user
        self.user_choice = input("> ")


    def select_forecast_day(self):
        pass

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