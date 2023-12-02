# 2. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки (включіть фантазію).
# Наприклад вона може містити класи Person, Teacher, Student, Book, Shelf, Author, Category і.т.д.

from models.category import Category
from models.student import Student
from models.book import Book
from models.base import BaseDatabaseConnector


class Library(BaseDatabaseConnector):
    @property
    def all_books(self):
        books = super()._select_all("SELECT * FROM books", ())
        return {book["name"]: book["id"] for book in books}
    
    def define_student(self):
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
        
        return student
    
    def show_all_books(self):
        [print(book) for book in self.all_books]

    def add_book_to_student(self, student : Student):
        {print(f'{book[1]} -> {book[0]}') for book in self.all_books.items()}

        selected_book_id = input("Select book number: ").strip()
        book = Book.get_book_by_id(selected_book_id)
        student.add_book(book['id'])
        print(f'The book {book["name"]} is taken.')

    def show_taken_books(self, student: Student):
        taken_books = student.taken_books

        for i in taken_books:
            [print(f'{i[0]} -> {i[1]}') for i in i.items()]

    def interactive_menu(self):
        student = self.define_student()
        
        while True:
            menu_option = input(
                "1 - Show books\n2 - Take book\n3 - My books\n4 - Exit\n"
            ).strip()

            match menu_option:
                case "1":
                    self.show_all_books()

                case "2":
                    self.add_book_to_student(student)

                case "3":
                    self.show_taken_books(student)

                case "4":
                    exit()
                    
                case _:
                    print("No such option. Try again.")


lib = Library()
lib.interactive_menu()
