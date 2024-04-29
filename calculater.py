from tkinter import *

def clear():
    display.delete(0, END)

def execute():
    try:
        result = eval(display.get())
        display.delete(0, END)
        display.insert(0, result)
    except Exception as e:
        display.delete(0, END)
        display.insert(0, "Error")

window = Tk()
window.title("Calculator")

display = Entry(window, width=60, bd=8, font=("arial", 20, "bold"), justify=RIGHT)
display.grid(row=0, column=0, columnspan=4)

btn1 = Button(window, text="1", width=6, height=2, command=lambda: display.insert(END, "1"))
btn2 = Button(window, text="2", width=6, height=2, command=lambda: display.insert(END, "2"))
btn3 = Button(window, text="3", width=6, height=2, command=lambda: display.insert(END, "3"))
btn4 = Button(window, text="4", width=6, height=2, command=lambda: display.insert(END, "4"))
btn5 = Button(window, text="5", width=6, height=2, command=lambda: display.insert(END, "5"))
btn6 = Button(window, text="6", width=6, height=2, command=lambda: display.insert(END, "6"))
btn7 = Button(window, text="7", width=6, height=2, command=lambda: display.insert(END, "7"))
btn8 = Button(window, text="8", width=6, height=2, command=lambda: display.insert(END, "8"))
btn9 = Button(window, text="9", width=6, height=2, command=lambda: display.insert(END, "9"))
btn0 = Button(window, text="0", width=6, height=2, command=lambda: display.insert(END, "0"))
btn_add = Button(window, text="+", width=6, height=2, command=lambda: display.insert(END, "+"))
btn_subtract = Button(window, text="-", width=6, height=2, command=lambda: display.insert(END, "-"))
btn_multiply = Button(window, text="*", width=6, height=2, command=lambda: display.insert(END, "*"))
btn_divide = Button(window, text="/", width=6, height=2, command=lambda: display.insert(END, "/"))
btn_exclamation = Button(window, text="!", width=6, height=2, command=lambda: display.insert(END, "!"))
btn_percentage = Button(window, text="%", width=6, height=2, command=lambda: display.insert(END, "%"))
btn_clear = Button(window, text="C", width=6, height=2, command=clear)
btn_equals = Button(window, text="=", width=6, height=2, command=execute)


btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn7.grid(row=3, column=0)
btn8.grid(row=3, column=1)
btn9.grid(row=3, column=2)
btn0.grid(row=4, column=0)
btn_clear.grid(row=4, column=1)
btn_equals.grid(row=4, column=2)
btn_subtract.grid(row=5, column=0)
btn_add.grid(row=5, column=1)
btn_multiply.grid(row=5, column=2)
btn_divide.grid(row=5, column=3)
btn_exclamation.grid(row=4, column=3)
btn_percentage.grid(row=3,column=3)

window.mainloop()