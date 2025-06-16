# ====================================================================================
# Author: @dabihdev
# Year:   2024
# Python version: 3.6.5
# ====================================================================================

from settings import *         # global settings
from project import Project    # Project class
import os                      # File, folder and terminal operations (works only on Windows)
import json                    # JSON parsing
from bs4 import BeautifulSoup  # XML/HTML parsing

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
            "a": "APRIRE un progetto esistente.",
            "s": f"SELEZIONARE il giorno di previsione (attuale: +{self.selected_day}).",
            "p": "creare una NUOVA PREVISIONE (mappa e testo).",
            "e": "esportare il testo di previsione sulla PAGINA HTML.",
            "g": "generare il codice html per l'ANTEPRIMA IN HOMEPAGE.",
            "i": "mostrare INFORMAZIONI sul programma.",
            "x": "USCIRE dal programma."
        }

    
    def return_to_menu(self):
        """Make the program pause until user presses ENTER."""
        input("premere INVIO per tornare al menù...")
        os.system("cls") # clear screen

    
    def load_project(self):
        """Load project data from existing project."""

        # ask user project name
        print()
        folder_name = input("Inserire il nome della cartella del progetto che si vuole caricare> ")
        
        # try fetching data
        print("Sto caricando il progetto...")
        try:
            with open(output_dir+folder_name+"/"+folder_name+'.json', 'r') as file:
                data = json.load(file)                                                             # load project data
                self.current_project = Project(data["forecast_day"], data["author"])               # initialize project
                self.selected_day = data["forecast_day"]                                           # update forecast day
                print("Progetto caricato!")
        except:
            print("Nessun progetto con questo nome!")
    

    def update_commands(self):
        """Update commands description with current forecast day."""
        self.commands["s"] =  f"selezionare il giorno di previsione (attuale: +{self.selected_day})."

    
    def get_input(self):
        """Display to the user the available commands for this program, get input from user."""
        
        # if current project not empty, print current project name and authors names
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
        authors_names = input("Specificare il cognome dell'autore. In caso di 2 o più autori, specificare i diversi cognomi separandoli con una virgola> ")

        # Split authors names if more than one is given
        authors_names_list = authors_names.split(sep=",") # split the names and put them in a list

        for name in authors_names_list:
            author_string += name.upper().strip() + "/"    # attach the names in upper case to the author_string

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
            print ('Processo annullato!')
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
        
        if svg_generated:                                        
            self.current_project.add_document()                                                   # add docx template document to project directory
            self.current_project.save_project_data()                                              # save project data to JSON
            print("> Sto aprendo i file generati...")
            os.system("start "+self.current_project.path+self.current_project.filenames["docx"])  # open the newly created docx file
            os.system("start "+self.current_project.path+self.current_project.filenames["svg"])   # open newly created svg map
        else:
            print("> ATTENZIONE: il file .svg non è stato generato.")                             # if svg not created stop the process and flag the user
        
        
    def export_to_html(self):
        """If project directory and docx file are found, create html page and export forecast text to the html page."""
        
        if self.current_project:
            print("> Sto esportando il testo sulla pagina HTML...")
            html_generated = self.current_project.add_html()               # add html template page to project directory
        else: # if no project created/selected
            print("Non hai ancora creato o selezionato un progetto!")
            return # stop function
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

    def generate_preview_html(self):
        # stop if no project created/selected
        if not self.current_project:
            print("\n Non hai selezionato o creato nessun progetto!\n")
            return # stop function
        
        # read and parse html code from asset
        try:
            with open("../assets/preview.html", "rt", encoding= "utf-8") as html:
                html_soup = BeautifulSoup(html, "html5lib")
        except FileNotFoundError:
            print("> File preview.html non trovato. Assicurarsi che la cartella assets sia presente nella cartella di preforema,\ne che contenga il file preview.html")
            return # stop the function

        # update following parameters:
        # 1. forecast date (title)
        weekday = self.current_project.forecast_weekday
        day = self.current_project.forecast_day.day
        month = months_dict[self.current_project.forecast_day.month]
        year = self.current_project.forecast_day.year
        new_title = f"PREVISIONE PER {weekday} {day} {month} {year}"

        # 2. link to forecast page
        page_url = f"https://www.pretemp.it/archivio/{year}/{month.lower()}/previsioni/{self.current_project.forecast_date}.html"

        # 3. link to forecast map
        map_url = f"https://www.pretemp.altervista.org/archivio/{year}/{month.lower()}/cartine/{self.current_project.forecast_date}.svg"

        # 4. risk level + risk color
        risk_level = input("Inserisci il livello di pericolosità più elevato che hai/avete emesso\n(inserire numero oppure la scritta assenti): ").upper()
        risk_color = risk_colors_dict[risk_level] # color code as str
        style_string = f"color: {risk_color}; font-size: 14pt; font-family: arial, helvetica, sans-serif;"

        # 5. authors
        authors = self.current_project.author_string

        # update html code
        # html_soup.find("span", {"id": "forecast-date"}).string = new_title

        for a in html_soup.find_all('a', href=True):
            if (a['id'] == "page-link"):
                a.string = new_title
                a['href'] = page_url
            elif a['id'] == "map-page-link":
                a['href'] = page_url
                
        html_soup.find("img", {"id": "map-link"})["src"] = map_url
        html_soup.find("span", {"id": "risk-level"}).string = risk_level
        html_soup.find("span", {"id": "risk-level"})["style"] = style_string
        html_soup.find("span", {"id": "authors"}).string = f"Autori: {authors}"

        # save generated html code in txt file
        gencode_file = f'livello{risk_level}.txt'
        with open(self.current_project.path+gencode_file, "w", encoding="utf-8") as txt:
            txt.write(str(html_soup.prettify(formatter="html")))

        # log user
        print(f"Codice HTML di preview generato correttamente! Copialo dal file {gencode_file} e incollalo\nin home page")

        # open txt file
        os.system("start "+self.current_project.path+gencode_file)


    def show_info(self):
        """Print the content of README.txt"""

        # read and print text from file
        with open("../info.txt", newline="", encoding="utf-8") as file:
            for line in file.readlines():
                print(line.strip())
        
        # add empty lines at the end
        print("\n")


    def exit_program(self):
        print()
        print("Chiudo il programma. Ciao!")
        self.running = False

    def run(self):
        """Run main loop."""
        while self.running:
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
            elif self.user_choice == "g":
                self.generate_preview_html()
            elif self.user_choice == "i":
                self.show_info()
            elif self.user_choice == "x":
                self.exit_program()
                return # interrupt function here
            else:
                print()
                print("Comando non riconosciuto, riprovare.")
            
            # clear screen, go back to menu
            self.return_to_menu()