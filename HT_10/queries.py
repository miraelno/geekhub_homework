SELECT_USER = "SELECT * FROM users WHERE name = ? AND password = ?"
ADD_USER = "INSERT INTO users (name, password) VALUES (?, ?)"
GET_USER_BALANCE = "SELECT balance FROM users WHERE id = ?"
UPDATE_USER_BALANCE = "UPDATE users SET balance = ? WHERE id = ?"
ADD_TRANSACTION = "INSERT INTO transactions (datetime, amount, description, user_id) VALUES (?, ?, ?, ?)"