import sqlite3

con = sqlite3.connect("ATM_DB.db")
cur = con.cursor()

# cur.execute('CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), password VARCHAR(255), balance DOUBLE DEFAULT 0.00, isCollector BOOLEAN DEFAULT 0)')
# cur.execute('CREATE TABLE transactions(id INTEGER PRIMARY KEY AUTOINCREMENT, datetime DATETIME, amount FLOAT, description VARCHAR(255), user_id INTEGER, FOREIGN KEY(user_id) REFERENCES users(id))')
# cur.execute('CREATE TABLE banknotes(id INTEGER PRIMARY KEY AUTOINCREMENT, nominal INTEGER, amount INTEGER)')

# cur.execute(
#     "INSERT INTO users (name, password, balance, isCollector) VALUES ('JohnDoe', 'password123', 1000.00, 0), ('AliceSmith', 'securePass456', 500.50, 0), ('BobJohnson', 'test123', 1200.75, 0), ('admin', 'admin', 0, 1)"
# )
# cur.execute(
#     "INSERT INTO banknotes (nominal, amount) VALUES (10, 50), (20, 50), (50, 50), (100, 40), (200, 30), (500, 10), (1000, 10)"
# )

con.commit()
