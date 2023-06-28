from mysql import connector

connection = connector.connect(
  host = "127.0.0.1",
  user = "root",
  password = ""
)

print(connection)

cursor = connection.cursor();
cursor.execute("show databases")

print("---Databases---")
for db in cursor:
  print(db)

cursor.execute("use test")
cursor.execute("show tables")
print("---Tables in Test---")
for table in cursor:
  print(table)
# cursor.execute('create table pythonStudents (id int,name text,course text)')

def insertData():
  cursor.execute("insert into pythonstudents values(1, 'name', 'bsc')")
  connection.commit()

# insertData()

print("---Test Data---")
cursor.execute("select * from pythonstudents")
data = cursor.fetchall()

for row in data:
  print(row)

# or

for row in cursor:
  print(row)

cursor.close()
connection.close()