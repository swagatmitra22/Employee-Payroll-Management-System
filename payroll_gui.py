import tkinter as tk
from PIL import ImageTk


class EmployeeSystem:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(
            "Employee Payroll Management System | Developed by Swagat Mitra | 22BAI1400")
        self.root.state("zoomed")
        self.root.config(bg="white")

        # self.logo=ImageTk.PhotoImage(file="C:\\Users\\swaga\\Downloads\logotext.jpg")

        title = tk.Label(self.root, text="EMPLOYEE PAYROLL MANAGEMENT SYSTEM", relief=tk.RAISED, font=(
            "cambria", 30, "bold"), anchor='w', bg="firebrick3", fg="white", padx=10).place(x=0, y=0, relwidth=1)
        title = tk.Button(self.root, relief=tk.RAISED, text="LOGOUT", font=(
            "cambria", 19, "bold"), bg="gold", fg="black", width=10).place(x=1377, y=0)

        # ====================Frame1=========================
        Frame1 = tk.Frame(self.root, bd=5, relief=tk.FLAT, bg="white")
        Frame1.place(x=5, y=55, width=200, height=725)
        title1 = tk.Label(Frame1, text="MENU", relief=tk.RAISED, font=(
            "cambria", 20, "bold"), bg="DodgerBlue4", fg="white", anchor='w', padx=10).place(x=0, y=0, relwidth=1)

        btn_employee = tk.Button(Frame1, bd=3, text="EMPLOYEE\n\nDETAILS", font=(
            "cambria", 20, "bold"), bg="sky blue", fg="black").place(x=0, y=40, relwidth=1, relheight=1/3)
        btn_salary = tk.Button(Frame1, bd=3, text="SALARY\n\nDETAILS", font=(
            "cambria", 20, "bold"), bg="sky blue", fg="black").place(x=0, y=273, relwidth=1, relheight=1/3)
        btn_slip = tk.Button(Frame1, bd=3, text="PAY\n\nSLIP", font=(
            "cambria", 20, "bold"), bg="sky blue", fg="black").place(x=0, y=500, relwidth=1, relheight=1/3)

        # ===================Frame2==========================
        Frame2 = tk.Frame(self.root, relief=tk.FLAT, bg="white")
        Frame2.place(x=300, y=145, width=1130, height=630)


root = tk.Tk()
obj = EmployeeSystem(root)
root.mainloop()
