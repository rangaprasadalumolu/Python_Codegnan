from withdraw import Withdraw
from deposit import Deposit
from connection import databaseConnection

def Transfer(from_acc, to_acc, amount):
    db = databaseConnection()
    cursor = db.cursor()

    cursor.execute("SELECT acc_no FROM account WHERE acc_no=%s", (to_acc,))
    if not cursor.fetchone():
        cursor.close()
        db.close()
        return "Receiver account not found"

    cursor.close()
    db.close()

    res = Withdraw(from_acc, amount)
    if "successful" in res:
        Deposit(to_acc, amount)
    return res
