import os                          # operations within the folders (works only on Windows)
from docx import Document          # .docx file reading and writing

class Project:
    def __init__(self,
                 forecast_date: str,
                 author_string: str,
                 output_dir: str
                 ):
        """Initialize the project."""

        # project name = folder name = forecast date
        self.forecast_date = forecast_date

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
        self.author = author_string

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

    

