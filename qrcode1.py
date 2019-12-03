# import pyqrcode and tkinter module
import pyqrcode
from tkinter import *

# creating main tkinter window
root = Tk()

# creating fixed geometry of the tkinter window
root.geometry("450x100")
root.resizable(0,0)

# gives title
root.title("QRCode Generator")

# create label widget
l1 = Label(root, text = "Text to turn into QR Code", fg = "green")
l2 = Label(root, text = "Name QR Image file", fg = "green")

# grid method to arrange labels 
l1.grid(row = 1, column = 0, pady = 5)
l2.grid(row = 2, column = 0, pady = 5)

# entry widgets, used to take entry from user
e1 = Entry(root, width = 50)
e2 = Entry(root, width = 50)

# arrange entry widgets
e1.grid(row=1, column = 1, columnspan = 4)
e2.grid(row=2, column = 1, columnspan = 4)

def show():
	"""
	This generate a QR Code for the input given by user.
	Saves a .png file with name given by user.
	Display the QR Code.
	"""
	qr = pyqrcode.create(e1.get(), error='L', mode='binary')
	qr.png(e2.get()+".png", scale=3)
	qr.show()

# button widget 
b1 = Button(root, text = "Save & Show", 
	        command=show,
	        width = 20, 
	        activeforeground = "red", 
	        fg = "green") 

b2 = Button(root, text = "Exit", 
	        command=quit, 
	        width = 10, 
	        activeforeground = "red", 
	        fg = "green") 
  
# arranging button widgets 
b1.grid(row = 7, column = 3, pady = 5)
b2.grid(row = 7, column = 4, pady = 5) 

# infinite loop which can be terminated 
# by keyboard or mouse interrupt
root.mainloop()