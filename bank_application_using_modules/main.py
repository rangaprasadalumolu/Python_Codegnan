# main.py

from operations import login, withdraw, deposit, transfer, ministatement, balanceEnquiry, logout

print("======== Welcome to People's Bank Application ========")

username = int(input("Enter your account number: "))
password = int(input("Enter your password: "))

login_val = login(username, password)

while login_val:
    print("\nSelect an Operation:")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Transfer")
    print("4. Mini-Statement")
    print("5. Balance Enquiry")
    print("6. Logout")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        amt = int(input("Enter amount to withdraw: "))
        withdraw(username, amt)
    elif choice == 2:
        amt = int(input("Enter amount to deposit: "))
        deposit(username, amt)
    elif choice == 3:
        acc = int(input("Enter receiver account no: "))
        amt = int(input("Enter transfer amount: "))
        transfer(username, acc, amt)
    elif choice == 4:
        ministatement(username)
    elif choice == 5:
        balanceEnquiry(username)
    elif choice == 6:
        logout()
    else:
        print("Please enter a valid operation (1-6).")
