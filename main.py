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
# Tab-specific widgets
tab_widgets = [
    [  # Stat Tab
        ctk.CTkButton(window, text="Health", command=lambda: print("Health")),
        ctk.CTkButton(window, text="Level", command=lambda: print("Level"))
    ],
    [  # Inventory Tab
        ctk.CTkButton(window, text="Weapons", command=lambda: print("Weapons")),
        ctk.CTkButton(window, text="Apparel", command=lambda: print("Apparel"))
    ],
    [  # Data Tab
        ctk.CTkButton(window, text="Quests", command=lambda: print("Quests")),
        ctk.CTkButton(window, text="Stats", command=lambda: print("Stats"))
    ],
    [  # Map Tab
        ctk.CTkButton(window, text="Local Map", command=lambda: print("Local Map")),
        ctk.CTkButton(window, text="World Map", command=lambda: print("World Map"))
    ],
    [  # Radio Tab
        ctk.CTkButton(window, text="Radio On", command=lambda: print("Radio On")),
        ctk.CTkButton(window, text="Radio Off", command=lambda: print("Radio Off"))
    ]
]

#Hotbar
hotbar_label = ctk.CTkLabel(window, text="")
hotbar_label.place(relx=0, rely=0)
tabs = [ctk_stat, ctk_inv, ctk_data, ctk_map, ctk_radio]
current_tab = [0]

#Func to change tabs

# Keep track of currently visible widgets
visible_widgets = []

def update_tab(index):
    hotbar_label.configure(image=tabs[index])
    
    # Hide previous tab widgets
    for widget in visible_widgets:
        widget.place_forget()
    visible_widgets.clear()

    # Show new tab widgets
    for i, widget in enumerate(tab_widgets[index]):
        widget.place(relx=0.1, rely=0.4 + i * 0.1)  # Stagger buttons vertically
        visible_widgets.append(widget)
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