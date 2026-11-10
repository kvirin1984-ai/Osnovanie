from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk


def update_label2(event):
    code = combobox.get()
    name = currencies[code]
    label2.config(text=name)


def update_label3(event):
    code = combobox0.get()
    name = crypto[code]
    label3.config(text=name)


def exchange():
    base_currency = combobox.get().strip()
    target_crypto = combobox0.get().strip()
    if target_crypto and base_currency:
        try:
            name = currencies[base_currency]
            response = requests.get(f'https://api.coingecko.com/api/v3/'
                                    f'simple/price?ids={target_crypto}&vs_currencies={base_currency}')
            response.raise_for_status()
            data = response.json()
            target = data[target_crypto][base_currency]
            label1.config(text=f'Курс = 1 {target_crypto} \nза {target} {name} ({base_currency})')
        except Exception as err:
            label1.config(text=f'Ошибка {err}')
    else:
        label1.config(text='Введите код валюты и выберите криптовалюту')

crypto = {
    'bitcoin': 'Биткоин (BTC)',
    'ethereum': 'Эфириум (ETH)',
    'tether': 'Тетер (USDT)',
    'binancecoin': 'Бинанскоин (BNB)',
    'solana': 'Солана (SOL)',
    'ripple': 'Райпл (XRP)',
    'dogecoin': 'Догкоин (DOGE)',
    'tron': 'Трон (TRX)'
}

currencies = {
    'eur': 'Евро',
    'jpy': 'Японская йена',
    'gbp': 'Фунт стерлингов',
    'aud': 'Австралийский доллар',
    'rub': 'Российский рубль',
    'cad': 'Канадский доллар',
    'usd': 'Американский доллар',
    'cny': 'Китайский юань'
}

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