import customtkinter as ctk
from PIL import Image, ImageTk
from AnimatedGif import *
#Window
window = ctk.CTk()
window.geometry("480x320")
#window.attributes("-fullscreen", True) #uncomment when done developing
window.resizable(0,0)
window.configure(fg_color="#000000")    


#GIF
vault_guy = AnimatedGif(window, "vaultboy.gif", 0.07)
vault_guy.configure(borderwidth=0, highlightthickness=0, bg="#2b2b2b")
vault_guy.place(relx=0.3635,rely= 0.2281)
vault_guy.start()


#Tabs
stat = Image.open("hotbar/stat.png")
ctk_stat = ctk.CTkImage(light_image= stat, dark_image= stat, size=(480, 24))
inv = Image.open("hotbar/inv.png")
ctk_inv = ctk.CTkImage(light_image= inv, dark_image= inv, size=(480, 24))
data = Image.open("hotbar/data.png")
ctk_data = ctk.CTkImage(light_image= data, dark_image= data, size=(480, 24))
map = Image.open("hotbar/map.png")
ctk_map = ctk.CTkImage(light_image= map, dark_image= map, size=(480, 24))
radio = Image.open("hotbar/radio.png")
ctk_radio = ctk.CTkImage(light_image= radio, dark_image= radio, size=(480, 24))


#Hotbar
hotbar_label = ctk.CTkLabel(window, text="")
hotbar_label.place(relx=0, rely=0)
tabs = [ctk_stat, ctk_inv, ctk_data, ctk_map, ctk_radio]
current_tab = [0]  # Use list to make it mutable in nested functions



#Func to change tabs

def update_tab(index):
    hotbar_label.configure(image=tabs[index])
def next_tab(event=None):
    current_tab[0] = (current_tab[0] + 1) % len(tabs)
    update_tab(current_tab[0])
def prev_tab(event=None):
    current_tab[0] = (current_tab[0] - 1) % len(tabs)
    update_tab(current_tab[0])

#Keybinds
window.bind("<d>", next_tab)
window.bind("<a>", prev_tab)
#######
update_tab(current_tab[0])
window.mainloop()