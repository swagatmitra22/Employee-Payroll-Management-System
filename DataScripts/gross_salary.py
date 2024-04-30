import random
import mysql.connector

try:
    database = mysql.connector.connect(host = "localhost", user = "root", password = "sql-299792458", database = "payroll")
    cursor = database.cursor()
    cursor.execute("SELECT DISTINCT salary.id, salary.basic_salary, salary.choice_pay, salary.hra, salary.convenience_exp, salary.bonus, salary.overtime FROM employees INNER JOIN salary ON employees.id = salary.emp_id")
    records = cursor.fetchall()
    for record in records:
        cursor.execute(f"UPDATE salary SET gross_salary = {sum(record[1:])} WHERE id = {record[0]}")
        
    database.commit()
    
except Exception as e:
    print(e)