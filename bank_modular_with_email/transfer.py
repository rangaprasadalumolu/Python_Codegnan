# Transfer Function
from accounts import users_table
def transfer(sender:int,receiver:int,transfer_amount:int):
    # checking accounts in users_table
    if sender in users_table:
        if receiver in users_table:
            amount = users_table[sender][0]
            if amount >= transfer_amount:
                users_table[sender][0] -= transfer_amount
                users_table[receiver][0] += transfer_amount
                print(f'{transfer_amount} Transfer Sucessfull\
                    Current Balance is : {users_table[sender][0]}')
            else:
                print("Insufficient Amount in your account")
        else:
            print("Reciever account not found")
    else:
        ("User Not Found")