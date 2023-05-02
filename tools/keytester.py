#!/usr/bin/env python3

from tkinter import Tk, ttk, StringVar

root = Tk()
key = StringVar()
root.bind_all("<Key>", lambda e: key.set(f"{e.keysym = }, {e.keycode = }"))

ttk.Label(root, textvariable=key).pack()

root.mainloop()
