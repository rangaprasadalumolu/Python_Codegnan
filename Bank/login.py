from connection import databaseConnection

def login(acc_no, password):
    db = databaseConnection()
    cursor = db.cursor()

    cursor.execute("SELECT password FROM account WHERE acc_no=%s", (acc_no,))
    data = cursor.fetchone()

    cursor.close()
    db.close()

    if not data:
        return False
    return data[0] == password
