# importing the calendar module
import calendar
# import tkinter module
from tkinter import *


# The function will display a calendar of a given year

def showCalender():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calendar for the Year")
    gui.geometry("550x600")
    year = int(year_fieled.get())
    # year1 = float(year)
    gui_content = calendar.calendar(year)
    calenderYear = Label(gui, text=gui_content, font=("Consoles", 10 ,"bold"))
    calenderYear.grid(row=5, column=1, padx=20)
    gui.mainloop()


#     Main code/driver code. Execution starts here
if __name__ == '__main__':
    new = Tk()
    new.config(background='grey')
    new.title("CALENDAR")
    new.geometry("250x140")
    calenda = Label(new, text='Calender', bg="grey", font=("times", 28, "bold"))
    # label for to enter year
    year = (Label(new, text="Enter the year", bg="dark grey"))
    # text box for the input
    year_fieled = Entry(new)
    button = Button(new, text="Show Calender", fg="Black", bg="Blue", command=showCalender)
    Exit = Button(new, text="Exit", fg="Black", bg="Blue", command= showCalender)
    # adjusting the widgets positions
    calenda.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_fieled.grid(row=3, column=1)
    button.grid(row=4, column=1)
    Exit.grid(row=6, column=1)
    new.mainloop()


