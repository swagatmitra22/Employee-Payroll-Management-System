import random
import mysql.connector

try:
    database = mysql.connector.connect(host = "localhost", user = "root", password = "sql-299792458", database = "payroll")
    cursor = database.cursor()
    cursor.execute("SELECT id, working_days, total_days, overtime FROM salary")
    records = cursor.fetchall()
    for record in records:
            perf_metric = (random.randint(0, 10) / 10) * 2500
            bonus = ((5556) * float(record[1])) / float(record[2]) + (float(record[3])/2) + perf_metric
            cursor.execute(f"UPDATE salary SET bonus = {int(bonus)} WHERE id = {record[0]}")
        
    database.commit()
    
except Exception as e:
    print(e)