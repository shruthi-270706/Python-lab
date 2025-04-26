import tkinter as tk
m = tk.Tk()
m.title('Button Demonstration')
m.geometry("200x200")
b1 = tk.Button(m, text = "STOP", command=m.destroy, activebackground = "Red")
b2 = tk.Button(m, text = "Submit", width=20, height = 2,bd = 10, font = 20, command=m.destroy, bg = "blue")
b3 = tk.Button(m, text = "Clear")
b4 = tk.Button(m, text = "Nothing")
b1.pack(side = "top")
b1.grid(row = 0, column = 0,  pady = 15)
b2.grid(row = 0, column = 1,  pady = 15)
b3.grid(row = 1, column = 0,  pady = 15)
b4.grid(row = 1, column = 1,  pady = 15)
"""b1 = tk.Button(m, text = "Click me !", width = 20, height = 10, bd = 5,
               command = m.destroy)
b1.place(x = 20, y = 20)"""
m.mainloop()
"""b1.pack(side = 'left')
b2.pack(side = 'right')
b3.pack(side = 'top')
b4.pack()"""