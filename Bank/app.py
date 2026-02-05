from login import login
from register import register
from balance import Balance
from withdraw import Withdraw
from deposit import Deposit
from transfer import Transfer
from ministatement import Ministatement

print("Welcome to Online Banking")

choice = int(input("1. Login\n2. Register\nEnter choice: "))

if choice == 2:
    u = input("Username: ")
    p = input("Password: ")
    e = input("Email: ")
    amt = int(input("Initial deposit: "))
    print(register(u, p, e, amt))

elif choice == 1:
    acc = int(input("Account Number: "))
    pwd = input("Password: ")

    if login(acc, pwd):
        while True:
            print("\n1.Balance 2.Withdraw 3.Deposit 4.Transfer 5.MiniStatement 6.Logout")
            ch = int(input("Choice: "))

            if ch == 1:
                print(Balance(acc))
            elif ch == 2:
                print(Withdraw(acc, int(input("Amount: "))))
            elif ch == 3:
                print(Deposit(acc, int(input("Amount: "))))
            elif ch == 4:
                to = int(input("To Account: "))
                amt = int(input("Amount: "))
                print(Transfer(acc, to, amt))
            elif ch == 5:
                print(Ministatement(acc))
            elif ch == 6:
                print("Logged out")
                break
            else:
                print("Invalid option")
    else:
        print("Invalid login")
