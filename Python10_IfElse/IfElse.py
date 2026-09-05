# ============ if else ===============

# correct email - kushagra@example.com
# correct password - pass123
email = input("Enter your Email : ")
if '@' in email:
    password = input("Enter your Password : ")
    if email == "kushagra@example.com" and password == "pass123":
        print("Welcome!!")
    else:
        print("Wrong Credentials")
else:
    print("Email is wrong Give correct email")

# give user a second chance 
if email == "kushagra@example.com" and password == "pass123":
    print("Welcome!!")
elif email == "kushagra@example.com" and password != "pass123":
    print("Password incorrect")
    password = input("Enter password again : ")
    if password == "pass123":
        print("Finally Correct!! Welcome")
    else:
        print("Still incorrect")
else:
    print("Wrong Credentials")