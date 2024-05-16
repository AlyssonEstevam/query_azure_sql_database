import pyodbc
import os
import json

abs_path = os.path.dirname(__file__)

with open(abs_path + '\\enviroment.json') as file:
    variables = json.load(file)

server = variables['server']
database = variables['database']
username = variables['username']
password = variables['password']
driver = variables['driver']

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        row = cursor.fetchone()
        while row:
            print(str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()
