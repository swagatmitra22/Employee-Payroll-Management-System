import random
import mysql.connector


try:
    database = mysql.connector.connect(host = "localhost", user = "root", password = "sql-299792458", database = "payroll")
    cursor = database.cursor()
    cursor.execute("SELECT DISTINCT salary.id, salary.gross_salary, salary.deductions, salary.provident_fund FROM employees INNER JOIN salary ON employees.id = salary.emp_id")
    records = cursor.fetchall()
    for record in records:
        cursor.execute(f"UPDATE salary SET net_salary = {record[1] - record[2] - record[3]} WHERE id = {record[0]}")
        
    database.commit()
    
except Exception as e:
    print(e)