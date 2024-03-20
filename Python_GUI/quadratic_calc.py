from tkinter import *
from tkinter import messagebox

windows = Tk()
windows.geometry('500x500')
windows.title("Quadratic Function Calculator")


# Function for computing quadratic function
def formula():
    a1 = int(a.get())
    b1 = int(b.get())
    c1 = int(c.get())
    root = ((b1 ** 2) + (4 * a1 * c1)) ** (1 / 2)
    denominator = 2 * a1
    root1 = (-b1 + root) / denominator
    root2 = (-b1 - root) / denominator
    x1 = Label(fram, text="{:.3f}".format(root1), bg='#fffff5', width=12, padx=5,
               font=('arial', 12, 'bold'), border=2, anchor='w')
    x2 = Label(fram, text="{:.3f}".format(root2), bg='#fffff5', width=12, padx=5,
               font=('arial', 12, 'bold'), border=2, anchor='w')
    x1.place(x=20, y=10)
    x2.place(x=220, y=10)
    Label(fram, text="Root 1", fg='grey').place(x=60, y=40)
    Label(fram, text='Root 2', fg='grey').place(x=260, y=40)


lbl_instruction = Label(windows, text="\nEnter appropriate values to the input"
                                      " provided below")
lbl_instruction.pack()

line = Canvas()
line.create_line(50, 2, 335, 2, width=3, fill='brown')
line.pack()

lbl_x_square = Label(windows, text="Enter Coefficient [a]")
lbl_x = Label(windows, text="Enter Coefficient [b]")
lbl_const = Label(windows, text="Enter Coefficient [c]")
lbl_x_square.place(x=50, y=80)
lbl_x.place(x=50, y=130)
lbl_const.place(x=50, y=180)

a = Entry(windows, width=40, borderwidth=2)
b = Entry(windows, width=40, borderwidth=2)
c = Entry(windows, width=40, borderwidth=2)
a.place(y=82, x=180)
b.place(y=132, x=180)
c.place(y=182, x=180)

fram = LabelFrame(windows, text="Result pane", fg="brown",
                  font=('courier', 12, 'italic'), width=380,
                  height=200)
fram.place(x=50, y=230)
btn = Button(fram, text="Compute Result", font=('arial', 12, 'bold'),
             border=2, padx=10, pady=2, command=formula)
btn.place(x=110, y=100)

Label(windows, text="Coded by EnGentech", fg='grey', font=('courier', 8, 'italic')).place(x=300, y=430)

windows.mainloop()
