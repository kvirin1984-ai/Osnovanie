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

frame = Frame(window, bg='#7AD0FF')
frame.grid(row=0, column=0)

label = Label(frame, text='Базовая ----->> \n валюта',
              font=('Segoe Print', 16, 'bold'), bg='#7AD0FF', fg='#5D2AB7')
label.grid(row=0, column=1, pady=10)

combobox = ttk.Combobox(frame, width=25, state ='readonly',values=list(currencies.keys()))
combobox.grid(row=0, column=2, pady=10)
combobox.bind('<<ComboboxSelected>>', update_label2)

label2 = ttk.Label(frame)
label2.config(font=('Segoe Print', 12, 'bold'), background='#7AD0FF', foreground='#5D2AB7')
label2.grid(row=1, column=2)

label0 = Label(frame, text='Целевая ----->> \n криптовалюта',
               font=('Segoe Print', 16, 'bold'), bg='#7AD0FF', fg='#B72818')
label0.grid(row=2, column=1, pady=10)

combobox0 = ttk.Combobox(frame, width=25, state='readonly',values=list(crypto.keys()))
combobox0.grid(row=2, column=2, pady=10)
combobox0.bind('<<ComboboxSelected>>', update_label3)

label3 = ttk.Label(frame)
label3.config(font=('Segoe Print', 12, 'bold'), background='#7AD0FF', foreground='#B72818')
label3.grid(row=3, column=2)

button = Button(frame, width=35, height=3,
                text='Получить курс базовой валюты \n к выбранной криптовалюте',
                bg='#2590CF', activebackground='#E6AF00', font=('Algerian', 13, 'bold'), command=exchange)
button.grid(row=4, column=1, columnspan=3, padx=42, pady=20)

label1 = Label(frame, width=43, height=3, bg='#21C5CF',
               text='Выберите базовую валюту и криптовалюту',
               font=('Bahnschrift Condensed', 16, 'bold'))
label1.grid(row=5, column=1, columnspan=3, padx=42, pady=20)


window.mainloop()