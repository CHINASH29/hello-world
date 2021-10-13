import csv
import tkinter
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import filedialog
from tkinter import *


root = Tk()
with open("file.txt", "r") as f:
    Label(root, text=f.read()).pack()
root.mainloop()


window = Tk()

window.geometry('150x150')


def file_opener():
    input = filedialog.askopenfile(initialdir="/")
    print(input)
    for i in input:
        print(i)


x = Button(window, text='Select a .txt/.csv file', command=file_opener)
x.pack()
mainloop()


#import pandas as pd
root = tk.Tk()
tk.Label(root, text='File Path').grid(row=0, column=0)
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v).grid(row=0, column=1)


def import_csv_data():
    global v
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)

    #df = pd.read_csv(csv_file_path)
tk.Button(root, text='Browse Data Set',
          command=import_csv_data).grid(row=1, column=0)
tk.Button(root, text='Close', command=root.destroy).grid(row=1, column=1)
root.mainloop()


root = tkinter.Tk()
# open file
with open("salary_dataset.csv", newline="") as file:
    reader = csv.reader(file)

    r = 0  # r and c tell us where to grid the labels
    for col in reader:
        c = 0
        for row in col:
            label = tkinter.Label(root, width=10, height=2,
                                  text=row, relief=tkinter.RIDGE)
            label.grid(row=r, column=c)
            c += 1
        r += 1
root.mainloop()
