import mysql.connector
import pandas as pd
import hashlib


class PayrollDatabase:

    def __init__(self):
        self.database = mysql.connector.connect(
            host="localhost", user="root", password="6296", database="payroll")

    def getEmployees(self) -> list:
        """
        Function returns id of all employees found in the database
        """
        raw_query = "SELECT id FROM employees"
        return pd.read_sql(raw_query, con=self.database)["id"].tolist()

    def getEmployeeDetails(self, employee_id: int) -> pd.DataFrame:
        """
        Returns details of the employees matching given id as a PandaS Dataframe
        """
        raw_query = f"SELECT * FROM employees WHERE id = {employee_id}"
        return pd.read_sql(raw_query, con=self.database)

    # returns all salray details of an employee
    def getSalaryDetails(self, employee_id: int, month: str, year: int) -> pd.DataFrame:
        """
        Returns (month, bonus, convenience_exp, net_salary, gross_salary) from payslip as determined by employee id, month and year as a PandaS dataframe
        """
        raw_query = f"SELECT salary.`month` AS `month`, salary.`bonus` AS bonus, salary.`convenience_exp` AS convenience_exp, salary.`net_salary` AS net_salary, salary.`gross_salary` AS gross_salary, salary.`overtime` AS overtime, salary.`deductions` AS deductions, salary.`choice_pay` AS choice_pay, salary.`year` AS `year`, salary.working_days AS working_days, salary.emp_id AS emp_id, salary.basic_salary AS basic_salary, salary.total_days AS total_days, salary.provident_fund AS provident_fund, salary.hra AS hra, employees.bank_name AS bank_name, employees.account_name AS account_name, employees.account_number AS account_number, employees.ifsc AS ifsc FROM employees INNER JOIN salary ON employees.id = salary.emp_id WHERE emp_id = {employee_id} AND month = '{month}' AND year = {year}"
        return pd.read_sql(raw_query, con=self.database)

    # returns all details
    def getAllDetails(self, employee_id: int, month: str, year: int):
        raw_query = f"SELECT employees.id AS id, employees.gender AS gender, employees.`name` AS `name`, employees.department AS department, employees.contact AS mobile, employees.email AS email, salary.basic_salary AS basic_salary, employees.bank_name AS bank_name, employees.account_number AS account_number, salary.working_days AS working_days, salary.total_days AS total_days, employees.account_name AS account_name, employees.ifsc AS ifsc, salary.convenience_exp AS convenience_exp, salary.hra AS hra, salary.choice_pay AS choice_pay, salary.overtime AS overtime, salary.gross_salary AS gross_salary, salary.provident_fund AS provident_fund, salary.deductions AS deductions, salary.bonus AS bonus, salary.net_salary AS net_salary FROM salary INNER JOIN employees ON employees.id = salary.emp_id WHERE employees.id = {employee_id} AND salary.`year` = {year} AND salary.`month` = '{month}'"
        return pd.read_sql(raw_query, con=self.database)

    def getJoiningDate(self, employee_id: int):
        raw_query = f"SELECT joining_date FROM employees WHERE id = {employee_id}"
        return pd.read_sql(raw_query, con=self.database)


class UserDatabase:

    def __init__(self):
        self.database = mysql.connector.connect(
            host="localhost", user="root", password="6296", database="payroll")
        self.cursor = self.database.cursor()
        self.salt = "demo"

    def exists(self, username):
        raw_query = f"SELECT username FROM users WHERE username = '{username}'"
        self.cursor.execute(raw_query)
        result = self.cursor.fetchall()

        return len(result) > 0

    def verify(self, username, password):
        encryption = hashlib.sha224()
        encryption.update((username + password + self.salt).encode('utf-8'))
        encrypted = encryption.digest()

        raw_query = f"SELECT password FROM users WHERE username = '{username}'"
        self.cursor.execute(raw_query)
        result = self.cursor.fetchone()

        return result[0] == encrypted
