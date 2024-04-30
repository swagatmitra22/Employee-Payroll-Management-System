import random
import mysql.connector

try:
    database = mysql.connector.connect(host = "localhost", user = "root", password = "sql-299792458", database = "payroll")
    cursor = database.cursor()
    cursor.execute("SELECT id, basic_salary FROM salary")
    records = cursor.fetchall()
    for record in records:
            conv = (record[1] * 3) / 100
            pf = (record[1] * 12) / 100
            cursor.execute(f"UPDATE salary SET provident_fund = {pf}, convenience_exp = {conv} WHERE id = {record[0]}")
        
    database.commit()
    
except Exception as e:
    print(e)