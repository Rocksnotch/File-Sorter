import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
import os
import datetime as dt

# Global Variables
folder = ""
file = ""
fileTypes = [".png", ".jpg", ".jpeg", ".psd", ".txt", ".clip", ".gif"]


# Functions

def errorBox(message):
    errorWindow = tk.Tk()
    errorWindow.geometry("200x100")
    errorLabel = Label(errorWindow, text=message).pack()
    errorButton = Button(errorWindow, text="OK", command=errorWindow.destroy).pack()
    errorWindow.mainloop()

def selectFolder():
    global folder
    global file

    folder = fd.askdirectory()
    selectedLabel.config(text="Selected: " + folder)

    file = ""


def selectFile():
    global file
    global folder

    file = fd.askopenfilenames()
    if len(file) == 1:
        selectedLabel.config(text="Selected: " + file[0])
    else:
        selectedLabel.config(text="Selected: " + str(len(file)) + " files")

    folder = ""

def renameFile():
    global folder
    global file
    global dateChoice
    fileList = []

    if not folder and not file:
        errorBox("Please select a file or folder.")
        return

    if not dateChoice:
        errorBox("Please select a date format.")
        return

    if folder:
        fileList = os.listdir(folder)

        for file in fileList:
            if file.endswith(tuple(fileTypes)):
                if dateChoice.get() == 1:
                    date = dt.datetime.fromtimestamp(os.path.getmtime(folder + "/" + file)).strftime("%m-%d-%Y")
                else:
                    date = dt.datetime.fromtimestamp(os.path.getmtime(folder + "/" + file)).strftime("%d-%m-%Y")


                new_name = date + os.path.splitext(file)[1]

                try:
                    os.rename(os.path.join(folder, file), os.path.join(folder, new_name))
                except FileExistsError:
                    base, extension = os.path.splitext(new_name)
                    counter = 1
                    new_name_with_counter = f"{base}-{counter}{extension}"
                    while os.path.exists(os.path.join(folder, new_name_with_counter)):
                        counter += 1
                        new_name_with_counter = f"{base}-{counter}{extension}"
                    os.rename(os.path.join(folder, file), os.path.join(folder, new_name_with_counter))
        folder = ""
        file = ""
        fileList.clear()
        selectedLabel.config(text="Selected: None")
        
    if file:
        for f in file:
            if dateChoice.get() == 1:
                date = dt.datetime.fromtimestamp(os.path.getmtime(f)).strftime("%m-%d-%Y")
            else:
                date = dt.datetime.fromtimestamp(os.path.getmtime(f)).strftime("%d-%m-%Y")

            new_name = date + os.path.splitext(f)[1]

            try:
                os.rename(f, os.path.join(os.path.dirname(f), new_name))
            except FileExistsError:
                base, extension = os.path.splitext(new_name)
                counter = 1
                new_name_with_counter = f"{base}-{counter}{extension}"
                while os.path.exists(os.path.join(os.path.dirname(f), new_name_with_counter)):
                    counter += 1
                    new_name_with_counter = f"{base}-{counter}{extension}"
                os.rename(f, os.path.join(os.path.dirname(f), new_name_with_counter))
        folder = ""
        file = ""
        selectedLabel.config(text="Selected: None")

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
mmddyyyy = Radiobutton(mainWindow, text="MM-DD-YYYY", variable=dateChoice, value=1)
mmddyyyy.pack()

ddmmyyyy = Radiobutton(mainWindow, text="DD-MM-YYYY", variable=dateChoice, value=2)
ddmmyyyy.pack()

# Main Window Rename Button

renameButton = Button(mainWindow, text="Rename", command=lambda: renameFile())
renameButton.pack()


mainWindow.mainloop()


