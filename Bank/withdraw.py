from connection import databaseConnection

def Withdraw(acc_no, amount):
    db = databaseConnection()
    cursor = db.cursor()

    cursor.execute("SELECT balance FROM account WHERE acc_no=%s", (acc_no,))
    balance = cursor.fetchone()[0]

    if balance < amount:
        cursor.close()
        db.close()
        return "Insufficient funds"

    new_balance = balance - amount

    cursor.execute(
        "UPDATE account SET balance=%s WHERE acc_no=%s",
        (new_balance, acc_no)
    )

    cursor.execute(
        "INSERT INTO transactions(acc_no,type_of_transaction,trans_amount) VALUES(%s,'debit',%s)",
        (acc_no, amount)
    )

    db.commit()
    cursor.close()
    db.close()

    return f"Withdrawal successful. Balance: {new_balance}"
