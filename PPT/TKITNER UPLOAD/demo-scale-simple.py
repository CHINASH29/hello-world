# Scale
from tkinter import *
root = Tk()
scl = Scale(root, from_=1, to=12, resolution=2)
scl.pack(expand=YES, fill=Y)


def report():
    print(scl.get())


Button(root, text='state', command=report).pack(side=RIGHT)
root.mainloop()
