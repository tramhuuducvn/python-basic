import customtkinter
from PIL import Image
from assets import my_images
from constants import window
from pages import app

class Frame(customtkinter.CTkFrame):
    def __init__(self, master: app.Application):
        super().__init__(master, fg_color="transparent")
        
        self.grid_columnconfigure(0, weight=1)
        
        bg_welcome = customtkinter.CTkImage(light_image=Image.open(my_images.welcome),
                                  dark_image=Image.open(my_images.welcome),
                                  size=(window.width, window.height - 100))
        
        # IMAGE
        image_label = customtkinter.CTkLabel(self, image=bg_welcome, text="") 
        image_label.grid(row = 0, column = 0, columnspan = 2 ,sticky="NSEW")
        
        # OPTION 1
        img_button = customtkinter.CTkButton(self, text="STORED IMAGES", width=window.width/2, height=100, command=self.choose_image, border_width=4, border_color="white", font=("ubuntu", 20))
        img_button.grid(row = 1, column = 0)
        
        # OPTION 2
        img_button = customtkinter.CTkButton(self, text="CAMERA", width=window.width/2, height=100, command=self.choose_camera, border_width=4, border_color="white", font=("ubuntu", 20))
        img_button.grid(row = 1, column = 1)
               
    
    def choose_image(self):
        self.master.show_image_page()
    
    def choose_camera(self):
        self.master.show_camera_page()