
import sqlite3
db=sqlite3.connect("lambton.db")
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS USERS(FirstName text,LastName text,Phone text,Email text,Question text,Answer text, password text,cpassword text);''')
db.commit()
print('Table created successfully')
db.close()



