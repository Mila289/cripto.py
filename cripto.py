# "Изучение API CoinGecko"
# "Создание графического интерфейса пользователя"
import tkinter as tk
from tkinter import ttk


class CryptoApp:
    def __init__(self, master):
        self.master = master
        master.title("Криптовалютный курс")
