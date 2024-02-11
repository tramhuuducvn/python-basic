import customtkinter
from constants import window
import start_page

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Plate Number Detection")
        self.geometry(window.geometry)
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame = start_page.Frame(self)
        self.frame.grid(sticky="NSEW")
    
app = App()
app.mainloop()
