from db_connector import ConnectionDB


class BaseDatabaseConnector:
    def _select_one(self, query, params):
        with ConnectionDB() as con:
            cur = con.cursor()
            cur.execute(query, params)
            result = cur.fetchone()

        return result

    def _select_all(self, query, params):
        with ConnectionDB() as con:
            cur = con.cursor()
            cur.execute(query, params)
            result = cur.fetchall()

        return result

    def _insert(self, query, params):
        with ConnectionDB() as con:
            cur = con.cursor()
            cur.execute(query, params)
            con.commit()

    def _update(self, query, params):
        with ConnectionDB() as con:
            cur = con.cursor()
            cur.execute(query, params)
            con.commit()

    def _delete(self, query, params):
        with ConnectionDB() as con:
            cur = con.cursor()
            cur.execute(query, params)
            con.commit()
