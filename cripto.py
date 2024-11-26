# "Изучение API CoinGecko"
# "Создание графического интерфейса пользователя"
import tkinter as tk
from tkinter import ttk, Label


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

# "Создание кнопки для отправки запроса"
        self.reques_button=ttk.Button(master, text="Получить курс", command=self.get_crypto_price)
        self.reques_button.pack()

# "Создание метки для отображения результата"
        self.result_label = ttk.Label(master, text="Результат:")
        self.result_label.pack(pady=10)

# "Создание поля для вывода результата"
        self.result_text = tk.Text(master, height=1, width=20)
        self.result_text.pack()

# "Реализация получения курса криптовалюты"
    def get_crypto_price(self):

         root=tk.Tk()
         app=CryptoApp(root)
         root.mainloop()







