from database import run_query
import getpass


def login():
	email = input("Enter your email: ")
	password = getpass.getpass()

	query = "SELECT * FROM User WHERE email="+"'"+email+"' AND password="+"'"+password+"' " 

	item = run_query(query)
	for i in item:
		y_N = input("You have been login successfully.\nDo you want to delete info (y/N) ? ")
		if(y_N == 'y'):
			query = "DELETE FROM User WHERE email="+"'"+email+"' AND password="+"'"+password+"' "
			if run_query(query):
				print("\nDeletion successfully\n.")
		break
	else:
		print("\nPlease check your email or password\n")
	