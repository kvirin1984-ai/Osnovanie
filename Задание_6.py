from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk


window = Tk()
window.title('Конвертер криптовалют к доллару США')
pil_image = Image.open('Dollar.png')
icon = ImageTk.PhotoImage(pil_image)
window.iconphoto(True, icon)
window.configure(background='#7AD0FF')
WIDTH = window.winfo_screenwidth()
HEIGHT = window.winfo_screenheight()
X = 500
Y = 400
window.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}+{HEIGHT // 2 - Y // 2 - 25}")

style = ttk.Style()
style.theme_use('clam')

style.configure(
    "TCombobox",
    fieldbackground="#7AD0FF",
    background="#7AD0FF",
    foreground="black",
    arrowcolor="black",
    bordercolor="black",
    lightcolor="#7AD0FF",
    darkcolor="#7AD0FF",
    selectbackground="#7AD0FF",
    selectforeground="black",
)
style.map('TCombobox',
          fieldbackground=[('readonly', '#7AD0FF'), ('disabled', '#7AD0FF')],
          background=[('readonly', '#7AD0FF'), ('disabled', '#7AD0FF')])


frame = Frame(window, bg='#7AD0FF')
frame.grid(row=0, column=0)

label = Label(frame, text='Целевая ----->> \n криптовалюта',
              font=('Segoe Print', 16, 'bold'), bg='#7AD0FF')
label.grid(row=0, column=1, pady=10)

combobox = ttk.Combobox(frame, width=25, state='readonly',values=list(crypto.keys()))
combobox.grid(row=0, column=2, pady=10)
combobox.bind('<<ComboboxSelected>>', update_label)

label0 = ttk.Label(frame)
label0.config(font=('Segoe Print', 12, 'bold'), background='#7AD0FF', foreground='#FF000C')
label0.grid(row=1, column=2)

button = Button(frame, width=35, height=3,
                text='Получить курс выбранной криптовалюты \n к Доллару США', bg='#2590CF',
                activebackground='#E6AF00', font=('Algerian', 13, 'bold'), command=exchange)
button.grid(row=2, column=1, columnspan=3, padx=42, pady=20)

label1 = Label(frame, width=43, height=3, bg='#8EB9FC',
               text='Выберите криптовалюту', font=('Bahnschrift Condensed', 16, 'bold'))
label1.grid(row=3, column=1, columnspan=3, padx=42, pady=20)

window.mainloop()