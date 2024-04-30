from tkinter import*
from tkinter import messagebox
import GUI
from PIL import Image,ImageTk

def valid(string):
    if " " in string or "'" in string or '"' in string or "\t" in string or "\n" in string:
          return False
    else:
          return True


class Login_System:
  def __init__(self, payroll_database, user_database):
    self.payroll_database = payroll_database
    self.user_database = user_database
    
    self.root= Tk()
    self.root.title("Employee Payroll Management System | Developed by Aadrito, Swagat & Nikhilesh")
    self.root.resizable(False, False)
    self.root.geometry("1230x500+150+140")
    self.root.config(bg="old lace")
    self.logo = ImageTk.PhotoImage(Image.open("Images\\logo.png").resize((425, 425), Image.ANTIALIAS))
    #self.logo=ImageTk.PhotoImage(file="Images\\logo.png")

    #=============IMAGE FRAME==============
    #logo_frame = Canvas(self.root, height = 405, width = 540,relief=RAISED, bg='old lace', bd = 0)
    logo_frame = Canvas(self.root, height = 1000, width = 1000,relief=RAISED, bg='old lace', bd = 0)
    #logo_frame.place(x=10,y=75)
    logo_frame.place(x=0,y=0)
    logo_frame.create_image(60, 80, anchor=NW, image=self.logo)
    #logo_frame.pack()


    """
    logo_frame=Frame(self.root,bg="white")
    logo_frame.place(x=20,y=62, height = 425, width = 540)

    logo_lbl=Label(logo_frame,image=self.logo,bg='old lace').grid()
    """
    #==============VARIABLES================
    self.uname=StringVar()
    self.passwd=StringVar()

    #=============LOGIN WINDOW==============
    login=Frame(self.root,bd=5,relief=RIDGE,bg="white")        
    login.place(x=555,y=75,width=650,height=410)
    title1=Label(login,text="USER LOGIN",font=("cambria",25,"bold"),bg="firebrick3",fg="yellow",anchor='w',padx=10).place(x=0,y=0,relwidth=1)

    lbluser=Label(login,text="Username :",font=("cambria",20,"bold"),bg="white",fg="black").place(x=15,y=130)
    txtuser=Entry(login,textvariable=self.uname,bd=3,font=("cambria",20),bg="light yellow",fg="black").place(x=200,y=130,width=400)
       
    lblpass=Label(login,text="Password :",font=("cambria",20,"bold"),bg="white",fg="black").place(x=15,y=200)
    txtpass=Entry(login,textvariable=self.passwd,bd=3,font=("cambria",20),show="*",bg="light yellow",fg="black").place(x=200,y=200,width=400)
    

    btn_login=Button(login,text="  LOGIN  ",command=self.login,font=("cambria",20),bg="green3",fg="black",width=12,height=1).place(x=410,y=300)
    #self.root.iconphoto(True, self.logo)

    title=Label(self.root,text='AASWANI THERMALS PVT. LTD.',font=("cambria",35,"bold"),bg="DodgerBlue4",fg="white",padx=10)
    title.place(x=0,y=0,relwidth=1)

    self.root.wm_iconphoto(True, self.logo)
    self.root.mainloop()


  def login(self):
    if self.uname.get()=="" or self.passwd.get()=="":
      messagebox.showerror("ERROR","All fields are required")
    elif not valid(self.uname.get()) or not valid(self.passwd.get()): #to prevent SQL-Injection attacks
        messagebox.showerror("ERROR","Invalid username or password")
    elif self.user_database.exists(self.uname.get()) and self.user_database.verify(self.uname.get(), self.passwd.get()):
      #messagebox.showinfo("SUCCESSFUL",f"Welcome {self.uname.get()}")
      self.root.destroy()
      GUI.Master(self.payroll_database).start()
    else:
      messagebox.showerror("ERROR","Invalid Username or Password")

