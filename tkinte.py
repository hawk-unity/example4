from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Hawk application")
window.geometry('350x200')
chk_state = BooleanVar()
chk_state.set(True) #set check state
def text():
    print("Sustu bu gece karardı yine ay :| ")
    text()
def text2():
    print("Sen kötü biri değilsin onlar kötü :| ")
    text()
chk = Checkbutton(window, text='Sen kötü biri değilsin onlar kötü :|', command=text2)
chk2 = Checkbutton(window, text = 'Sustu bu gece karardı yine ay :|', command=text)
chk2.grid(column=0, row=1)
chk.grid(column=0, row=0)
window.mainloop()
