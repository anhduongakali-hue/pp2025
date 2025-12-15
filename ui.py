import tkinter as tk

window = tk.Tk()
window.title("tinkinter widgets ")
window.geometry("200x500")
tk.Label(window, text="This is a label").pack()
tk.Frame(window, width = 100, height = 100).pack()
from tkinter import messagebox
def onClick():
    messagebox.showinfo(message="Button 1 clicked")
tk.Button(window, text = "Button 1", command = onClick).pack()
entry = tk.Entry(window)
entry.insert(-1, "Entry for text input")
tk.Checkbutton(window, text = "Checkbutton option1").pack()
radioValue = tk.StringVar(value = "op1")
tk.Radiobutton(window, variable = radioValue,
text = "Radiobutton option 1", value = "op1")
tk.Radiobutton(window, variable = radioValue,
text = "Radiobutton option 2", value = "op2").pack()
icts = ["ICT", "I See Tea", "Icy Tea", "Ice City"]


listbox = tk.Listbox(window)
for i in icts:
    listbox.insert(icts.index(i), i)
from tkinter import ttk
icts = ["ICT", "I See Tea", "Icy Tea", "Ice City"]
ttk.Combobox(window, values = icts).pack()

mainloop = window.mainloop()