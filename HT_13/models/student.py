from models.base import BaseDatabaseConnector
from models.book import Book


class Student(BaseDatabaseConnector):
    def __init__(self, first_name: str, last_name: str, class_name: str):
        self.obj = super()._select_one(
            """
                SELECT * FROM students
                WHERE first_name = ? AND last_name = ?
            """,
            (first_name, last_name),
        )
        self.id = self.obj["id"] if self.obj else None
        self.first_name = first_name
        self.last_name = last_name
        self.class_name = class_name

    def save(self):
        if self.id:
            super()._update(
                """
                    UPDATE students
                    SET first_name = ?, last_name = ?, class_name = ?
                    WHERE id = ?
                """,
                (self.first_name, self.last_name, self.class_name, self.id),
            )
        else:
            super()._insert(
                """
                    INSERT INTO students (first_name, last_name, class_name)
                    VALUES (?, ?, ?)
                """,
                (self.first_name, self.last_name, self.class_name),
            )

    def add_book(self, book_id: int):
        super()._insert(
            """
                    INSERT INTO books_to_students (student_id, book_id)
                    VALUES (?, ?)
                """,
            (self.id, book_id),
        )

    @property
    def taken_books(self):
        books = self._select_all(
            """
                SELECT books.name AS book_name, authors.name AS author_name
                FROM books
                JOIN books_to_students
                ON books.id = books_to_students.book_id
                JOIN authors
                ON books.author_id = authors.id
                WHERE books_to_students.student_id = ?
            """,
            (self.id,),
        )
        return [{r["book_name"]: r["author_name"]} for r in books]
