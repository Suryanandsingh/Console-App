from database import run_query
from Login import login
from Signup import signup

print("1 for login")
print("2 for signup")
print("3 for exit")

while True:

	switchs = eval(input('Enter your choices '))

	if switchs == 1:
		print("Welcome To Login\n")
		login()
		
	elif switchs == 2:
		print("Welcome To Signup\n")
		signup()
	
	else:
		print("\nBye")
		break