from pages import app

app = app.Application()
app.mainloop()

# import customtkinter
# root = customtkinter.CTk()
# label=customtkinter.CTkLabel(root,text="I was Hidden")
# def labelactive():
#     label.pack()
# def labeldeactive():
#     label.pack_forget()
# customtkinter.CTkButton(root,text="Show",command=labelactive).pack()
# customtkinter.CTkButton(root,text="Hide",command=labeldeactive).pack()
# root.mainloop()