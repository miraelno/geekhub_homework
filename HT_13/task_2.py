# 2. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки (включіть фантазію).
# Наприклад вона може містити класи Person, Teacher, Student, Book, Shelf, Author, Category і.т.д.

from models.category import Category
from models.student import Student
from models.book import Book
from models.base import BaseDatabaseConnector


class Library(BaseDatabaseConnector):
    def find_book():
        pass

    @property
    def all_books(self):
        books = super()._select_all("SELECT * FROM books", ())
        return {book["name"]: book["id"] for book in books}

    def interactive_menu(self):
        print(
            "Welcome to the library!\nEnter your first name, last name and class name."
        )
        user_input = input("Separate it with 1 space: ").strip().split()
        while True:
            if len(user_input) < 3:
                user_input = input("Invalid value. Try again: ").strip().split()
            else:
                break

        first_name, last_name, class_name = user_input
        student = Student(first_name, last_name, class_name)

        if student.id is None:
            print("Registration is completed!")
            student.save()

        while True:
            menu_option = input(
                "1 - Show book\n2 - Take book\n3 - My books\n4 - Exit\n"
            ).strip()

            match menu_option:
                case "1":
                    [print(book) for book in self.all_books]
                case "2":
                    [print(book) for book in self.all_books]
                    selected_book_name = input("Select book name: ").strip()
                    book = Book(selected_book_name)
                    print(book)

                case "3":
                    pass
                case "4":
                    exit()
                case _:
                    print("No such option. Try again.")


lib = Library()
lib.interactive_menu()
# c = Category('New test')
# # c.save()
# print(c.name)
# c.delete()
# print(c.name)
# books = c.books
# print(books)

# s = Student('John','Doe', 'Math101')
# print(s.taken_books)
# s2 = Student('New', 'Student', 'Test')
# s2.save()
# print(s2)
# print(s2.taken_books)
