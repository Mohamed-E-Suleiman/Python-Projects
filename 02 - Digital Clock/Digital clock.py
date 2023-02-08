from tkinter import Tk, Label
import time , sys

master = Tk()
master.title('Digital Clock')
clock = Label(master, font= ('Times new roman', 90), bg='Grey', fg='White')
clock.pack()

def get_time():
    time_var = time.strftime("%I:%M:%S %p")
    clock.config(text = time_var)
    clock.after(200, get_time)

get_time()
master.mainloop()