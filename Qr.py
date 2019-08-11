# Python Program to create QRCode of User-Input text
# To do so pyqrcode module has to be installed

# Importing necessary packages
import pyqrcode
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image

#---

# Defining function to create widgets
def CreateWidgets():
    label = Label(text = "ENTER TEXT : ")
    label.grid(row = 0, column =1, padx = 5, pady = 5)

    root.entry = Entry(width = 30, textvariable = qrInput)
    root.entry.grid(row = 0, column = 2, padx = 5, pady = 5)

    button = Button(width = 10, text = "GENERATE", command = Generate)
    button.grid(row = 0, column = 3, padx = 5, pady = 5)

    label = Label(text = "QR CODE : ")
    label.grid(row = 1, column =1, padx = 5, pady = 5)

    # Canvas to display generated QR Code image
    root.canvas = Canvas(root, width = 350, height = 350)
    root.canvas.grid(row=2, column=1, columnspan = 3, padx=5, pady=5)

#---

# Defining Generate() function to create QRCode
def Generate():

    # Storing user-input text in a variable
    qrString = qrInput.get()

    # Checking if the user has entered some text then do the following
    if qrString != '':

        # Generate object of QRCode
        qrGenerate = pyqrcode.create(qrString)

        # Creating name for the image with user-input text as the name
        # and .png as the extension
        qrCodeName = qrString+".png"

        # Creating png image of the QRCode.
        # To create png image pypng module has to be installed
        qrGenerate.png(qrCodeName, scale = 10)

        # Creating object of PhotoImage class to display image
        root.img = ImageTk.PhotoImage(Image.open(qrCodeName))

        # Displaying QRCode image in the canvas
        root.canvas.create_image((root.img.width()/2), (root.img.height()/2),
                                 image = root.img)

    # If the user has not entered any text then error is shown
    else:
        messagebox.showerror("ERROR", "ENTER A TEXT.!")

#---

# Creating object root of tk
root = tk.Tk()

#Setting the title for the window
root.title("PyQR GENERATOR")
root.resizable(False, False)

# Creating tkinter variable
qrInput = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()