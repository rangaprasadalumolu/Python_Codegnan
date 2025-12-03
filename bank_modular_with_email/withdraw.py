from accounts import users_table
def withdraw(account:int,withdraw_amount:int):
    print("Withdraw Page")
    # Check for account in users table
    if account in users_table:
        amount = users_table[account][0]
        # Checking amount is sufficient or not
        if amount >= withdraw_amount:
            # Updating value in the table
            users_table[account][0] -= withdraw_amount
            print(f'{withdraw_amount} withdraw successful \
                  current balance is {users_table[account][0]}')
            print()
        else:
            print("Insufficient Balance")
    else:
        print("User Not Found")