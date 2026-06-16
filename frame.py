# from tkinter import *
# root = Tk()
# root.title("Login Frame")
# login_frame = Frame(root,bd=4,relief="groove",padx=20,pady=20)
# login_frame.pack(padx=30,pady=30)
# Label(login_frame,text= 'username').pack(anchor='w')
# Entry(login_frame).pack(fill ='x',pady = 5)

# Label(login_frame,text= 'pasword').pack(anchor='w')
# Entry(login_frame, show = '*').pack(fill ='x',pady = 5)

# Button(login_frame,text='login').pack(pady=10)

# root.mainloop()

from tkinter import *
root = Tk()
root.title('Login app')
root.geometry('400x400')
frame = Frame(master=root,height = 200,width =360,bg = "#ff0000")
