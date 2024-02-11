import customtkinter
from PIL import Image
from assets import my_images
from constants import window
from pages import app
from services import plate_number

class Frame(customtkinter.CTkFrame):
    def __init__(self, master: app.Application):
        super().__init__(master, width=window.width, height=window.height - 40)
        self.grid_columnconfigure(0, weight=1)
        
        self.image_ctn = customtkinter.CTkFrame(self, width=window.width, height=window.height-140, fg_color="gray")
        self.image_ctn.grid(row=0, column=0, columnspan=2)
        
        
        # IMAGE
        self.image_label = customtkinter.CTkLabel(self.image_ctn, text="Please pick your image!", width=window.width, height=window.height-140) 
        self.image_label.grid(row = 0, column = 0)
        
        # Button Choose Image
        img_button = customtkinter.CTkButton(self, text="CHOOSE YOUR IMAGE", width=window.width/2, height=100, command=self.choose_image, border_width=4, border_color="white", font=("ubuntu", 20))
        img_button.grid(row = 1, column = 0)
        
        # Label
        self.plate_label = customtkinter.CTkLabel(self, text="NO NAME", width=window.width/2, font=("ubuntu", 30))
        self.plate_label.grid(row = 1, column = 1)
    
    def choose_image(self):
        file = customtkinter.filedialog.askopenfile(initialdir="/home/dobermann/Python/python-basic/Temp/images", filetypes=[("Images",".png .jpg .jpeg")])
        if file == None:
            return
        print(file)
        ctk_image = customtkinter.CTkImage(light_image=Image.open(file.name),
                                  dark_image=Image.open(file.name),
                                  size=(window.width, window.height - 140))
        
        self.image_label.configure(False, image=ctk_image, text="")
        try:
            text = plate_number.detect(file.name)
            self.plate_label.configure(False, text=text)
        except:
            self.plate_label.configure(False, text="ERROR!")
            