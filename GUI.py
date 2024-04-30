import tkinter as tk
from PIL import ImageTk
import MainFrames
import Payroll


class Title:

    def on_logout(self):
        self.root.destroy()
        Payroll.main()

    def __init__(self, root: tk.Tk):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack(side=tk.TOP, fill=tk.X)

        self.text = tk.Label(self.frame, text="EMPLOYEE PAYROLL MANAGEMENT SYSTEM", relief=tk.RAISED, font=(
            "cambria", 30, "bold"), anchor=tk.CENTER, bg="firebrick3", fg="white", padx=10)
        self.text.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.logout_btn = tk.Button(self.frame, relief=tk.RAISED, text="LOGOUT", font=(
            "cambria", 19, "bold"), bg="gold", fg="black", width=10, command=self.on_logout)
        self.logout_btn.pack(side=tk.RIGHT, fill=tk.Y)


class Menu:

    def __init__(self, master : tk.Frame):
        self.master = master

        self.root = master.root
        self.frame = tk.Frame(self.root, bg="red", width=175)
        self.frame.pack(side=tk.LEFT, fill=tk.Y)

        self.text = tk.Label(self.frame, text="MENU", relief=tk.FLAT, font=(
            "cambria", 20, "bold"), bg="DodgerBlue4", fg="white", anchor=tk.CENTER, padx=10)
        self.text.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        self.choice = tk.IntVar()
        self.choice.set(0)

        self.option1 = tk.Radiobutton(self.frame, variable=self.choice, value=0, indicatoron=0, bd=3, text="EMPLOYEE\n\nDETAILS", font=(
            "georgia", 19, "bold"), bg="sky blue", selectcolor="light blue", fg="black", command=master.showEmployee)
        self.option2 = tk.Radiobutton(self.frame, variable=self.choice, value=1, indicatoron=0, bd=3, text="SALARY\n\nDETAILS",  font=(
            "georgia", 19, "bold"), bg="sky blue", selectcolor="light blue", fg="black", command=master.showSalary)
        self.option3 = tk.Radiobutton(self.frame, variable=self.choice, value=2, indicatoron=0, bd=3, text="PAY\n\nSLIP",        font=(
            "georgia", 19, "bold"), bg="sky blue", selectcolor="light blue", fg="black", command=master.showPaySlip)

        self.option1.place(relx=0, rely=0.1, relwidth=1, relheight=0.3)
        self.option2.place(relx=0, rely=0.4, relwidth=1, relheight=0.3)
        self.option3.place(relx=0, rely=0.7, relwidth=1, relheight=0.3)


class Master:

    def showEmployee(self):
        self.main.destroy()
        self.main = tk.Frame(self.root)
        self.main.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20)
        self.value = MainFrames.EmployeeFrame(
            self, self.database.getEmployees())

    def showPaySlip(self):
        self.main.destroy()
        self.main = tk.Frame(self.root)
        self.main.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.value = MainFrames.PaySlipFrame(self)

    def showSalary(self):
        self.main.destroy()
        self.main = tk.Frame(self.root)
        self.main.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20)
        self.value = MainFrames.SalaryFrame(self)

    def __init__(self, database):

        self.employee = 0
        self.month = ""
        self.year = 0

        self.database = database

        self.root = tk.Tk()
        self.root.title(
            "Employee Payroll Management System | Developed by Aadrito & Swagat")
        self.root.geometry("1315x690+200+80")
        self.root.state("zoomed")
        self.root.config(bg="old lace")

        self.title = Title(self.root)

        self.menu = Menu(self)

        self.main = tk.Frame(self.root)
        self.main.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20)
        self.value = MainFrames.EmployeeFrame(self, database.getEmployees())

        self.logo = ImageTk.PhotoImage(file="Images\\logo.png")
        self.root.iconphoto(False, self.logo)

    def start(self):
        self.root.mainloop()
