from accounts import accounts_table
def login(username:int,password:int):
    print("Loginpage")
    # Checking if account number exists
    if username in accounts_table:
        if password == accounts_table[username]:
            print("Login Successful")
            return True
        else:
            print("Invalid Password")
            return False
    else:
        print("User Not Found")
        return False