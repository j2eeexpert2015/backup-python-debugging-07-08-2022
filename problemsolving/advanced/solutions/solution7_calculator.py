# solution7_calculator.py

from tkinter import *
from decimal import *

# key press function:
def click(key):
    display.insert(END, key)

##### main:
window = Tk()
window.title("MyCalculator")

# create top_row frame
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# use Entry widget for an editable display
display = Entry(top_row, width=45, bg="light green")
display.grid()

# create num_pad_frame
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

num_pad_list = [
'7',  '8',  '9',
'4',  '5',  '6',
'1',  '2',  '3',
'0',  '.',  '=' ]

# create num_pad buttons with a loop
r = 0
c = 0
for btn_text in num_pad_list:
    # this will be fixed later:
    Button(num_pad, text=btn_text, width=5, command=click).grid(row=r,column=c)
    c = c+1
    if c > 2:
        c = 0
        r = r+1

# create operator_frame
operator = Frame(window)
operator.grid(row=1, column=1, sticky=E)

operator_list = [
'*', '/',  
'+', '-',
'(', ')',
'C' ]

# create operator buttons with a loop
r = 0
c = 0
for btn_text in operator_list:
    Button(operator, text=btn_text, width=5, command=click).grid(row=r,column=c)
    c = c+1
    if c > 1:
        c = 0
        r = r+1


##### Run mainloop
window.mainloop()
