import customtkinter
from constants import window
import pages

class Application(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # init window
        self.title("Plate Number Detection")
        self.geometry(window.geometry)
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        
        # add header
        self.header = customtkinter.CTkFrame(self, width=window.width, height=40, fg_color="transparent")
        # back button
        self.back_btn = customtkinter.CTkButton(self.header, text="Back", command=self.back)
        self.back_btn.grid(row=0, column=0)
        
        self.show_start_page()
    
    def back(self):
        self.frame.destroy()
        self.show_start_page()
        
    def show_header(self):
        self.header.grid(row = 0, column = 0, stick="EW")
    
    def hide_header(self):
        self.header.grid_forget()
        
    def show_start_page(self):
        self.hide_header()
        self.frame = pages.start_page.Frame(self)
        self.frame.grid(row=1, column=0, sticky="NSEW")
        
    def show_image_page(self):
        self.show_header()
        self.frame.destroy()
        self.frame = pages.image_page.Frame(self)
        self.frame.grid(sticky="NSEW")
        
    def show_camera_page(self):
        self.show_header()
        self.frame.destroy()
        self.frame = pages.camera_page.Frame(self)
        self.frame.grid(sticky="NSEW")