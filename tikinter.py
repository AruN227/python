from tkinter import *

window = Tk()
window.wm_title("India X1")

l1 = Label(window, text="Virat Kohli(C)")
l1.grid(row=0, column=2)

l2 = Label(window, text="Rohit Sharma(Vc)")
l2.grid(row=0, column=3)

l3 = Label(window, text="MS Dhoni(WK)")
l3.grid(row=3, column=0)

l4 = Label(window, text="KL Ragul")
l4.grid(row=3, column=1)

l5 = Label(window, text="Rishap Pant")
l5.grid(row=3, column=2)

l6 = Label(window, text="D.Karthik")
l6.grid(row=3, column=3)


l7 = Label(window, text="Jadeja")
l7.grid(row=3, column=4)

l8 = Label(window, text="Hardik")
l8.grid(row=3, column=5)

window.mainloop()