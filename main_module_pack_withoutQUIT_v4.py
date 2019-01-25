from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("ReturnNFound")
root.geometry("1200x480")
   
class user:

    def choose(self):
        rootA = Tk()
        rootA.title("ReturnNFound")
        rootA.geometry("1200x480")
        font_style3 = ("arial",15)

        #deposit or retrieve
        question = Label(rootA,text="Do you want to deposit lost item or retrieve your belonging?",bg="grey",fg="white")
        question.config(font=font_style3)
        question.pack(fill=X,pady=30)

        #deposit button
        deposit_button = Button(rootA,text="Deposit",height=3,width=10,bd=3)
        deposit_button.pack(pady=40)

        #retrieve button
        retrieve_button = Button(rootA,text="Retrieve",height=3,width=10,bd=3)
        retrieve_button.pack(pady=40)

    def check(self):
        i=0
        error="no"
        username = id_entry.get()
        password = password_entry.get()

        file = open("id_password_point.txt","r")
        content = file.read().split(",")
        file.close()

        while True:
            if username == content[i] and password == content[i+1]:
                root.destroy()
                self.choose() 
                token="yes"
            elif i<=12:
                i=i+3
                token="no"
            elif i==14:
                error = "yes"
                token="yes"
            if token == "yes":
                break
            
        if error=="yes":
            tkinter.messagebox.showerror("Error","Incorrect ID or password.")     

    def __init__(self,master):
        frame = Frame(master)
        frame.pack(fill=X,pady=10)
        
        global id_entry
        global password_entry

        font_style1 = ("verdana",20,"bold")
        font_style2 = ("arial",10)
        
        #welcome
        welcome_word = Label(frame,text="Welcome to ReturnNFound!",bg="grey",fg="white")
        welcome_word.config(font=font_style1)
        welcome_word.pack(fill=X,pady=20)

        #id
        id_label = Label(frame,text="Student / Staff ID:")
        id_label.config(font=font_style2)
        id_label.pack(pady=5)
        id_entry = Entry(frame,bd=5)
        id_entry.pack(pady=5)

        #password
        password_label = Label(frame,text="Password:")
        password_label.config(font=font_style2)
        password_label.pack(pady=5)
        password_entry = Entry(frame,show="*",bd=5)
        password_entry.pack(pady=5)

        #login button
        login_button = Button(frame,text="Log in",command=self.check,width=7,bd=3)
        login_button.pack(pady=10)

usernow = user(root)
root.mainloop()
