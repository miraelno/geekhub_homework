from db_connector import ConnectionDB

with ConnectionDB() as con:
    cur = con.cursor()
    # cur.execute("""
    #     CREATE TABLE students (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         first_name VARCHAR(255),
    #         last_name VARCHAR(255),
    #         class_name VARCHAR(20)
    #     )
    # """)
    # cur.execute("""
    #     CREATE TABLE categories (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         name VARCHAR(255)
    #     )
    # """)
    # cur.execute("""
    #     CREATE TABLE authors (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         name VARCHAR(255)
    #     )
    # """)
    # cur.execute("""
    #     CREATE TABLE books (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         name VARCHAR(255),
    #         category_id INTEGER,
    #         author_id INTEGER,
    #         FOREIGN KEY(category_id) REFERENCES categories(id),
    #         FOREIGN KEY(author_id) REFERENCES authors(id)
    #     )
    # """)

    cur.execute(
        """
        CREATE TABLE books_to_students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            book_id INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(id),
            FOREIGN KEY(book_id) REFERENCES books(id)
        )
    """
    )

    # cur.execute("""
    #     INSERT INTO students (first_name, last_name, class_name)
    #     VALUES
    #         ('John', 'Doe', 'Math101'),
    #         ('Jane', 'Smith', 'History101'),
    #         ('Bob', 'Johnson', 'English101')
    # """)

    # cur.execute("""
    #     INSERT INTO categories (name)
    #     VALUES
    #         ('Science'),
    #         ('History'),
    #         ('Fiction')
    # """)

    # cur.execute("""
    #     INSERT INTO authors (name)
    #     VALUES
    #         ('J.K. Rowling'),
    #         ('George Orwell'),
    #         ('Jane Austen')
    # """)

    # cur.execute("""
    #     INSERT INTO books (name, category_id, author_id)
    #     VALUES
    #         ('Harry Potter and the Philosopher''s Stone', 1, 1),
    #         ('1984', 3, 2),
    #         ('Pride and Prejudice', 3, 3)
    # """)

    cur.execute(
        """
        INSERT INTO books_to_students (student_id, book_id)
        VALUES
            (1, 2),
            (1, 1),
            (2, 3),
            (3, 3)
    """
    )

    con.commit()
