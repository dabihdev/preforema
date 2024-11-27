# ====================================================================================
# Author: @dabihdev
# Year:   2024
# Python version: 3.6.5
# ====================================================================================

from ui import UI

# MAIN
if __name__ == "__main__":
    
    # splash screen
    print("\n========== PREFOREMA (PREtemp FOREcast MAnager) ==========")

    # initialize UI
    ui = UI()

    # start looping
    while(ui.running):
        ui.run()