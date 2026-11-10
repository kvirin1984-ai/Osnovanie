from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk


window = Tk()
window.title('Конвертер криптовалют')
pil_image = Image.open('btc2.png')
icon = ImageTk.PhotoImage(pil_image)
window.iconphoto(True, icon)
window.configure(background='#7AD0FF')
WIDTH = window.winfo_screenwidth()
HEIGHT = window.winfo_screenheight()
X = 500
Y = 500
window.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}+{HEIGHT // 2 - Y // 2 - 25}")




window.mainloop()