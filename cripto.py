# "Изучение API CoinGecko"
# "Создание графического интерфейса пользователя"
import tkinter as tk
from tkinter import ttk


class CryptoApp:
    def __init__(self, master):
        self.master = master
        master.title("Криптовалютный курс")
# "Создание выпадающего списка для выбора криптовалюты"

        self.crypto_var = tk.StringVar()
        crypto_list = ['bicoin', 'ethereum', 'ripple', 'litecoin','cardano']
        self.crypto_menu = ttk.Combobox(master, textvariable=self.crypto_var)
        self.crypto_menu['values'] = crypto_list
        self.crypto_menu.pack(pady=10)



