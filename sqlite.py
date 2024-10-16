import sqlite3

# Connect to sqlite
connection = sqlite3.connect("student.db")

# Create cursor object to insert ,record, create tabel
cursor= connection.cursor() ## responsible for going through all record.

# Create table
table_info="""
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

# insert some more records
cursor.execute('''insert into STUDENT values('Krish','Data Science','A',89)''')
cursor.execute('''insert into STUDENT values('Sudhansu','Data Science','B',67)''')
cursor.execute('''insert into STUDENT values('Darious','Data Science','A',89)''')
cursor.execute('''insert into STUDENT values('Vikash','Devops','A',34)''')
cursor.execute('''insert into STUDENT values('Deepesh','Devops','A',56)''')

## Display all the records
print("The insrted records are:")
data= cursor.execute('''select * from STUDENT''')
for row in data:
    print(row)

# commit your changes in database
connection.commit()
connection.close()
