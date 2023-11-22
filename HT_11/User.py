from db_connection import ConnectionDB

from queries import SELECT_USER_BALANCE

class User:

    def __init__(self, id, name, password, balance, isCollector):
        self.id = id
        self.name = name
        self.password = password
        self.balance = balance
        self.isCollector = isCollector


    def get_balance_from_db(self):
        with ConnectionDB() as con:
            cur = con.cursor()
            query_result = cur.execute(SELECT_USER_BALANCE, (self.id, ))
            row = query_result.fetchone()

        return row["balance"]
    

    @property
    def balance(self):
        self._balance = self.get_balance_from_db()
        return self._balance


    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance