import os                                     # operations within the folders (works only on Windows)
from docx import Document                     # .docx file reading and writing
from bs4 import BeautifulSoup                 # XML parsing
from settings import *                        # import global settings
from datetime import datetime, timedelta      # date and time processing

class Project:
    def __init__(self,
                 selected_day: int,
                 author_string: str,
                 output_dir: str
                 ):
        """Initialize the project."""

        # set forecast date
        forecast_day = datetime.today() + timedelta(days=selected_day)
        forecast_date = forecast_day.strftime('%d-%m-%Y') # convert to string format
        forecast_weekday = weekdays_dict[forecast_day.weekday()]
        
        # project name = folder name = forecast date
        self.forecast_date = forecast_date
        
        # set weekday of forecast date
        self.forecast_weekday = forecast_weekday

        # project path
        self.path = output_dir+forecast_date+"/"                        
        
        # dictionary of file names inside the project directory
        self.filenames = {
            "docx": f"previsione_{forecast_date}.docx",
            "svg": f"mappa_{forecast_date}.svg",
            "html": f"{forecast_date}.html",
            "json": f"{forecast_date}.json",
            }                                            
        
        # author(s) name(s)
        self.author_string = author_string

        # create output folder if not existing already
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        # create project folder if not existing already
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        
    def add_document(self):
        """Add a template .docx document formatted for the PRETEMP forecast to the project directory."""

        # Create empty docx file
        new_document = Document()

        # Add section: "TESTO BREVE"
        paragraph1 = new_document.add_paragraph()
        paragraph1.add_run("TESTO BREVE").bold = True # make it bold
        paragraph2 = new_document.add_paragraph("Inserire qui un riassunto della previsione.")

        # Add empty line
        new_document.add_paragraph()

        # Add header: "DISCUSSIONE"
        paragraph3 = new_document.add_paragraph()
        paragraph3.add_run("DISCUSSIONE").bold = True

        # Add section: "--sezione 1--"
        paragraph4 = new_document.add_paragraph()
        paragraph4.add_run("--sezione 1--").bold = True
        paragraph5 = new_document.add_paragraph("Inserire qui la discussione per questa sezione.")

        # Add section: "--sezione 2--"
        paragraph6 = new_document.add_paragraph()
        paragraph6.add_run("--sezione 2--").bold = True
        paragraph7 = new_document.add_paragraph("Inserire qui la discussione per questa sezione.")

        # Save the newly created docx document in the folder ./previsioni/ with the name formatted as "previsione_<today's date>.docx"
        new_document.save(self.forecast_date+self.filenames["docx"])

    def add_map(self):
        """Create new SVG file in the forecast folder with template map and updated date and author."""

        # Open the file "./assets/mappa.svg" and read xml content
        with open("../assets/mappa.svg", "rt") as svg:
            xml_content = svg.read()

        xml_soup = BeautifulSoup(xml_content, "xml")

        # Create updated string that will substitute the text
        newstring_date = f"Valida dalle ore 00:00 UTC alle 24:00 UTC di {self.forecast_weekday.lower()} {self.forecast_date} - Emessa: {todays_weekday.lower()} {todays_date} alle ore 15:00 UTC "
        newstring_author = "AUTORE: " + self.author_string

        # Find and update text object "DATA E AUTORE"
        xml_soup.find("tspan", {"id": "tspan25"}).string = newstring_date    # update dates
        xml_soup.find("tspan", {"id": "tspan26"}).string = newstring_author  # update author's name
        new_xml_content = str(xml_soup)                                      # store updated xml content as string

        
        # if file already exists overwrite it, otherwise create it
        if os.path.isfile(self.path+self.filenames["svg"]):
            with open(self.path+self.filenames["svg"], "w") as svg:
                svg.write(new_xml_content)
        else:
            with open(self.path+self.filenames["svg"], "x") as svg:
                svg.write(new_xml_content)
