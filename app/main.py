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