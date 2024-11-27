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

        # set forecast day
        self.forecast_day = datetime.today() + timedelta(days=selected_day)

        # set forecast date = project directory name = project name
        self.forecast_date = self.forecast_day.strftime('%d-%m-%Y') # convert to string format
        
        # get forecast date weekday
        self.forecast_weekday = weekdays_dict[self.forecast_day.weekday()]

        # project path
        self.path = output_dir+self.forecast_date+"/"                        
        
        # dictionary of file names inside the project directory
        self.filenames = {
            "docx": f"previsione_{self.forecast_date}.docx",
            "svg": f"mappa_{self.forecast_date}.svg",
            "html": f"{self.forecast_date}.html",
            "json": f"{self.forecast_date}.json",
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


    def add_html(self):
        """Add html file in project directory, with updated date, time and author."""
        
        # Read html file content
        with open('../assets/dd_mm_yyyy.html') as html:
            html_soup = BeautifulSoup(html, "html5lib")

        # Create updated title 
        weekday = self.forecast_weekday
        day = self.forecast_day.day
        month = months_dict[self.forecast_day.month]
        year = self.forecast_day.year
        new_title = f"PREVISIONE PER {weekday} {day} {month} {year}"

        # Create updated forecast time range
        new_forecast_time_range = f"Valida dalle ore 00:00 alle 24:00 UTC di {weekday.lower()} {day} {month.lower()} {year}"

        # Create updated authors string
        new_authors = "Previsore: " + new_authors

        # Create date of forecast issue
        weekday = weekdays_dict[today.weekday()]
        day = today.day
        month = months_dict[today.month]
        year = today.year
        utc_hour = today.utcnow().strftime("%H:%M")
        new_forecast_issue_date = f"Emessa {weekday.lower()} {day} {month.lower()} {year} alle ore {utc_hour} UTC"

        # Update html elements
        html_soup.find("title", {"id": "window-title"}).string = new_title.lower() # window title
        html_soup.find("strong", {"id": "title-date"}).string = new_title # title
        html_soup.find("span", {"id": "forecast-time-range"}).string = new_forecast_time_range # forecast time range
        html_soup.find("p", {"id": "issue-date"}).string = new_forecast_issue_date # forecast issue date
        html_soup.find("p", {"id": "authors"}).string = new_authors # forecast authors names

        # Save edited html in new_folder_path
        new_html_name = f'{self.forecast_date}.html'
        if os.path.isfile(self.path+new_html_name):
            with open(self.path+new_html_name, "w") as html:
                html.write(str(html_soup.prettify(formatter="html")))
        else:
            with open(self.path+new_html_name, "x") as html:
                html.write(str(html_soup.prettify(formatter="html")))