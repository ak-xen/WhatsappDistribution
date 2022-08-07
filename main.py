import time

import pywhatkit
from tkinter import Tk, Label, OUTSIDE, Text, Button, END
from tkinter import Entry
from pywhatkit.core.exceptions import CountryCodeException
import json


class MainWindow:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title('WWWWAY')
        self.main_window.geometry('600x600')
        self.txt = Text(self.main_window, width=60)
        self.txt.place(height=400, width=290, x=30, y=30, bordermode=OUTSIDE, anchor='nw')
        self.txt.focus()
        self.lbl = Label(self.main_window, text='Введите сообщение для пользователей :')
        self.lbl.place(x=30, y=10)
        self.btn_get = Button(self.main_window, text='Отправить сообщение!', command=self.parse_and_send_message)
        self.btn_get.place(x=340, y=31)
        self.btn_del = Button(self.main_window, text='Удалить текст!', command=self.del_text_field)
        self.btn_del.place(x=340, y=61)

        # Добавление текстовых полей для пополнения списка номеров
        self.label_name = Label(self.main_window, text='Введите имя :')
        self.label_name.place(x=30, y=450)
        self.entry_name = Entry(self.main_window, width=25)
        self.entry_name.place(x=30, y=470)

        self.label_number = Label(self.main_window, text='Введите номер телефона :')
        self.label_number.place(x=30, y=500)
        self.entry_number = Entry(self.main_window, width=25)
        self.entry_number.place(x=30, y=520)

        self.entry_button = Button(self.main_window, text="Записать", width=22, command=self.write_new_number)
        self.entry_button.place(x=30, y=550)

    def parse_and_send_message(self):
        text = self.txt.get(1.0, END)
        try:
            for i in self.get_phone_numbers():
                name = str(i.keys())
                number = str(i.values())
                time.sleep(3)
                pywhatkit.sendwhatmsg_instantly(number, text, tab_close=True, close_time=5)
        except CountryCodeException:
            pass
TODO: 'Обработать неверный ввод номера. Сделать вывод номеров на окно.'
    def del_text_field(self):
        self.txt.delete(1.0, END)

    def write_new_number(self):
        name = self.entry_name.get()
        number = self.entry_number.get()

        with open('phone_numbers.json', 'r') as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                self.create_json()
                data = json.load(file)
            file.close()

        with open('phone_numbers.json', 'w') as file:
            data.append({name: number})
            json.dump(data, file, indent=4, ensure_ascii=False)
            file.close()

        self.entry_number.delete(0, END)
        self.entry_name.delete(0, END)
        return
    @staticmethod
    def create_json():
        with open('phone_numbers.json', 'w') as file:
            json.dump([], file)
            file.close()

    def get_phone_numbers(self):
        with open('phone_numbers.json') as file:
            data = json.load(file)
            file.close()
            return data


if __name__ == '__main__':
    window = MainWindow()
    window.main_window.mainloop()
