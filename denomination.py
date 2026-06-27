from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("DENOMINATION COUNTRE de italionito best de italion de fergusom")
root.configure(bg = "light blue")
root.geometry("600x500")
upload = Image.open("denomitation.png")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)


label = Label(root,image=image,bg = 'light blue')
label.place(x = 180 , y = 20)
label1 = Label(root,
               text = "Hey you silly goose wellllcomoe         "
               
bg = "light blue")
label1.place(relx  = 0.5,y = 340, anchor = CENTER)
def msg():
    MsgBox = messagebox.showinfo(
        "Alert",
        "do you want  the denomination county  "
    )
    if MsgBox == 'ok':
        topwin()
button1 = Button(
    root,text = 'get started'
    command = msg
    bg = 'brown'
    fg = 'white'
)
button1.place(x = 260,y = 360)





















