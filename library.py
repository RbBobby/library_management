from book import Book

class Library:
    def __init__(self):
        self.books = []  # Список книг в библиотеке

    def add_book(self, book):
        self.books.append(book)  # Добавляем книгу в библиотеку

    def display_books(self):
        for book in self.books:
            print(book)  # Отображаем список книг

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False  # Устанавливаем статус книги как недоступный
                print(f"You have borrowed '{book.title}'")
                return
        print(f"'{title}' is not available for borrowing.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_available:
                book.is_available = True  # Устанавливаем статус книги как доступный
                print(f"You have returned '{book.title}'")
                return
        print(f"'{title}' was not borrowed.")
