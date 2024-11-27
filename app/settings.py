from datetime import datetime, timedelta      # date and time processing

# Current directory
output_dir = "../previsioni/"

# Dictionary of weekdays
weekdays_dict = {
    0: "LUNEDI'",
    1: "MARTEDI'",
    2: "MERCOLEDI'",
    3: "GIOVEDI'",
    4: "VENERDI'",
    5: "SABATO",
    6: "DOMENICA",
}

# Dictionary of months
months_dict = {
    1: "GENNAIO",
    2: "FEBBRAIO",
    3: "MARZO",
    4: "APRILE",
    5: "MAGGIO",
    6: "GIUGNO",
    7: "LUGLIO",
    8: "AGOSTO",
    9: "SETTEMBRE",
    10: "OTTOBRE",
    11: "NOVEMBRE",
    12: "DICEMBRE"
}

# Current day
today = datetime.today()
todays_date = today.strftime('%d-%m-%Y')
todays_weekday = weekdays_dict[datetime.today().weekday()]

# Forecast day
selected_day = 1 # write 1 for tomorrow, 2 for the day after tomorrow etc.

# Dictionary of available user commands
""" commands = {
    "s": f"selezionare il giorno di previsione (attuale: +{selected_day}).",
    "p": "creare una nuova previsione (mappa e testo).",
    "e": "esportare il testo di previsione sulla pagina html.",
    "i": "mostrare informazioni sul programma.",
    "x": "uscire dal programma."
} """