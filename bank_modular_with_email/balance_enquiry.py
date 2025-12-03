# Balance Enquiry function
from accounts import users_table
def balance_enquiry(account:int):
    if account in users_table:
        print(f"Current Balance is:{users_table[account][0]}")
    else:
        print("User Not Found")