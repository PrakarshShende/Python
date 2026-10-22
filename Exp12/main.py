# 1. First GUI — first_gui.py
# import tkinter as tk

# root = tk.Tk()
# root.title("First GUI")
# root.mainloop()


# 2. Geometry Managers — geometry.py
# import tkinter as tk

# root = tk.Tk()
# root.title("Geometry Managers")
# root.geometry("300x250")

# # Pack
# tk.Button(root, text="Pack 1").pack()

# # Grid
# f = tk.Frame(root)
# f.pack()
# tk.Button(f, text="Grid 1").grid(row=0, column=0)
# tk.Button(f, text="Grid 2").grid(row=0, column=1)

# # Place
# tk.Button(root, text="Place").place(x=100, y=150)

# root.mainloop()


# 3. Label — label.py
# import tkinter as tk

# root = tk.Tk()
# root.title("Label")

# label = tk.Label(root, text="Roll no!")
# label.pack()

# root.mainloop()


# # 4. Button — button.py
# import tkinter as tk

# root = tk.Tk()
# root.title("Button")

# button = tk.Button(root, text="Stop", command=root.destroy)
# button.pack()

# root.mainloop()


# # 5. Entry — entry.py
# import tkinter as tk

# root = tk.Tk()
# root.title("Entry")

# tk.Label(root, text="First Name").grid(row=0, column=0)

# e1 = tk.Entry(root)
# e1.grid(row=0, column=1)

# root.mainloop()


# # 6. Checkbutton — checkbutton.py
# import tkinter as tk

# root = tk.Tk()
# root.title("Checkbutton")

# v1 = tk.IntVar()
# v2 = tk.IntVar()

# tk.Checkbutton(root, text="Male", variable=v1).pack()
# tk.Checkbutton(root, text="Female", variable=v2).pack()

# root.mainloop()


# # 7. Radiobutton — radiobutton.py
# import tkinter as tk

# root = tk.Tk()
# root.title("Radiobutton")

# v = tk.IntVar()

# tk.Radiobutton(root, text="Male", variable=v, value=1).pack()
# tk.Radiobutton(root, text="Female", variable=v, value=2).pack()

# root.mainloop()


# # 8. Listbox — listbox.py
# import tkinter as tk

# root = tk.Tk()
# root.title("Listbox")

# lb = tk.Listbox(root)
# lb.insert(1, "Python")
# lb.insert(2, "Java")
# lb.insert(3, "C++")
# lb.insert(4, "Any other")
# lb.pack()

# root.mainloop()


# # 9. Scrollbar — scrollbar.py
# import tkinter as tk

# root = tk.Tk()
# root.title("Scrollbar")

# scroll = tk.Scrollbar(root)
# scroll.pack(side="right", fill="y")

# lb = tk.Listbox(root, yscrollcommand=scroll.set)

# for i in range(100):
#     lb.insert(tk.END, "Line " + str(i))

# lb.pack()
# scroll.config(command=lb.yview)

# root.mainloop()


# # 10. Menu — menu.py
# import tkinter as tk

# root = tk.Tk()
# root.title("Menu")

# menu = tk.Menu(root)
# root.config(menu=menu)

# filemenu = tk.Menu(menu, tearoff=0)
# menu.add_cascade(label="File", menu=filemenu)

# filemenu.add_command(label="New")
# filemenu.add_command(label="Open")
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=root.destroy)

# helpmenu = tk.Menu(menu, tearoff=0)
# menu.add_cascade(label="Help", menu=helpmenu)
# helpmenu.add_command(label="About")

# root.mainloop()


# # 11. Combobox — combobox.py
# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.title("Combobox")

# label = tk.Label(root, text="Selected Item:")
# label.pack()

# combo = ttk.Combobox(root, values=["Java", "Python", "C++"])
# combo.pack()
# combo.set("Java")

# def show(event):
#     label.config(text="Selected Item: " + combo.get())

# combo.bind("<<ComboboxSelected>>", show)

# root.mainloop()


# # 12. Scale — scale.py
# import tkinter as tk

# root = tk.Tk()
# root.title("Scale")

# tk.Scale(root, from_=0, to=42).pack()
# tk.Scale(root, from_=0, to=200, orient="horizontal").pack()

# root.mainloop()


# # 13. Toplevel — toplevel.py
# import tkinter as tk

# root = tk.Tk()
# root.title("Main Window")

# win = tk.Toplevel(root)
# win.title("Python")

# tk.Label(win, text="Second Window").pack()

# root.mainloop()


# # 14. Message — message.py
# import tkinter as tk

# root = tk.Tk()
# root.title("Message")

# msg = tk.Message(root, text="This is our Message")
# msg.config(bg="lightgreen")
# msg.pack()

# root.mainloop()


# # 15. Menubutton — menubutton.py
# import tkinter as tk

# root = tk.Tk()
# root.title("Menubutton")

# mb = tk.Menubutton(root, text="Click here")
# mb.menu = tk.Menu(mb, tearoff=0)
# mb["menu"] = mb.menu

# v1 = tk.IntVar()
# v2 = tk.IntVar()

# mb.menu.add_checkbutton(label="Contact", variable=v1)
# mb.menu.add_checkbutton(label="About", variable=v2)

# mb.pack()

# root.mainloop()


# # 16. Spinbox — spinbox.py
# import tkinter as tk

# root = tk.Tk()
# root.title("Spinbox")

# spin = tk.Spinbox(root, from_=0, to=10)
# spin.pack()

# root.mainloop()


# # 17. Text — text.py
# import tkinter as tk

# root = tk.Tk()
# root.title("Text")

# txt = tk.Text(root, height=2, width=30)
# txt.pack()
# txt.insert(tk.END, "Python Tkinter")

# root.mainloop()


# # 18. Canvas — canvas.py
# import tkinter as tk

# root = tk.Tk()
# root.title("Canvas")

# canvas = tk.Canvas(root, width=200, height=150)
# canvas.pack()
# canvas.create_line(10, 10, 150, 100)

# root.mainloop()