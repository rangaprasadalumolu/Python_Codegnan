## creating table
#accounts_table={ account: password}
#users_table={account: [amount,name,email]}

account_table={12345:1357,
               67890:2468}

users_table={12345:[1000,'Prasad','prasad@gmail.com'],
             67890:[500,'Chintu','chintu7@gmail.com']}

#functions
#login function
def login(username:int, password:int):
    #checking the account number is exists in accounts table or not
    if username in account_table:
        #checking the password
        if password == account_table[username]:
            print("Login Successful!")
            print(f"Welcome, {users_table[username][1]}!")
            return True
        else:
            print("\n Incorrect password. Please try again.")
            return False
    else:
        print("Account not found")
        return False

#withdraw function
def withdraw(account:int, withdraw_amount:int):
    print("\n--- Withdraw page ---")
    if withdraw_amount <= 0:
        print("Enter a valid amount.")
    elif withdraw_amount > users_table[account][0]:
        print("Insufficient balance.")
    else:
        users_table[account][0] -= withdraw_amount
        print(f"{withdraw_amount} withdrawn successfully.")
        print(f"Remaining balance: {users_table[account][0]}")
#deposit function
def deposit(account:int, deposited_amount:int):
    print("\n--- Deposit page ---")
    if deposited_amount <= 0:
        print("Enter a valid amount.")
    else:
        users_table[account][0] += deposited_amount
        print(f"{deposited_amount} deposited successfully.")
        print(f"New balance: {users_table[account][0]}")
#Transfer function
def transfer(sender:int, receiver:int, transfer_amount:int):
    print("\n--- Transfer page ---")
    if sender not in users_table:
        print("Sender account not found.")
    elif receiver not in users_table:
        print("Receiver account not found.")
    elif transfer_amount <= 0:
        print("Enter a valid amount.")
    elif users_table[sender][0] < transfer_amount:
        print("Insufficient funds to transfer.")
    else:
        users_table[sender][0] -= transfer_amount
        users_table[receiver][0] += transfer_amount
        print(f"{transfer_amount} transferred successfully to account {receiver}.")
        print(f"Your Current Balance: {users_table[sender][0]}")
#ministatement function
def ministatement(account:int):
    print("\n--- Mini Statement ---")
    if account in users_table:
        print(f"Name : {users_table[account][1]}")
        print(f"Email: {users_table[account][2]}")
        print("Mini statement page under development.")
    else:
        print("Account not found.")
#balance enquiry 
def balanceEnquiry(account:int):
    if account in users_table:
        print(f"Current Balance: {users_table[account][0]}")
    else:
        print("User not found")


#logout function
def logout():
    print("\n Logout Successful. Thank's for using People's Bank!")
    exit()

#main
if __name__=="__main__":

    print("========Welcome to People's Bank Appication========")
    username=int(input("Enter your account no:"))
    password=int(input("Enter the password:"))
    login_val=login(username,password)
    while login_val:
        print("\n Select an Operation:")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Transfer")
        print("4. Mini-Statement")
        print("5. Balance Enquiry")
        print("6. Logout")
        choice = int(input("Enter your choice (1-6): "))
        if choice==1:
            amt = int(input("Enter amount to withdraw: "))
            withdraw(account=username, withdraw_amount=amt)
        
        elif choice==2:
            amt = int(input("Enter amount to deposit: "))
            deposit(account=username, deposited_amount=amt)
        elif choice==3:
            acc=int(input("Enter receiver account no:"))
            amt=int(input("Enter transfer amount:"))
            transfer(sender=username, receiver=acc, transfer_amount=amt)
        elif choice==4:
            ministatement(account=username)
        elif choice==5:
            balanceEnquiry(account=username)
        elif choice==6:
            logout()
        else:
            print("Please enter a valid operation (1-6).")

