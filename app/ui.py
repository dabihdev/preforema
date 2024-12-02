# ====================================================================================
# Author: @dabihdev
# Year:   2024
# Python version: 3.6.5
# ====================================================================================

from settings import *        # global settings
from project import Project   # Project class
import os                     # File and folder operations (works only on Windows)
import json                   # JSON parsing

class UI:
    """Class initializing the program User Interface."""
    def __init__(self):
        """Initialize User Interface."""
        
        # UI global settings
        self.selected_day = 1       # default +1 (tomorrow)
        self.current_project = None # empty project
        self.running = True         # set to False to stop main loop

        # current user input
        self.user_choice = None
        
        # dictionary of displayed commands
        self.commands = {
            "a": "aprire un progetto esistente.",
            "s": f"selezionare il giorno di previsione (attuale: +{self.selected_day}).",
            "p": "creare una nuova previsione (mappa e testo).",
            "e": "esportare il testo di previsione sulla pagina html.",
            "i": "mostrare informazioni sul programma.",
            "x": "uscire dal programma."
        }

    
    def load_project(self):
        """Load project data from existing project."""

        # ask user project name
        print()
        folder_name = input("Inserire il nome della cartella del progetto che si vuole caricare> ")
        
        # try fetching data
        print("Sto caricando il progetto...")
        try:
            file = open(output_dir+folder_name+"/"+folder_name+'.json', 'r')
        except:
            print("Nessun progetto con questo nome!")
            return # stops function here
        else:
            data = json.load(file)                                                             # load project data
            self.current_project = Project(data["forecast_day"], data["author"])               # initialize project
            self.selected_day = data["forecast_day"]                                           # update forecast day
            print("Progetto caricato!")
        finally:
            file.close()
    

    def update_commands(self):
        """Update commands description with current forecast day."""
        self.commands["s"] =  f"selezionare il giorno di previsione (attuale: +{self.selected_day})."

    
    def get_input(self):
        """Display to the user the available commands for this program, get input from user."""
        
        # if current project not empty, print current project name and authors names
        print()
        if(self.current_project):
            print(f"GIORNO DI PREVISIONE: {self.current_project.forecast_date}")
            print(f"AUTORE/I: {self.current_project.author_string}")
        else:
            print("PROGETTO VUOTO")
        
        # display available commands
        print()
        for key in self.commands.keys():
            print(f"- Digita [{key}] per {self.commands[key]}")
        
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

    
    def update_forecast_day(self):
        """Change current forecast day, reset current project to None."""
        # prompt user
        print()
        print("ATTENZIONE: CAMBIARE IL GIORNO DI PREVISIONE FARA' USCIRE DAL PROGETTO IN CORSO\nSE SI DESIDERA TORNARE AL PROGETTO CORRENTE DIGITARE UNA LETTERA QUALSIASI.")
        print()
        day = input("Digitare il giorno di previsione come un numero intero (1 per domani, 2 per dopodomani, ecc.)\noppure una lettera qualsiasi per tornare al progetto corrente> ")
        
        # if input is an integer, update selected day and reset project
        try:
            day = int(day)
        except :
            print()
            print ('Il valore inserito non è numerico!')
            print()
        else:
            self.selected_day = day
            self.current_project = None 


    def create_project(self):
        """Ask user for author(s) name(s), initialize project directory and files, open docx and svg."""
        print()
        author_string = self.get_author_name()                                                # ask user input, return author(s) name(s)
        print("> Sto creando il progetto, attendere...")
        self.current_project = Project(self.selected_day, author_string)                      # initialize project and project directory
        svg_generated = self.current_project.add_map()                                        # add SVG template map to project directory
        self.current_project.add_document()                                                   # add docx template document to project directory
        self.current_project.save_project_data()                                              # save project data to JSON
        print("> Sto aprendo i file generati...")
        os.system("start "+self.current_project.path+self.current_project.filenames["docx"])  # open the newly created docx file
        if svg_generated:
            os.system("start "+self.current_project.path+self.current_project.filenames["svg"])   # open newly created svg map
        else:
            print("> ATTENZIONE: il file .svg non è stato generato. Assicurarsi che la cartella assets\nsia stata aggiunta nella cartella del programma preforema.")
        
        
    def export_to_html(self):
        """If project directory and docx file are found, create html page and export forecast text to the html page."""
        
        print("> Sto esportando il testo sulla pagina HTML...")
        html_generated = self.current_project.add_html()               # add html template page to project directory
        if html_generated:
            self.current_project.save_project_data()                   # update JSON file with name of newly created html
        
        # try exporting forecast text to HTML page
        try:
            self.current_project.export_text_to_html()                 # export forecast text to HTML page
        except:
            print("> ERRORE: File di progetto non trovati. Prima di esportare il testo assicurarsi di aver creato un progetto.") # print error message
        else: 
            print("> Testo esportato! Apro la pagina...")
            os.system("start "+self.current_project.path+self.current_project.filenames["html"])  # open newly created HTML page


    def show_info(self):
        """Print the content of README.txt"""

        # read and print text from file
        with open("../info.txt", newline="", encoding="utf-8") as file:
            for line in file.readlines():
                print(line.strip())


    def exit_program(self):
        print()
        print("Chiudo il programma. Ciao!")
        print()
        print("============== PREFOREMA, @DABIHDEV (2024) ===============")
        print()
        self.running = False

    def run(self):

        # update commands
        self.update_commands()

        # prompt user
        self.get_input()

        # handle user input
        if self.user_choice == "a":
            self.load_project()
        elif self.user_choice == "s":
            self.update_forecast_day()
        elif self.user_choice == "p":
            self.create_project()
        elif self.user_choice == "e":
            self.export_to_html()
        elif self.user_choice == "i":
            self.show_info()
        elif self.user_choice == "x":
            self.exit_program()
        else:
            print()
            print("Comando non riconosciuto, riprovare.")
            print()