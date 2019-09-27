import MySQLdb

conn=MySQLdb.connect(host='localhost',user='root',passwd='')

cursor = conn.cursor()

cursor.execute('Create database Library')

cursor.execute('use Library')

# Create table
table='create table books(book_accno char(30) primary key, book_name ' \
      'char(50),no_of_copies int(5),price int(5))'
cursor.execute(table)

# Insert
cursor.execute('insert books values (%s,%s,%s,%s)',('Py9098','Programming With Python',100,50))
cursor.execute('insert books values (%s,%s,%s,%s)',('Py9099','Programming With Python',100,50))

# Select
cursor.execute('select * from books')
cursor.fetchall()

# Update
cursor.execute('update books set price=%s where no_of_copies<=%s',[60,101])

# Delete
cursor.execute('delete from books where no_of_copies<=%s',[101])

conn.close()
