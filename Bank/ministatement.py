from connection import databaseConnection

def Ministatement(acc_no):
    db = databaseConnection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM transactions 
        WHERE acc_no=%s 
        ORDER BY trans_time DESC 
        LIMIT 10
    """, (acc_no,))

    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data
