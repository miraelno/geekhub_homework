import sqlite3

con = sqlite3.connect("ATM_DB.db")
cur = con.cursor()

# cur.execute('CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), password VARCHAR(255), balance DOUBLE)')
# cur.execute('CREATE TABLE transactions(id INTEGER PRIMARY KEY AUTOINCREMENT, datetime DATETIME, amount DOUBLE, description VARCHAR(255), user_id INTEGER, FOREIGN KEY(user_id) REFERENCES users(id))')

cur.execute(
    "INSERT INTO users (name, password, balance) VALUES ('JohnDoe', 'password123', 1000.00), ('AliceSmith', 'securePass456', 500.50), ('BobJohnson', 'test123', 1200.75)"
)

cur.execute(
    "INSERT INTO transactions (datetime, amount, description, user_id) VALUES ('2023-11-17 08:30:00', 50.00, 'Grocery shopping', 1), ('2023-11-17 12:15:00', -20.50, 'Lunch with friends', 2), ('2023-11-18 09:45:00', 100.75, 'Deposit', 3), ('2023-11-19 15:20:00', -30.25, 'Movie tickets', 1)"
)


con.commit()
