from connection import databaseConnection

def Balance(acc_no):
    db = databaseConnection()
    cursor = db.cursor()

    cursor.execute("SELECT balance FROM account WHERE acc_no=%s", (acc_no,))
    bal = cursor.fetchone()[0]

    cursor.close()
    db.close()
    return bal
