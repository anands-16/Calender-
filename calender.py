import calendar
from tkinter import *

def showCalender():
    gui = Tk()
    gui.config(background = "black")
    gui.title("Calender of the year")
    gui.geometry("550x600")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text= gui_content,foreground = "white", font= "Consolas 10 bold",background = "black")
    calYear.grid(row=5, column=1,padx=20)
    gui.mainloop()


if __name__=='__main__':
    new = Tk()
    new.config(background = 'pink')
    new.title("Calender")
    new.geometry("250x140")
    year_field = Entry(new)
    cal = Label(new,text = "calender",bg = 'Blue',font = ("times", 28 ,"bold"))
    year = Label(new,text = "enter year",bg = 'green')
    button = Button(new,text = "show calender",bg ="yellow",command = showCalender)
    cal.grid(row = 1,column = 1)
    year.grid(row =2,column=1)
    year_field.grid(row =3,column=1)
    button.grid(row = 4,column= 3)
    new.mainloop()

