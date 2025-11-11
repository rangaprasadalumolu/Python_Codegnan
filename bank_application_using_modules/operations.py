# operations.py

from accounts import account_table, users_table

def login(username: int, password: int):
    if username in account_table:
        if password == account_table[username]:
            print("Login Successful!")
            print(f"Welcome, {users_table[username][1]}!")
            return True
        else:
            print("\nIncorrect password. Please try again.")
            return False
    else:
        print("Account not found")
        return False

def withdraw(account: int, withdraw_amount: int):
    print("\n--- Withdraw Page ---")
    if withdraw_amount <= 0:
        print("Enter a valid amount.")
    elif withdraw_amount > users_table[account][0]:
        print("Insufficient balance.")
    else:
        users_table[account][0] -= withdraw_amount
        print(f"{withdraw_amount} withdrawn successfully.")
        print(f"Remaining balance: {users_table[account][0]}")

def deposit(account: int, deposited_amount: int):
    print("\n--- Deposit Page ---")
    if deposited_amount <= 0:
        print("Enter a valid amount.")
    else:
        users_table[account][0] += deposited_amount
        print(f"{deposited_amount} deposited successfully.")
        print(f"New balance: {users_table[account][0]}")

def transfer(sender: int, receiver: int, transfer_amount: int):
    print("\n--- Transfer Page ---")
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

def ministatement(account: int):
    print("\n--- Mini Statement ---")
    if account in users_table:
        print(f"Name : {users_table[account][1]}")
        print(f"Email: {users_table[account][2]}")
        print("Mini statement page under development.")
    else:
        print("Account not found.")

def balanceEnquiry(account: int):
    if account in users_table:
        print(f"Current Balance: {users_table[account][0]}")
    else:
        print("User not found")

def logout():
    print("\nLogout Successful. Thank you for using People's Bank!")
    exit()
