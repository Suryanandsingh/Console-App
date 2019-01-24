import sqlite3 as sq

db_name = 'database.db'

def run_query(query, parameters=()):
	with sq.connect(db_name) as conn:
		c = conn.cursor()
		query_re = c.execute(query, parameters)
		conn.commit()
	return query_re


def create_database():
	query = 'CREATE TABLE User(email TEXT PRIMARY KEY NOT NULL,Username TEXT NOT NULL,password TEXT NOT NULL)'
	run_query(query)


"""
	Below command uncomment when you will create database
"""

# if __name__ == '__main__':
# 	create_database()
