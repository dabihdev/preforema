# ====================================================================================
# Author: @dabihdev
# Year:   2024
# Python version: 3.6.5
# ====================================================================================

# GLOBAL SETTINGS
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

# Dictionary of risk-level colors
risk_colors_dict = {
    "ASSENTI": "#277f9d",
    "0": "#ffff00",
    "1": "#ff6600",
    "2": "#ff0000",
    "3": "#FF00FF"
}

# Current day
today = datetime.today()
todays_date = today.strftime('%d-%m-%Y')
todays_weekday = weekdays_dict[datetime.today().weekday()]
