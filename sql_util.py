import pyodbc

connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=KHBW001;'
                      'Database=tempdb;'
                      'Trusted_Connection=yes;')

cursor = connection.cursor()
cursor.execute(
    "CREATE TABLE NewTestPyTable(Symbol varchar(15), Shares integer, Price integer)")  # creates new table
params = [('ETH', 55, 199),
          ('KHC', 66, 33)]
# insert two records into new table
cursor.executemany(
    "INSERT INTO tempdb.dbo.NewTestPyTable (Symbol, Shares, Price) VALUES (?, ?, ?)", params)

connection.commit()