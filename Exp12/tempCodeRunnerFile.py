
# import tkinter as tk
# from tkinter import ttk

# top = tk.Tk()
# top.title("Tkinter Reference")
# top.geometry("500x700")

# # pack example
# f1 = tk.Frame(top)
# f1.pack()

# b1 = tk.Button(f1, text="Button 1")
# b2 = tk.Button(f1, text="Button 2")
# b3 = tk.Button(f1, text="Button 3")

# b1.pack(side="left")
# b2.pack(side="left")
# b3.pack(side="left")

# # grid example
# f2 = tk.Frame(top)
# f2.pack(pady=5)

# b4 = tk.Button(f2, text="Grid 1")
# b5 = tk.Button(f2, text="Grid 2")
# b6 = tk.Button(f2, text="Grid 3")

# b4.grid(row=0, column=0)
# b5.grid(row=0, column=1)
# b6.grid(row=1, column=0, columnspan=2)

# # place example
# f3 = tk.Frame(top, height=70)
# f3.pack(fill="x")
# f3.pack_propagate(False)

# tk.Button(f3, text="Place 1").place(x=20, y=10)
# tk.Button(f3, text="Place 2").place(x=130, y=10)
# tk.Button(f3, text="Place 3").place(x=240, y=10)

# # label
# label = tk.Label(top, text="Roll No")
# label.pack()

# # entry
# tk.Label(top, text="First Name").pack()
# entry = tk.Entry(top)
# entry.pack()

# # checkbutton
# v1 = tk.IntVar()
# v2 = tk.IntVar()

# tk.Checkbutton(top, text="Male", variable=v1).pack()
# tk.Checkbutton(top, text="Female", variable=v2).pack()

# # radiobutton
# v = tk.StringVar()

# tk.Radiobutton(top, text="Male", variable=v,
#                value="Male").pack()
# tk.Radiobutton(top, text="Female", variable=v,
#                value="Female").pack()

# # listbox
# lb = tk.Listbox(top, height=3)
# lb.insert(1, "Python")
# lb.insert(2, "Java")
# lb.insert(3, "C++")
# lb.pack()

# # scrollbar
# f4 = tk.Frame(top)
# f4.pack()

# scroll = tk.Scrollbar(f4)
# scroll.pack(side="right", fill="y")

# mylist = tk.Listbox(f4, height=3,
#                     yscrollcommand=scroll.set)

# for i in range(20):
#     mylist.insert(tk.END, "Line " + str(i))

# mylist.pack(side="left")
# scroll.config(command=mylist.yview)

# # menu
# menu = tk.Menu(top)
# top.config(menu=menu)

# filemenu = tk.Menu(menu, tearoff=0)
# menu.add_cascade(label="File", menu=filemenu)
# filemenu.add_command(label="New")
# filemenu.add_command(label="Open")
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=top.destroy)

# # combobox
# combo = ttk.Combobox(top, values=["Java", "Python", "C++"])
# combo.pack()
# combo.set("Java")

# # scale
# tk.Scale(top, from_=0, to=42).pack()
# tk.Scale(top, from_=0, to=100,
#          orient="horizontal").pack()

# # toplevel window
# def new_window():
#     win = tk.Toplevel(top)
#     win.title("Python")
#     tk.Label(win, text="This is a new window").pack()
#     tk.Button(win, text="Close",
#               command=win.destroy).pack()

# tk.Button(top, text="Open Window",
#           command=new_window).pack()

# # message
# msg = tk.Message(top, text="This is our Message",
#                  bg="lightgreen", width=200)
# msg.pack()

# # menubutton
# mb = tk.Menubutton(top, text="Click Here", relief="raised")
# mb.menu = tk.Menu(mb, tearoff=0)
# mb["menu"] = mb.menu
# mb.menu.add_command(label="Contact")
# mb.menu.add_command(label="About")
# mb.pack()

# # spinbox
# tk.Spinbox(top, from_=0, to=10).pack()

# # text
# txt = tk.Text(top, height=2, width=25)
# txt.pack()
# txt.insert(tk.END, "Python Tkinter")

# # canvas
# canvas = tk.Canvas(top, width=100, height=50, bg="white")
# canvas.pack()
# canvas.create_line(10, 10, 90, 40)

# # stop button
# tk.Button(top, text="Stop", command=top.destroy).pack()

# top.mainloop()
# d(label="About")
# mb.pack()

# # Spinbox
# tk.Spinbox(top, from_=0, to=10).pack()

# # Text
# txt = tk.Text(top, height=2, width=25)
# txt.pack()
# txt.insert(tk.END, "Python Tkinter")

# # Canvas
# canvas = tk.Canvas(top, width=100, height=50, bg="white")
# canvas.pack()
# canvas.create_line(10, 10, 90, 40)

# # Stop Button
# tk.Button(top, text="Stop",
#           command=top.destroy).pack(pady=5)

# # Run Program
# top.mainloop()
