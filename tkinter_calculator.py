from tkinter import *

root = Tk()

root.title("Simple Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END) 
    e.insert(0, str(current) + str(number))



def button_clear():
    e.delete(0, END)




def button_add():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + '+')

def button_sub():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + '-')

def button_mul():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + '*')

def button_div():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + '/')




def button_equal():
    res = eval(e.get())
    e.delete(0, END)
    e.insert(0, res)


button_1 = Button(root, text="1", padx=32, pady=15, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=32, pady=15, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=32, pady=15, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=32, pady=15, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=32, pady=15, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=32, pady=15, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=32, pady=15, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=32, pady=15, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=32, pady=15, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=32, pady=15, command=lambda: button_click(0))


button_equal = Button(root, text="=", padx=32, pady=15, command=button_equal)
button_clear = Button(root, text="Clear", padx=32, pady=15, command=button_clear)

button_add = Button(root, text="+", padx=32, pady=15, command=button_add) 
button_sub = Button(root, text="-", padx=32, pady=15, command=button_sub) 
button_mul = Button(root, text="*", padx=32, pady=15, command=button_mul) 
button_div = Button(root, text="/", padx=32, pady=15, command=button_div) 


# putting the buttons on the screen

button_1.grid(row=4,column=0)
button_2.grid(row=3,column=0)
button_3.grid(row=3,column=1)
button_4.grid(row=3,column=2)
button_5.grid(row=3,column=3)
button_6.grid(row=2,column=0)
button_7.grid(row=2,column=1)
button_8.grid(row=2,column=2)
button_9.grid(row=2,column=3)
button_0.grid(row=4,column=1)


button_clear.grid(row=4, column=2)
button_equal.grid(row=4, column=3)


button_add.grid(row=1, column=0)
button_sub.grid(row=1, column=1)
button_mul.grid(row=1, column=2)
button_div.grid(row=1, column=3)



root.mainloop()


