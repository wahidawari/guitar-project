from tkinter import *
import tkinter as tk
import subprocess as sub
import os
import sys


p = sub.Popen('python hello.py',stdout=sub.PIPE,stderr=sub.PIPE)
output, errors = p.communicate()




root = Tk()

B=tk.Button(root,text="Hello",command= p.communicate())
B.pack()

text = Text(root)
text.pack()
text.insert(END, output)
root.mainloop()
