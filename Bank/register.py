from connection import databaseConnection

def register(username, password, email, initial_deposit=0):
    db = databaseConnection()
    cursor = db.cursor()

    cursor.execute("SELECT acc_no FROM account WHERE email=%s", (email,))
    if cursor.fetchone():
        return "Email already exists"

    cursor.execute(
        "INSERT INTO account(username,password,balance,email) VALUES(%s,%s,%s,%s)",
        (username, password, initial_deposit, email)
    )
    db.commit()

    cursor.execute("SELECT acc_no FROM account WHERE email=%s", (email,))
    acc_no = cursor.fetchone()[0]

    cursor.close()
    db.close()

    return f"Account created successfully. Account Number: {acc_no}"
