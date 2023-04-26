import tkinter as tk    # import Tkinter package
from tkinter import *

# Define a function to return the text in the label and be added to a string
def click():
    name=entry.get() # get the text entred into the Entry dialog box and insert it to a variable name
    output["text"]=f"Hello {name}, how are you?"  # take the value that is in entry field and add it to the out text


root=tk.Tk()   # generating a root window
root.title("My first GUI design")
root.geometry("300x300")  # size of pop-up window
label=tk.Label(text="What is your name?",fg='black',bg='orange',width=15,height=2)
# or make the two previous lines of codes to one with label=tk.Label(text='Enter Name',height=2,width=25)
entry=tk.Entry(width=15)   #generate a user Entry dialog box with width of 15
button=tk.Button(text='Submit',command=click,fg='black',bg='orange') # Submit button and execute the run function
output=tk.Label(height=2,width=25)

# a menue bar in the root window
menu=Menu(root)
item=Menu(menu)
item.add_command(label='Menu')
menu.add_cascade(label='bar',menu=item)
root.config(menu=menu)

label.pack() # make visible the label on the window
entry.pack()
button.pack()
output.pack()
root.mainloop()  # open a new window and without calling this line, nothing will be popped up on the screen. Actually mainloop() will call an endless loop of the window







