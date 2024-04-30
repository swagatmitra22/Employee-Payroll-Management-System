import random
import mysql.connector

try:
    database = mysql.connector.connect(host = "localhost", user = "root", password = "sql-299792458", database = "payroll")
    cursor = database.cursor()
    cursor.execute("SELECT DISTINCT salary.id, employees.rent, salary.basic_salary FROM employees INNER JOIN salary ON employees.id = salary.emp_id")
    records = cursor.fetchall()
    for record in records:
            if (record[1] == 1):
                cursor.execute(f"UPDATE salary SET hra = {record[2]/2} WHERE id = {record[0]}")
            else:
                cursor.execute(f"UPDATE salary SET hra = 0 WHERE id = {record[0]}")
        
    database.commit()
    
except Exception as e:
    print(e)