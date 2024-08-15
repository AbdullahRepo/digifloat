import pyodbc

cnxn_str = (
    r'ODBC Driver 18 for SQL Server};'
    r'Server=tcp:server-ha-ya.database.windows.net,1433;'
    r'Database=database-ha-ya;'
    r'Uid=UserID-ha-ya;'
    r'Pwd=P@ssword-ha-ya'
)

conn = pyodbc.connect(cnxn_str)
print("Connection successful")

#this can be considered as the change in the repo


