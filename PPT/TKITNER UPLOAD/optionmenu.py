# Option Menu
from tkinter import *
root = Tk()

var1 = StringVar()
var2 = StringVar()
opt1 = OptionMenu(root, var1, 'Main', 'Idly', 'Dosai',
                  'Pizza')     # like Menubutton
opt2 = OptionMenu(root, var2, 'Side dish', 'Onion Sambar',
                  'Onion Tomato Chutney ', 'Pickle')   # but shows choice
opt1.pack(fill=X)
opt2.pack(fill=X)
var1.set('Main')
var2.set('Side dishes')


def state(): print(var1.get(), "&", var2.get())                  # linked variables


Button(root, command=state, text='state').pack()
root.mainloop()
