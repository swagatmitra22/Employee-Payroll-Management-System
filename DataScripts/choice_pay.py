import random
import mysql.connector

try:
    database = mysql.connector.connect(host = "localhost", user = "root", password = "sql-299792458", database = "payroll")
    cursor = database.cursor()
    cursor.execute("SELECT salary.id AS id, employees.joining_date, salary.`year` FROM employees INNER JOIN salary ON employees.id = salary.emp_id")
    records = cursor.fetchall()
    for record in records:
            ratio = min(10, record[2] - record[1].year) / 10
            salary = int(((5 * ratio) + 5) * 1000)
            cursor.execute(f"UPDATE salary SET choice_pay = {salary} WHERE id = {record[0]}")
        
    database.commit()
    
except Exception as e:
    print(e)