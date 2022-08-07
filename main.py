import pywhatkit
from tkinter import Tk, Label, OUTSIDE, Text, Button, END


class MainWindow():
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

    def parse_and_send_message(self):
        text = self.txt.get(1.0, END)
        pywhatkit.sendwhatmsg_instantly('', text, tab_close=True, close_time=5)

    def del_text_field(self):
        self.txt.delete(1.0, END)


if __name__ == '__main__':
    window = MainWindow()
    window.main_window.mainloop()
