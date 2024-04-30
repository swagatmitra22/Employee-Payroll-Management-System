import random
import mysql.connector

ranges = {"Finance Officer" : (50, 75), "Engg Service Head" : (60, 80), "Assistant Manager Prod" : (40, 60),
        "Purchase officer" : (40, 55), "Head Technical" : (85, 105), "Stores Officer" : (40, 60),
        "I&M Shift Engineer" : (30, 45), "E&M Shift Engineer" : (30, 45), "Sr Officer Technical" : (70, 80),
        "M&U Maint Section Head" : (80, 100), "Safety Head" : (40, 55), "E&M Section Head" : (45, 60),
        "IT Officer" : (70, 85), "OMI Shift Prod Officer" : (60, 80), "OMI Prod Head": (85, 100), "Head of Security": (0, 5),
        "Service Shift Engineer": (30, 45), "CEO": (0, 0)}

try:
    database = mysql.connector.connect(host = "localhost", user = "root", password = "sql-299792458", database = "payroll")
    cursor = database.cursor()
    cursor.execute("SELECT salary.id AS id, employees.designation, employees.joining_date, salary.`year` FROM employees INNER JOIN salary ON employees.id = salary.emp_id")
    records = cursor.fetchall()
    for record in records:
            ratio = min(10, record[3] - record[2].year) / 10
            salary = int(((((ranges[record[1]][1]) - ranges[record[1]][0]) * ratio + ranges[record[1]][0]) // 5) * 5000)
            cursor.execute(f"UPDATE salary SET basic_salary = {salary} WHERE id = {record[0]}")
        
    database.commit()
    
except Exception as e:
    print(e)