from models.base import BaseDatabaseConnector


class Category(BaseDatabaseConnector):
    def __init__(self, name: str):
        self.obj = super()._select_one(
            """
            SELECT * FROM categories WHERE name = ?
            """,
            (name,),
        )
        self.id = self.obj["id"] if self.obj else None
        self.name = name

    def save(self):
        if self.id:
            super()._update(
                """
                    UPDATE categories
                    SET name = ? WHERE id = ?
                """,
                (self.name, self.id),
            )
        else:
            super()._insert(
                """
                    INSERT INTO categories (name)
                    VALUES (?)
                """,
                (self.name,),
            )

    def delete(self):
        super()._delete(
            "DELETE FROM categories WHERE name = ?",
            (self.name,),
        )

    @property
    def books(self):
        books = self._select_all(
            "SELECT * FROM books WHERE category_id = ?",
            (self.id,),
        )
        return [r["name"] for r in books]
