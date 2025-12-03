# Deposit Function
from accounts import users_table
def deposit(account:int,deposit_amount:int):
    print("Deposit Page")
    amount = users_table[account][0]
        # Checking amount is sufficient or not
    if account in users_table:
        if deposit_amount > 0:
            # Updating value in the table
            users_table[account][0] += deposit_amount
            print(f'{deposit_amount} deposited successful \
                  current balance is {users_table[account][0]}')
        else:
            print("Insufficient Balance")
    else:
        print("User Not Found")