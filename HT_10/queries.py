SELECT_ALL_NOMINALS = "SELECT * FROM banknotes"
SELECT_MINIMUM_NOMINAL = "SELECT min(nominal) as min_nominal FROM banknotes"
SELECT_TOTAL_BALANCE = "SELECT sum(nominal * amount) AS balance FROM banknotes"
SELECT_USER = "SELECT * FROM users WHERE name = ? AND password = ?"
SELECT_USER_BALANCE = "SELECT balance FROM users WHERE id = ?"

ADD_TRANSACTION = "INSERT INTO transactions (datetime, amount, description, user_id) VALUES (?, ?, ?, ?)"
ADD_USER = "INSERT INTO users (name, password) VALUES (?, ?)"

UPDATE_NOMINAL_AMOUNT = "UPDATE banknotes SET amount = ? WHERE nominal = ?"
UPDATE_USER_BALANCE = "UPDATE users SET balance = ? WHERE id = ?"
