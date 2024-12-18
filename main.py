import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
import os
import datetime as dt

# Global Variables
folder = ""
file = ""
fileTypes = [".png", ".jpg", ".jpeg", ".psd", ".txt"]


# Functions

def errorBox(message):
    errorWindow = tk.Tk()
    errorWindow.geometry("200x100")
    errorLabel = Label(errorWindow, text=message).pack()
    errorButton = Button(errorWindow, text="OK", command=errorWindow.destroy).pack()
    errorWindow.mainloop()

def selectFolder():
    global folder 
    folder = fd.askdirectory()
    selectedLabel.config(text="Selected: " + folder)

def selectFile():
    global file
    file = fd.askopenfilenames()
    if len(file) == 1:
        selectedLabel.config(text="Selected: " + file[0])
        print("File Type: " + os.path.splitext(file[0])[1])
    else:
        selectedLabel.config(text="Selected: " + str(len(file)) + " files")

def renameFile(dateChoice):
    global folder
    global file

    if not folder and not file:
        errorBox("Please select a file or folder.")
        return
    elif folder:
        print("Folder selected: " + folder)
    elif file:
        print("File selected: " + file[0])

    if not dateChoice:
        errorBox("Please select a date format.")
        return
    elif dateChoice == 1:
        print("Date format: MM-DD-YYYY")
    elif dateChoice == 2:
        print("Date format: DD-MM-YYYY")

    folder = ""
    file = ""

    pass

# Main Window Configuration
mainWindow = tk.Tk(className=" File Rename Tool")
mainWindow.geometry("800x400")

# Main Window Widgets

# Menu Bar

menu = Menu(mainWindow)
mainWindow.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open Folder...", command=selectFolder)
fileMenu.add_command(label="Open File(s)...", command=selectFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=mainWindow.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='How to...')

# Main Window Intro Label
introLabel = Label(mainWindow, text="Welcome to the File Rename Tool!").pack()

# Main Window select File/Folder label
intro3Label = Label(mainWindow, text="Please select the file or folder you would like to rename in the 'file' tab.").pack()

selectedLabel = Label(mainWindow, text="Selected: None")
selectedLabel.pack()

# Main Window pick format label
intro2Label = Label(mainWindow, text="Please select the date format of the files you would like to rename:").pack()

# Main Window Date Choice Radio Buttons
dateChoice = IntVar()
Radiobutton(mainWindow, text="MM-DD-YYYY", variable=dateChoice, value=1).pack()
Radiobutton(mainWindow, text="DD-MM-YYYY", variable=dateChoice, value=2).pack()

intro3Label = Label(mainWindow, text="Please select the file type(s) you want to rename (all that apply)").pack()

# Main Window File Type Checkboxes
fileTypeCheckboxes = []
for fileType in fileTypes:
    fileTypeCheckboxes.append(IntVar())
    Checkbutton(mainWindow, text=fileType, variable=fileTypeCheckboxes[-1]).pack()

# Main Window Rename Button

renameButton = Button(mainWindow, text="Rename", command=lambda: renameFile(dateChoice.get()))
renameButton.pack()


mainWindow.mainloop()


