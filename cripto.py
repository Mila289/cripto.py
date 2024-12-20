# "Изучение API CoinGecko"
# "Создание графического интерфейса пользователя"

import tkinter as tk
from tkinter import ttk
import requests


class CryptoApp:
    def __init__(self, master):
        self.master = master
        master.title("Криптовалютный курс")
# "Создание выпадающего списка для выбора криптовалюты"

        self.crypto_var = tk.StringVar()
        crypto_list = ['bitcoin', 'ethereum', 'ripple', 'litecoin','cardano']
        self.crypto_menu = ttk.Combobox(master, textvariable=self.crypto_var)
        self.crypto_menu['values'] = crypto_list
        self.crypto_menu.pack(pady=10)


        self.currency_var = tk.StringVar()
        currency_list = ['usd', 'eur', 'gbp']
        self.currency_menu = ttk.Combobox(master, textvariable=self.currency_var)
        self.currency_menu['values'] = currency_list
        self.currency_menu.pack(pady=5)

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
        crypto_id = self.crypto_var.get().lower()
        currency = self.currency_var.get().lower()
        try:
            response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={currency}")
            data = response.json()
            if crypto_id in data and currency in data[crypto_id]:
                price=data[crypto_id][currency]
                self.result_text.delete(1.0,tk.END)
                self.result_text.insert(tk.END, f"{crypto_id} в {currency}:{price}")
            else:
                self.show_error_message("Не удалось получить данные о курсе.")
        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Произошла ошибка: {str(e)}")


    def show_error_message(self, message):
        error_window = tk.Toplevel(self.master)
        error_window.title("Ошибка")
        label=ttk.Label(error_window, text=message)
        label.pack(pady=20)
        close_button=ttk.Button(error_window, text="Закрыть", command=error_window.destroy)
        close_button.pack()


root=tk.Tk()
app=CryptoApp(root)
root.mainloop()









