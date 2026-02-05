from connection import databaseConnection

def createTables():
    db = databaseConnection()
    cursor = db.cursor()

    account_table = """
    CREATE TABLE IF NOT EXISTS account(
        acc_no BIGINT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL,
        balance FLOAT DEFAULT 0,
        email VARCHAR(100) UNIQUE NOT NULL
    );
    """

    transaction_table = """
    CREATE TABLE IF NOT EXISTS transactions(
        transaction_id BIGINT PRIMARY KEY AUTO_INCREMENT,
        acc_no BIGINT NOT NULL,
        type_of_transaction ENUM('debit','credit'),
        trans_amount FLOAT NOT NULL,
        trans_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (acc_no) REFERENCES account(acc_no)
    );
    """

    cursor.execute(account_table)
    cursor.execute(transaction_table)

    db.commit()
    cursor.close()
    db.close()
