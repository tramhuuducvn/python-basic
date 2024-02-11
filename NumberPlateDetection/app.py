import customtkinter
from pages import start_page

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Plate Number Detection")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = start_page.StartPage(self)
        self.checkbox_frame.grid(sticky="NSEW")
    
app = App()
app.mainloop()