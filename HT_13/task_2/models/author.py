from models.base import BaseDatabaseConnector


class Author(BaseDatabaseConnector):
    def __init__(self, name: str):
        self.obj = super()._select_one(
            """
                SELECT * FROM authors WHERE name = ?
            """,
            (name,),
        )
        self.id = self.obj["id"] if self.obj else None
        self.name = name

    def save(self):
        if self.id:
            super()._update(
                """
                    UPDATE authors
                    SET name = ? WHERE id = ?
                """,
                (self.name, self.id),
            )
        else:
            super()._insert(
                """
                    INSERT INTO authors (name)
                    VALUES (?)
                """,
                (self.name,),
            )

    def delete(self):
        super()._delete(
            "DELETE FROM authors WHERE name = ?",
            (self.name,),
        )
