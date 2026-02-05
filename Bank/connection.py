import mysql.connector as SQLC

def databaseConnection():
    return SQLC.connect(
        host="localhost",
        user="root",
        password="root",
        database="bank_db"
    )



#cursor object creation
#cursor=database_config.cursor()


# accounts_table_query="""create table if not exists account(acc_no bigint primary key auto_increment, 
# username varchar(100) not null, 
# password varchar(100) not null, 
# balance float, 
# email varchar(100) not null unique);"""


# cursor.execute(accounts_table_query)
# print('Table Created')


#transaction_table_query="""create table if not exists transaction(transaction_id  bigint primary key auto_increment, 
#acc_no bigint not null, 
#type_of_transaction enum('deposit','credit'), 
#trans_amount float not null, 
#foreign key (acc_no) references account(acc_no));"""

#cursor.execute(transaction_table_query)
#print('Table Created')

# inserting data into accounts table
#insert_data_query="""insert into account(username, password, balance, email)
#                       values(%s, %s, %s, %s);"""
#cursor.execute(insert_data_query, ('ramesh','4567', 2000,'ramesh@gmail.com'))
#database_config.commit()
#print("Data inserted sucessfully")

#cursor.execute("select * from account;")
#records=cursor.fetchall()
#print(records)

