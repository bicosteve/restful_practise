import sqlite3

# initialize connection
connection = sqlite3.connect('test.db')


cursor = connection.cursor()


create_users_table = 'CREATE TABLE users(id integer primary key autoincrement,username text, password text)'
cursor.execute(create_users_table)

create_items_table = 'CREATE TABLE items(id integer primary key autoincrement,name text,price text)'
cursor.execute(create_items_table)

connection.close()
