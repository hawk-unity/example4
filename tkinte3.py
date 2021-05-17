from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Hawk Application")
window.geometry('350x200')
rad1 = Radiobutton(window,text='1.Seçenek', value=1)
rad2 = Radiobutton(window,text='2.Seçenek', value=2)
rad3 = Radiobutton(window,text='3.Seçenek', value=3)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
window.mainloop()
