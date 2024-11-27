from ui import UI
from project import Project

# MAIN
if __name__ == "__main__":
    
    # splash screen
    print("\n========== PREFOREMA (PREtemp FOREcast MAnager) ==========")

    # initialize UI
    ui = UI()

    # start looping
    while(ui.running):
        ui.run()