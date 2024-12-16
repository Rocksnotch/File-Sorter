import tkinter as tk
from tkinter import *
import os

# Main Window Configuration
mainWindow = tk.Tk(className=" File Rename Tool")
mainWindow.geometry("800x400")

# Main Window Widgets

# Menu Bar

menu = Menu(mainWindow)
mainWindow.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open Folder...")
fileMenu.add_command(label="Open File(s)...")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=mainWindow.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='How to...')

# Main Window Intro Label
introLabel = Label(mainWindow, text="Welcome to the File Rename Tool!").pack()

# Main Window select File/Folder label
intro3Label = Label(mainWindow, text="Please select the file or folder you would like to rename in the 'file' tab.").pack()

# Main Window pick format label
intro2Label = Label(mainWindow, text="Please select the date format of the files you would like to rename:").pack()

# Main Window Date Choice Radio Buttons
dateChoice = IntVar()
Radiobutton(mainWindow, text="MM-DD-YYYY", variable=dateChoice, value=1).pack()
Radiobutton(mainWindow, text="DD-MM-YYYY", variable=dateChoice, value=2).pack()


mainWindow.mainloop()


