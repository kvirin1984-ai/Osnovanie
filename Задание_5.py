from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
import json
import pprint
from requests.packages import target

window = Tk()
window.title('Курс обмена валют')
WIDTH = window.winfo_screenwidth()
HEIGHT = window.winfo_screenheight()
X = 460
Y = 450
window.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}+{HEIGHT // 2 - Y // 2 - 25}")

Label(text='Базовая валюта').pack()
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=3)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)

base_label = ttk.Label()
base_label.pack(pady=10)

Label(text='Вторая базовая валюта').pack()
base2_combobox = ttk.Combobox(values=list(currencies.keys()))
base2_combobox.pack(padx=10, pady=3)
base2_combobox.bind('<<ComboboxSelected>>', update_base2_label)

base2_label = ttk.Label()
base2_label.pack(pady=10)

Label(text='Целевая валюта').pack(padx=10)

target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=10)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)

target_label = ttk.Label()
target_label.pack(pady=10)

Button(text='Получить курс обмена', command=exchange).pack(padx=10, pady=10)

window.mainloop()