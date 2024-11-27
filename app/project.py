class Project:
    def __init__(self,
                 forecast_date: str,
                 author_string: str,
                 output_dir: str
                 ):
        
        # project name = folder name = forecast date
        self.name = forecast_date

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
