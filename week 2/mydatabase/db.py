import sqlite3
from user import User 


connection = sqlite3.connect('my_database.db')  

cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

def insert_query(b):
    insert_query = 'INSERT INTO users (name, age, email) VALUES (?, ?, ?)'
    cursor.execute(insert_query, (b.name, b.age, b.email))

    connection.commit()
    return True

user = User("chaitanya", 22, "gmail",1)
def recieve_data():
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    users = []
    for row in rows:
        user = User(row[1],row[2],row[3])  
        users.append(user)
    return users
def close():
    cursor.close()
    connection.close()