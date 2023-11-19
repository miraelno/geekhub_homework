import sqlite3
 
class ConnectionDB:
 
    def __init__(self):
        self.db_name = 'ATM_DB.db'
    
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_val:
            raise