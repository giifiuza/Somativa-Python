# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry( "200x200" )

# Change the label text
def show():
	label.config( text = clicked.get() )

# Dropdown menu options
options = [
	"Brastemp",
	"Electrolux",
	"Samsung",
	"LG",
	"Consul",
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Choose")

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()

# Create button, it will change label text
button = Button( root , text = "click Me" , command = show ).pack()

# Create Label
label = Label( text="Choose one of them" )
# label.pack()

# Execute tkinter
root.mainloop()
