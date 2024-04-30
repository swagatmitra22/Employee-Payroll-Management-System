from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
import datetime
import Database
from datetime import date
from fpdf import FPDF
import os

class EmployeeFrame:

    def on_clear(self):
        self.master.employee = 0
        self.master.showEmployee()


    def update(self):
        try:
            emp_id = int(self.emp_id.get())
        except ValueError:
            tk.messagebox.showerror("ERROR","Invalid ID")
            return
        details = self.master.database.getEmployeeDetails(emp_id)
        if (details.empty):
            tk.messagebox.showerror("ERROR","Record not found")
        else:
            self.master.employee = emp_id
            try:
                self.image = ImageTk.PhotoImage(Image.open(f"Images\\employees\\{str(emp_id)}.png").resize((200, 200), Image.ANTIALIAS))
            except Exception:
                self.image = ImageTk.PhotoImage(Image.open(f"Images\\employees\\default.png").resize((200, 200), Image.ANTIALIAS))
            self.t.configure(image = self.image)
            self.name.set(details.at[0, "name"])
            self.gender.set(details.at[0, "gender"])
            self.birth_date.set(details.at[0, "birth_date"])
            self.joining_date.set(details.at[0, "joining_date"])
            self.age.set((datetime.date.today().year - details.at[0, "birth_date"].year) - 1)
            self.department.set(details.at[0, "department"])
            self.experience.set(2023 - details.at[0, "joining_date"].year)
            self.mail.set(details.at[0, "email"])
            self.alt_mail.set(details.at[0, "alt_email"])
            self.present_address.set(details.at[0, "present_address"])
            self.permanent_address.set(details.at[0, "permanent_address"])
            self.designation.set(details.at[0, "designation"])
            self.id_proof.set(details.at[0, "proof_of_identity"])
            self.id_type.set(details.at[0, "proof_of_identity_type"].upper())
            self.contact.set(details.at[0, "contact"])
            self.alt_contact.set(details.at[0, "alt_contact"])
            self.status.set(details.at[0, "status"])

    def on_refresh(self):
        self.master.database = Database.PayrollDatabase()
        if self.master.employee != 0:
            self.emp_id.set(str(self.master.employee))
            self.update()
        

    def __init__(self, master, employees):
        self.master = master

        self.root=self.master.main
        self.root.config(bg="old lace")

        self.emp_id = tk.StringVar()

        self.empid=Label(self.root,text="Employee ID :",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.empid.place(x=0,y=40)
        self.txt_id=ttk.Combobox(self.root, textvariable = self.emp_id, values = employees, font=("cambria",20))
        self.txt_id.place(x=200,y=40,width=250)
        #=================Button==================
        self.btn_browse=Button(self.root,bd=3,text="Search",font=("cambria",20),bg="chartreuse2",fg="black", command = self.update)
        self.btn_browse.place(x=490,y=35,width=160,height=42)
        self.btn_clear=Button(self.root,bd=3,text="Clear",font=("cambria",20),bg="firebrick3",fg="yellow", command = self.on_clear)
        self.btn_clear.place(x=680,y=35,width=160,height=42)
        self.btn_refresh=Button(self.root,bd=3,text="Refresh",font=("cambria",20),bg="light salmon",fg="black", command = self.on_refresh)
        self.btn_refresh.place(x=870,y=35,width=160,height=42)

        #=================Text====================

        self.empname=Label(self.root,text="Name:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.empname.place(x=0,y=110)
        self.name = tk.StringVar()
        self.txt_name=Entry(self.root,state=DISABLED, textvariable=self.name, font=("cambria",20),bg="white",fg="black")
        self.txt_name.place(x=200,y=110,width=250)

        self.empdob=Label(self.root,text="Date of Birth:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.empdob.place(x=480,y=110)
        self.birth_date = tk.StringVar()
        self.txt_dob=Entry(self.root,state=DISABLED,textvariable=self.birth_date,font=("cambria",20),bg="white",fg="black")
        self.txt_dob.place(x=730,y=110,width=250)

        self.empsex=Label(self.root,text="Sex:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.empsex.place(x=0,y=180)
        self.gender = tk.StringVar()
        self.txt_sex=Entry(self.root,state=DISABLED,textvariable=self.gender, font=("cambria",20),bg="white",fg="black")
        self.txt_sex.place(x=90,y=180,width=130)

        self.empage=Label(self.root,text="Age:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.empage.place(x=230,y=180)
        self.age = tk.StringVar()
        self.txt_age=Entry(self.root,state=DISABLED, textvariable=self.age,font=("cambria",20),bg="white",fg="black")
        self.txt_age.place(x=320,y=180,width=130)

        self.empdoj=Label(self.root,text="Date of Joining:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.empdoj.place(x=480,y=180)
        self.joining_date = tk.StringVar()
        self.txt_doj=Entry(self.root,state=DISABLED,textvariable=self.joining_date,font=("cambria",20),bg="white",fg="black")
        self.txt_doj.place(x=730,y=180,width=250)

        self.empdept=Label(self.root,text="Department:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.empdept.place(x=0,y=250)
        self.department = tk.StringVar()
        self.txt_dept=Entry(self.root,state=DISABLED,textvariable=self.department,font=("cambria",20),bg="white",fg="black")
        self.txt_dept.place(x=200,y=250,width=250)

        self.empdesg=Label(self.root,text="Designation:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.empdesg.place(x=480,y=250)
        self.designation = tk.StringVar()
        self.txt_desg=Entry(self.root,state=DISABLED,textvariable=self.designation, font=("cambria",20),bg="white",fg="black")
        self.txt_desg.place(x=730,y=250,width=250)

        self.empexp=Label(self.root,text="Experience:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.empexp.place(x=0,y=320)
        self.experience = tk.StringVar()
        self.txt_exp=Entry(self.root,state=DISABLED, textvariable=self.experience, font=("cambria",20),bg="white",fg="black")
        self.txt_exp.place(x=200,y=320,width=250)

        self.empproof=Label(self.root,text="ID Proof Type:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.empproof.place(x=480,y=320)
        self.id_type = tk.StringVar()
        self.txt_proof=Entry(self.root,state=DISABLED,textvariable=self.id_type,font=("cambria",20),bg="white",fg="black")
        self.txt_proof.place(x=730,y=320,width=250)

        self.empidno=Label(self.root,text="ID:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.empidno.place(x=1000,y=320)
        self.id_proof = tk.StringVar()
        self.txt_idno=Entry(self.root,state=DISABLED,textvariable=self.id_proof,font=("cambria",20),bg="white",fg="black")
        self.txt_idno.place(x=1100,y=320,width=200)

        self.empemail=Label(self.root,text="Email ID:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.empemail.place(x=0,y=390)
        self.mail = tk.StringVar()
        self.txt_email=Entry(self.root,state=DISABLED,textvariable=self.mail,font=("cambria",20),bg="white",fg="black")
        self.txt_email.place(x=200,y=390,width=780)

        self.empcontact=Label(self.root,text="Contact:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.empcontact.place(x=0,y=530)
        self.contact = tk.StringVar()
        self.txt_contact=Entry(self.root,state=DISABLED,textvariable=self.contact,font=("cambria",20),bg="white",fg="black")
        self.txt_contact.place(x=200,y=530,width=250)

        self.empsts=Label(self.root,text="Status:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.empsts.place(x=1000,y=530)
        self.status = tk.StringVar()
        self.txt_sts=Entry(self.root,state=DISABLED,textvariable=self.status,font=("cambria",20),bg="white",fg="black")
        self.txt_sts.place(x=1100,y=530,width=200)

        self.empaltemail=Label(self.root,text="Alt Email ID:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.empaltemail.place(x=0,y=460)
        self.alt_mail = tk.StringVar()
        self.txt_altemail=Entry(self.root,state=DISABLED,textvariable=self.alt_mail,font=("cambria",20),bg="white",fg="black")
        self.txt_altemail.place(x=200,y=460,width=780)

        self.empaltcon=Label(self.root,text="Alt Contact:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.empaltcon.place(x=480,y=530)
        self.alt_contact = tk.StringVar()
        self.txt_altcon=Entry(self.root,state=DISABLED,textvariable=self.alt_contact,font=("cambria",20),bg="white",fg="black")
        self.txt_altcon.place(x=730,y=530,width=250)

        self.emppradd=Label(self.root,text="Present Address:",font=("cambria",20),bg="old lace",fg="black",anchor='sw',padx=10)
        self.emppradd.place(x=0,y=600)
        self.present_address = tk.StringVar()
        self.txt_pradd=Entry(self.root,state=DISABLED,textvariable=self.present_address,font=("cambria",20),bg="white",fg="black")
        self.txt_pradd.place(x=280,y=600,width=1020)

        self.empperadd=Label(self.root,text="Permanent Address:",font=("cambria",20),bg="old lace",fg="black",anchor='sw',padx=10)
        self.empperadd.place(x=0,y=670)
        self.permanent_address = tk.StringVar()
        self.txt_peradd=Entry(self.root,state=DISABLED,textvariable=self.permanent_address,font=("cambria",20),bg="white",fg="black")
        self.txt_peradd.place(x=280,y=670,width=1020)

        #=====================Image===================
        self.Frame1 = Canvas(self.root, height = 200, width = 200,relief=RAISED, bg='black')
        self.Frame1.place(x=1100,y=40)
        self.image = ImageTk.PhotoImage(Image.open("Images\\employees\\default.png").resize((200, 200), Image.ANTIALIAS))
        self.t = Label(self.Frame1, image = self.image, bg = "old lace")
        self.t.pack()

        if self.master.employee != 0:
            self.emp_id.set(str(self.master.employee))
            self.update()

class SalaryFrame:

    def load(self):
        month = self.month.get()
        year = self.year.get()

        if self.master.employee == 0:
            tk.messagebox.showerror("ERROR","No employee selected")
            return
        elif month == "":
            tk.messagebox.showerror("ERROR","Month missing")
            return

        salary_details = self.master.database.getSalaryDetails(self.master.employee, month, year)
        if salary_details.empty:
            self.month.set(self.master.month)
            tk.messagebox.showerror("ERROR","No record found")
            return
        self.master.month = month
        self.master.year = year


        self.bank_name.set(salary_details.at[0, 'bank_name'])
        self.accno.set(salary_details.at[0, 'account_number'])
        self.accnm.set(salary_details.at[0, 'account_name'])
        self.ifsc.set(salary_details.at[0, 'ifsc'])
        self.wd.set(salary_details.at[0, 'working_days'])
        self.td.set(salary_details.at[0, 'total_days'])
        self.basic.set(salary_details.at[0, 'basic_salary'])
        self.pf.set(salary_details.at[0, 'provident_fund'])
        self.hra.set(salary_details.at[0, 'hra'])
        self.cpay.set(salary_details.at[0, 'choice_pay'])
        self.bpay.set(salary_details.at[0, 'bonus'])
        self.cex.set(salary_details.at[0, 'convenience_exp'])
        self.ot.set(salary_details.at[0, 'overtime'])
        self.deduc.set(salary_details.at[0, 'deductions'])
        self.gsalary.set(salary_details.at[0, 'gross_salary'])
        self.netsalary.set(salary_details.at[0, 'net_salary'])





    def __init__(self, master):

        MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

        self.master = master
        self.root=self.master.main
        self.root.config(bg="old lace")

        self.l_month=Label(self.root, text="Month:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_month.place(x=0,y=40)
        self.month = tk.StringVar()
        self.txt_month=ttk.Combobox(self.root,values = MONTHS, state="readonly",font=("cambria",20), textvariable = self.month)
        self.txt_month.place(x=150,y=40,width=200)

        self.l_year=Label(self.root,text="Year:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_year.place(x=380,y=40)
        self.year = tk.IntVar()
        if self.master.employee == 0:
            self.txt_year=ttk.Combobox(self.root,state="readonly", values = list(range(2023, 2003, -1)),font=("cambria",20), textvariable = self.year )
        else:
            self.txt_year=ttk.Combobox(self.root,state="readonly", values = list(range(2023, self.master.database.getJoiningDate(self.master.employee).at[0, "joining_date"].year - 1, -1)),font=("cambria",20), textvariable = self.year )
        self.txt_year.place(x=470,y=40,width=150)
        self.year.set(2023)

        self.calc=Button(self.root,text="Calculate",font=("cambria",20),bg="chartreuse2",fg="black",padx=10, command = self.load)
        self.calc.place(x=670,y=40, height = 40)

        self.l_bank_name=Label(self.root,text="Bank Name:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_bank_name.place(x=0,y=110)
        self.bank_name = tk.StringVar()
        self.txt_bank_name=Entry(self.root,state=DISABLED,font=("cambria",20),bg="white",fg="black", textvariable = self.bank_name )
        self.txt_bank_name.place(x=250,y=110,width=370)

        self.l_accno=Label(self.root,text="Account Number:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_accno.place(x=670,y=110)
        self.accno = tk.StringVar()
        self.txt_accno=Entry(self.root,state=DISABLED,font=("cambria",20),bg="white",fg="black", textvariable = self.accno )
        self.txt_accno.place(x=930,y=110,width=370)

        self.l_accnm=Label(self.root,text="Account Name:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_accnm.place(x=0,y=180)
        self.accnm = tk.StringVar()
        self.txt_accnm=Entry(self.root,state=DISABLED,font=("cambria",20),bg="white",fg="black", textvariable = self.accnm )
        self.txt_accnm.place(x=250,y=180,width=370)

        self.l_ifsc=Label(self.root,text="IFSC:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_ifsc.place(x=670,y=180)
        self.ifsc = tk.StringVar()
        self.txt_ifsc=Entry(self.root,state=DISABLED,font=("cambria",20),bg="white",fg="black", textvariable = self.ifsc )
        self.txt_ifsc.place(x=930,y=180,width=370)

        self.l_wd=Label(self.root,text="Working Days:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_wd.place(x=0,y=250)
        self.wd = tk.StringVar()
        self.txt_wd=Entry(self.root,state=DISABLED,font=("cambria",20),bg="white",fg="black", textvariable = self.wd )
        self.txt_wd.place(x=250,y=250,width=370)

        self.l_td=Label(self.root,text="Total Days:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_td.place(x=670,y=250)
        self.td = tk.StringVar()
        self.txt_td=Entry(self.root,state=DISABLED,font=("cambria",20),bg="white",fg="black", textvariable = self.td )
        self.txt_td.place(x=930,y=250,width=370)


        self.l_basic=Label(self.root,text="Basic Salary:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_basic.place(x=0,y=320)
        self.basic = tk.StringVar()
        self.txt_basic=Entry(self.root,state=DISABLED,font=("cambria",20),bg="white",fg="black", textvariable = self.basic )
        self.txt_basic.place(x=250,y=320,width=370)

        self.l_pf=Label(self.root,text="Provident Fund:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_pf.place(x=0,y=530)
        self.pf = tk.StringVar()
        self.txt_pf=Entry(self.root,state=DISABLED,font=("cambria",20),bg="white",fg="black", textvariable = self.pf )
        self.txt_pf.place(x=250,y=530,width=370)

        self.l_hra=Label(self.root,text="HRA:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_hra.place(x=0,y=390)
        self.hra = tk.StringVar()
        self.txt_hra=Entry(self.root,state=DISABLED,font=("cambria",20),bg="white",fg="black", textvariable = self.hra )
        self.txt_hra.place(x=250,y=390,width=370)

        self.l_cpay=Label(self.root,text="Choice Pay:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_cpay.place(x=670,y=390)
        self.cpay = tk.StringVar()
        self.txt_cpay=Entry(self.root,state=DISABLED,font=("cambria",20),bg="white",fg="black", textvariable = self.cpay )
        self.txt_cpay.place(x=930,y=390,width=370)

        self.l_bpay=Label(self.root,text="Bonus Pay:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_bpay.place(x=0,y=460)
        self.bpay = tk.StringVar()
        self.txt_bpay=Entry(self.root,state=DISABLED,font=("cambria",20),bg="white",fg="black", textvariable = self.bpay )
        self.txt_bpay.place(x=250,y=460,width=370)

        self.l_cex=Label(self.root,text="Convenience :",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_cex.place(x=670,y=320)
        self.cex = tk.StringVar()
        self.txt_cex=Entry(self.root,state=DISABLED,font=("cambria",20),bg="white",fg="black", textvariable = self.cex )
        self.txt_cex.place(x=930,y=320,width=370)

        self.l_ot=Label(self.root,text="Overtime:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_ot.place(x=670,y=460)
        self.ot = tk.StringVar()
        self.txt_ot=Entry(self.root,state=DISABLED,font=("cambria",20),bg="white",fg="black", textvariable = self.ot )
        self.txt_ot.place(x=930,y=460,width=370)

        self.l_deduc=Label(self.root,text="Deductions:",font=("cambria",20),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_deduc.place(x=0,y=600)
        self.deduc = tk.StringVar()
        self.txt_deduc=Entry(self.root,state=DISABLED,font=("cambria",20),bg="white",fg="black", textvariable = self.deduc )
        self.txt_deduc.place(x=250,y=600,width=370)

        self.l_gsalary=Label(self.root,text="Gross Salary:",font=("cambria",20, 'bold'),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_gsalary.place(x=670,y=530)
        self.gsalary = tk.StringVar()
        self.txt_gsalary=Entry(self.root,state=DISABLED,font=("cambria",20,'bold'),bg="white",fg="black", textvariable = self.gsalary )
        self.txt_gsalary.place(x=930,y=530,width=370)

        self.l_netsalary=Label(self.root,text="Net Salary:",font=("cambria",20,"bold"),bg="old lace",fg="black",anchor='w',padx=10)
        self.l_netsalary.place(x=670,y=600)
        self.netsalary = tk.StringVar()
        self.txt_netsalary=Entry(self.root,state=DISABLED,font=("cambria",20,"bold"),bg="white",fg="black", textvariable = self.netsalary)
        self.txt_netsalary.place(x=930,y=600,width=370)

        if self.master.employee != 0 and self.master.month != "" and self.master.year != 0:
            self.month.set(self.master.month)
            self.year.set(self.master.year)
            self.load()


class PaySlipFrame:
    
    def on_reset(self):
        self.master.employee = 0
        self.master.month = ""
        self.master.year = 2023
        self.master.showPaySlip()

    def on_pdf(self):
        if self.master.employee == 0:
            tk.messagebox.showerror("ERROR","No employee selected")
            return
        elif self.master.month == "":
            tk.messagebox.showerror("ERROR","Month missing")
            return
        elif self.master.year == 0:
            tk.messagebox.showerror("ERROR","Year missing")
            return
        elif self.details is None:
            tk.messagebox.showerror("ERROR","No record found")
            return
        pdf = FPDF(orientation='P', format=(120, 400))
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_font('Times', '', 12)
        for line in self.print.split('\n'):
            pdf.cell(0, 10, line, 0, 1)
        folder_path = filedialog.asksaveasfile(initialfile=f"{self.master.employee}.pdf")
        pdf.output(folder_path.name, 'F')

    def __init__(self, master):
        self.VIEW_TEMPLATE = "				           AASWANI THERMALS PVT. LTD.\n	         				Kolkata, West Bengal\n_____________________________________________________________________________________________________________________________________________\n	Employee ID :		{0}				Employee Name :		{1}\n	Sex :		{2}				Department :		{3}\n	Contact :		{4}				Email ID : 		{5}\n_____________________________________________________________________________________________________________________________________________\n	Salary of : 		{6}				Generated on :		{7}\n	Bank Name:		{8}				IFSC :		{9}\n	Acc. No. :		{10}				Acc. Name :		{11}\n	Days Present :		{12}				Days Absent :		{13}\n	Basic Salary :		{14}				Convenience :		{15}\n	HRA :		{16}				Choice Pay :		{17}\n	Bonus Pay :		{18}				Overtime :		{19}\n_____________________________________________________________________________________________________________________________________________\n	Gross Salary :		{20}\n_____________________________________________________________________________________________________________________________________________		Provident Fund :		{21}				Deductions :		{22}\n_____________________________________________________________________________________________________________________________________________\n	Net Salary :		{23}\n_____________________________________________________________________________________________________________________________________________\n** This is a computer generated slip, does not require signature of authority.\n** All the payment values are written in INR.\n\n"
        self.PDF_TEMPLATE = "              AASWANI THERMALS PVT. LTD.\n                          Kolkata, West Bengal\n______________________________________________\n	Employee ID :\t\t\t\t\t\t\t\t\t\t\t {0}\n Employee Name :\t\t\t\t\t\t {1}\n	Sex : \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{2}\n Department :               {3}\n	Contact :                      {4}\n Email ID :                   {5}\n______________________________________________\n	Salary of : 	         	        {6}\n Generated on :           	 {7}\n Bank Name:	               	{8}\n IFSC :	                          {9}\n	Acc. No. :                   	 {10}\n Acc. Name :	                {11}\n	Days Present :		            {12}\n Days Absent :	            	{13}\n	Basic Salary :	            	{14}\n Convenience :		    \t     \t\t{15}\n	HRA :	                        	{16}\n Choice Pay :	            	  {17}\n	Bonus Pay :		               {18}\n Overtime :	              	    {19}\n	Gross Salary :		            {20}\n______________________________________________    				\n Provident Fund :		        {21}\n Deductions :              	  {22}\n Net Salary :	                 {23}\n______________________________________________\n** This is a computer generated slip, does not \nrequire signature of authority.\n** All the payment values are written in INR.\n\n"


        self.master = master

        try:
            self.details = self.master.database.getAllDetails(self.master.employee, self.master.month, self.master.year)
            self.view = self.VIEW_TEMPLATE.format(self.details.at[0, 'id'], self.details.at[0, 'name'], self.details.at[0, 'gender'], self.details.at[0, 'department'], self.details.at[0, 'mobile'],
                                                  self.details.at[0, 'email'], f"{self.master.month}, {self.master.year}", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), self.details.at[0, 'bank_name'], self.details.at[0, 'ifsc'], self.details.at[0, 'account_number'], 
                                                  self.details.at[0, 'account_name'], self.details.at[0, 'working_days'], self.details.at[0, 'total_days'], self.details.at[0, 'basic_salary'], self.details.at[0, 'convenience_exp'], 
                                                  self.details.at[0, 'hra'], self.details.at[0, 'choice_pay'], self.details.at[0, 'bonus'], self.details.at[0, 'overtime'], self.details.at[0, 'gross_salary'], self.details.at[0, 'provident_fund'],
                                                  self.details.at[0, 'deductions'], self.details.at[0, 'net_salary'])
            self.print = self.PDF_TEMPLATE.format(self.details.at[0, 'id'], self.details.at[0, 'name'], self.details.at[0, 'gender'], self.details.at[0, 'department'], self.details.at[0, 'mobile'],
                                                  self.details.at[0, 'email'], f"{self.master.month}, {self.master.year}", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), self.details.at[0, 'bank_name'], self.details.at[0, 'ifsc'], self.details.at[0, 'account_number'], 
                                                  self.details.at[0, 'account_name'], self.details.at[0, 'working_days'], self.details.at[0, 'total_days'], self.details.at[0, 'basic_salary'], self.details.at[0, 'convenience_exp'], 
                                                  self.details.at[0, 'hra'], self.details.at[0, 'choice_pay'], self.details.at[0, 'bonus'], self.details.at[0, 'overtime'], self.details.at[0, 'gross_salary'], self.details.at[0, 'provident_fund'],
                                                  self.details.at[0, 'deductions'], self.details.at[0, 'net_salary'])
        except Exception:
            self.details = None
            self.view = ""
            self.print = self.PDF_TEMPLATE

        self.root=self.master.main
        self.root.config(bg="old lace")

        #==============Pay Slip Frame====================
        sal_Frame=Frame(self.root,relief=RIDGE,bg='white',bd=3)
        sal_Frame.place(x=30,y=30,width=1300,height=550)


        btn_reset=Button(self.root,text="Reset",font=("cambria",20),bd=3,bg="firebrick3",fg="yellow", command = self.on_reset).place(x=30,y=625,width=200)
        btn_save=Button(self.root,text="Save as PDF",font=("cambria",20),bd=3,bg="chartreuse2",fg="black", command = self.on_pdf).place(x=1130,y=625,width=200)

        scroll_y=Scrollbar(sal_Frame,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.slip=Text(sal_Frame, font=("cambria",17),bg="white",fg="black",yscrollcommand=scroll_y.set)
        self.slip.insert(tk.END, self.view)
        self.slip.config(state = DISABLED)
        self.slip.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.slip.yview)