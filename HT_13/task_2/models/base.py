from db_connector import ConnectionDB


class BaseDatabaseConnector:
    @staticmethod
    def _select_one(query, params):
        with ConnectionDB() as con:
            cur = con.cursor()
            cur.execute(query, params)
            result = cur.fetchone()

        return result
    
    @staticmethod
    def _select_all(query, params):
        with ConnectionDB() as con:
            cur = con.cursor()
            cur.execute(query, params)
            result = cur.fetchall()

        return result
    
    @staticmethod
    def _insert(query, params):
        with ConnectionDB() as con:
            cur = con.cursor()
            cur.execute(query, params)
            con.commit()

    @staticmethod
    def _update(query, params):
        with ConnectionDB() as con:
            cur = con.cursor()
            cur.execute(query, params)
            con.commit()

    @staticmethod
    def _delete(query, params):
        with ConnectionDB() as con:
            cur = con.cursor()
            cur.execute(query, params)
            con.commit()
