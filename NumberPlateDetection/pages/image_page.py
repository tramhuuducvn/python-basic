import customtkinter
from PIL import Image
from assets import my_images
from constants import window
from pages import app

class Frame(customtkinter.CTkFrame):
    def __init__(self, master: app.Application):
        super().__init__(master, fg_color="red")
        self.grid_columnconfigure(0, weight=1)