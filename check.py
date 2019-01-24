import sqlite3

conn = sqlite3.connect('database.db')

#conn.execute("INSERT INTO User (email, Username, password) \
#      VALUES ('abc@gmail.com', 'surya','singh1234' )")

cursor = conn.execute("SELECT * from User")
for i in cursor:
	print(i)

conn.close()