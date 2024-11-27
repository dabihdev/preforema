from settings import *        # global settings
from project import Project   # Project class
import os                     # operations within the folders (works only on Windows)

class UI:
    def __init__(self):
        self.selected_day = selected_day
        self.current_project = None

    
    def get_input(self):
        """Display to the user the available commands for this program, get input from user."""
        
        # display available commands
        print("")
        for key in commands.keys():
            print(f"- Digita [{key}] per {commands[key]}")
        
        # get input from user
        self.user_choice = input("> ")

    
    def get_author_name(self) -> str:
        """Ask the user(s) to insert his/her/(their) family name. Return formatted author(s) name(s)."""

        # Initialize output_string
        author_string = ""

        # Get user input
        authors_names = input("Specificare il cognome dell'autore. In caso di 2 o più autori, specificare i diversi cognomi separandoli con uno spazio> ")

        # Split authors names if more than one is given
        authors_names_list = authors_names.split() # split the names and put them in a list

        for name in authors_names_list:
            author_string += name.upper() + "/"    # attach the names in upper case to the author_string

        author_string = author_string[:-1]         # delete last '/'

        # return output string
        return author_string

    
    def select_forecast_day(self):
        """Change current forecast day."""
        # prompt user
        print()
        day = input("Digitare il giorno di previsione come un numero intero (1 per domani, 2 per dopodomani, ecc.)> ")
        
        # if input is an integer, update selected day
        try:
            day = int(day)
        except :
            print()
            print ('Il valore inserito non è numerico!')
            print()
        else:
            self.selected_day = day


    def create_project(self):
        """Ask user for author(s) name(s), initialize project directory and files, open docx and svg."""
        print()
        author_string = self.get_author_name()                                                # ask user input, return author(s) name(s)
        print("Sto creando il progetto, attendere...")
        self.current_project = Project(self.selected_day, author_string)                      # initialize project and project directory
        self.current_project.add_map()                                                        # add SVG template map to project directory
        self.current_project.add_document()                                                   # add docx template document to project directory
        print("Progetto creato con successo! Sto aprendo i file...")
        os.system("start "+self.current_project.path+self.current_project.filenames["docx"])  # open the newly created docx file
        os.system("start "+self.current_project.path+self.current_project.filenames["svg"])   # open newly created svg map
        

    def export_to_html(self):
        """If project directory and docx file are found, create html page and export forecast text to the html page."""
        try:
            print("Sto esportando il testo sulla pagina HTML...")
            self.current_project.add_html()                            # add docx template document to project directory
            self.current_project.export_text_to_html()                 # export forecast text to HTML page
        except:
            print("ERRORE: File di progetto non trovati. Prima di esportare il testo assicurarsi di aver creato un progetto.") # print error message
        else:
            print("Testo esportato! Apro la pagina...")
            os.system("start "+self.current_project.path+self.current_project.filenames["html"])  # open newly created HTML page


    def show_info(self):
        """Print the content of README.txt"""

        # read and print text from file
        with open("../README.txt", newline="", encoding="utf-8") as file:
            for line in file.readlines():
                print(line.strip())


    def exit_program(self):
        pass

    def run(self):
        pass