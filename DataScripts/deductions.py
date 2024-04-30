import random
import mysql.connector

def income_tax(sal):
    sal = sal * 12
    if (sal <= 250000):
        return 0
    elif (sal > 250000 and sal <= 500000):
        return ((sal - 250000) * 5) / (12 * 100)
    elif (sal > 500000 and sal <= 1000000):
        return (12500/12) + float(((sal - 500000) * 20) / (12 * 100))
    else:
        return (112500/12) + float(((sal - 1000000) * 30) / (12 * 100))


try:
    database = mysql.connector.connect(host = "localhost", user = "root", password = "sql-299792458", database = "payroll")
    cursor = database.cursor()
    cursor.execute("SELECT DISTINCT salary.id, salary.gross_salary FROM employees INNER JOIN salary ON employees.id = salary.emp_id")
    records = cursor.fetchall()
    for record in records:
        cursor.execute(f"UPDATE salary SET deductions = {int(income_tax(record[1])) + 4000} WHERE id = {record[0]}")
        
    database.commit()
    
except Exception as e:
    print(e)