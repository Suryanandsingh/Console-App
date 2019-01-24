import re, getpass
from database import run_query

def signup():
	user = mail =  0
	Username = email = password = ''
	while True:
		if user == 0:
			Username = input("Enter Your Username: ")
			if re.match("^[a-zA-Z0-9_]{6,}$", Username):
				user = 1
				pass
			else:
				print('Wrong Username\n')
				continue
		if mail == 0:
			email = input("Enter Your Email: ")
			if re.match("^\w.+@[a-zA-Z]+?\.[a-zA-Z]{2,3}$", email):
				mail = 1
				pass
			else:
				print("Wrong email\n")
				continue
		else:
			print("Enter Your password ")
			password = getpass.getpass()
			if re.match('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
				again_password = getpass.getpass("Again password: ")
				if password == again_password:
					query = 'INSERT INTO User VALUES(?, ?, ?)'
					parameters = (email, Username, password)
					if run_query(query, parameters):
						print("\nRegistration has been Successfully")
						break
				else:
					print("Not match password\n")
					continue
			else:
				print('Wrong password\n')
				continue
