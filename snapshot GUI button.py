import pyautogui
import tkinter as tk
from tkinter.filedialog import *
from tkinter import Canvas
root = tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def takeScreenshot():
    myScreenshot=pyautogui.screenshot()
    path=asksaveasfilename()
    myScreenshot.save(path+"ss.png")

Butt = tk.Button(text="Take SS", Command= takeScreenshot(), font=10)
canvas1.create_window(150,150,window=Butt)

root.mainloop()
