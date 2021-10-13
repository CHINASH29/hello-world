

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import random
import re
from tkinter import scrolledtext


def clicked():
    filename = 'G:\\Sem 5\\Python\\LAB_PRGMS\\names.txt'
    mainstring = open(filename).read()
    alpha = combo.get()
    if (alpha.isalpha()):
        chnamelist = re.findall(r"\b" + alpha + "\w*", mainstring, re.I)
        if not len(chnamelist):
            tkinter.messagebox.showerror("Error", " Name does not match")
        else:
            randname = random.choice(chnamelist)
            lbl2 = Label(window, text="Suggested Name : " +
                         randname, font=("Cambria", 14), width=43)
            lbl2.place(x=20, y=130)

    else:
        tkinter.messagebox.showerror("Error", "Not an Alphabet or a string")


window = Tk()
window.title("Name Generator")
window.geometry('500x500')
lbl1 = Label(window, text="NAME GENERATOR", font=("Cambria", 20))
lbl1.pack()
lbl2 = Label(window, text="Starting With", font=("Cambria", 14))
lbl2.place(x=20, y=70)
combo = ttk.Combobox(window, width=10, height=10)
combo['values'] = (
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z')
combo.current(10)
combo.place(x=150, y=70)
btn1 = Button(window, text="Generate", width=15, command=clicked)
btn1.place(x=280, y=70)
filename = "G:\\Sem 5\\Python\\LAB_PRGMS\\names.txt"
mainstring = open(filename).read()
chnamelist = re.findall(r"\bm\w*", mainstring, re.I)
randname = random.sample(chnamelist, 12)
lbl3 = Label(window, text="Starting with M", font=("Cambria", 14))
lbl3.place(x=20, y=170)
mlist = ""
for i in randname:
    mlist = mlist + i + "\n"
text_area = scrolledtext.ScrolledText(
    window, wrap=tk.WORD, width=12, height=10, font=("Times New Roman", 15))
text_area.place(x=20, y=200)
text_area.insert(tk.INSERT, mlist)
lbl4 = Label(window, text="Starting with P", font=("Cambria", 14))
lbl4.place(x=180, y=170)

text_area1 = scrolledtext.ScrolledText(
    window, wrap=tk.WORD, width=12, height=10, font=("Times New Roman", 15))
text_area1.place(x=180, y=200)
chnamelist = re.findall(r"\bp\w*", mainstring, re.I)
randname = random.sample(chnamelist, 12)
mlist = ""
for i in randname:
    mlist = mlist + i + "\n"

text_area1.insert(tk.INSERT, mlist)
lbl5 = Label(window, text="Starting with N", font=("Cambria", 14))
lbl5.place(x=320, y=170)

text_area2 = scrolledtext.ScrolledText(
    window, wrap=tk.WORD, width=12, height=10, font=("Times New Roman", 15))
text_area2.place(x=320, y=200)
chnamelist = re.findall(r"\bn\w*", mainstring, re.I)
randname = random.sample(chnamelist, 12)
mlist = ""
for i in randname:
    mlist = mlist + i + "\n"

text_area2.insert(tk.INSERT, mlist)
window.mainloop()
