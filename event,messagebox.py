# from tkinter import *
# window = Tk()
# window.title("Evennt Handdler")
# window.geometry("100x100")
# def handle_keypress(event):
#     print(event.char)
# window.bind("<Key>",handle_keypress)   
# def handle_click(event) :
#     print("\nthe button was clicked")
# button = Button(text="click me")
# button.pack()    
# button.bind("<Button - 1>",handle_click)
# window.mainloop()

from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x200")
def msd():
    messagebox.showwarning("Alert","stop!  Virus is found you are hecked")
button = Button(root,text="scam  for virus",command=msd)   
button.place(x=40,y=80) 
root.mainloop()