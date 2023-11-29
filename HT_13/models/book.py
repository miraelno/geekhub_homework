from models.author import Author
from models.category import Category
from models.base import BaseDatabaseConnector


class Book(BaseDatabaseConnector):
    def __init__(self, name: str, category: Category, author: Author):
        self.obj = super()._select_one(
            """
                SELECT * FROM books WHERE name = ?
            """,
            (name,),
        )
        self.id = self.obj["id"] if self.obj else None
        self.name = name
        self.category = category
        self.author = author

    def save(self):
        if self.id:
            super()._update(
                """
                UPDATE categories
                SET name = ?, category_id = ?, author_id = ?
                WHERE id = ?
            """,
                (self.name, self.category.id, self.author.id, self.id),
            )
        else:
            super()._insert(
                """
                    INSERT INTO books (name, category_id, author_id)
                    VALUES (?, ?, ?)
                """,
                (self.name, self.category.id, self.author.id),
            )
