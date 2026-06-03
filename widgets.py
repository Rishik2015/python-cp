from tkinter import *
from datetime import date

root = Tk()
root.title("getting started with widgets")
root.geometry('400x300')
lbl = Label(text = 'hello', fg = "white",bg = "blue",height=1 ,width = 300, font = ('Arial',20))
na_lbl = Label(text = 'phull name', bg = "#38b1d3",font= ('Arial',17))
name_ent = Entry(font = ('arial',17))

def display():
    name = name_ent.get()
    global message
    message = "Welcome to the appplication! \n Todays date is :"
    greet = "Hello"+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box = Text(height = 3,font = ("Arial",20))   

btn = Button(text = 'begin',command = display,height = 1,bg = "#008CFF",fg = 'white',font = ('Arial',18)) 
lbl.pack()
na_lbl.pack()
name_ent.pack()
btn.pack()
text_box.pack()

root.mainloop()

