import pypyodbc

connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=sql.steemsql.com;'
                              'Database=DBSteem;'
                              'uid=steemit;pwd=steemit')
cursor = connection.cursor() 



SQLCommand = ("select name,voting_power from Accounts where name='firedream'")


              

cursor.execute(SQLCommand)
print (cursor.fetchall())
connection.close()
