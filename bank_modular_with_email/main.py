
import accounts
from login import login
from withdraw import withdraw
from deposit import deposit
from transfer import transfer
from ministatement import ministatement
from balance_enquiry import balance_enquiry
from email_module import singleEmailSender
import logout



# main
if __name__ == "__main__":
    print("Welcome to the Codegnan Bank Application")
    username = int(input("Enter Your Account Number:"))
    password = int(input("Enter Your Password:"))
    login_val = login(username = username,password=password)
    while login_val:
        operations = ("\n 1.Withdraw \n", "2.Deposit \n", "3.Transfer \n",
                      "4.Mini Statement \n", "5.Balance Enquiry \n", "6.Logout \n")
        print(*operations) #*removes () tuple symbol
        choice = int(input("Select your Operation:"))
        user_email = accounts.users_table[username][2]
        if choice == 1:
            amount=int(input("Enter your withdraw amount:"))
            withdraw(account= username,withdraw_amount=amount)
            singleEmailSender(
                to_email=user_email,
                subject="Withdraw Alert",
                body=f"You have withdrawn Rs.{amount} from account {username}."
            )
        elif choice == 2:
            amount=int(input("Enter your deposit amount:"))
            deposit(account=username,deposit_amount=amount)
            singleEmailSender(
                to_email=user_email,
                subject="Deposit Alert",
                body=f"You have deposited Rs.{amount} into account {username}."
            )
        elif choice==3:
            accounts=int(input("Enter receivers account:"))
            amount=int(input("Enter the transfer amount:"))
            transfer(sender=username,receiver=accounts,transfer_amount=amount)
            singleEmailSender(
                to_email=user_email,
                subject="Transfer Alert",
                body=f"You have transferred Rs.{amount} to account {accounts}."
            )
            if accounts in accounts.users_table:
                receiver_email = accounts.users_table[accounts][2]
                singleEmailSender(
                    to_email=receiver_email,
                    subject="Transfer Received",
                    body=f"You have received Rs.{amount} from account {username}."
                )
        elif choice == 4:
            ministatement(account=username)
            singleEmailSender(
                to_email=user_email,
                subject="Mini Statement",
                body=f"Mini statement requested for account {username}."
            )
        elif choice == 5:
            balance_enquiry(account=username) 
            singleEmailSender(
                to_email=user_email,
                subject="Balance Enquiry",
                body=f"Balance enquiry for account {username}."
            )   
        elif choice == 6:
            singleEmailSender(
                to_email=user_email,
                subject="Logout Notification",
                body=f"You have logged out from account {username}."
            )
            logout.logout("Logged out Successfully")
            exit()
        else:
            print("Select Your option Between 1 to 5")