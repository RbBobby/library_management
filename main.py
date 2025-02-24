from library import Library
from book import Book

def main():
    library = Library()

    # Добавляем книги в библиотеку
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))

    print("Available books in the library:")
    library.display_books()

    # Проверка на выдачу книги
    library.borrow_book("1984")
    library.borrow_book("The Great Gatsby")

    print("\nAvailable books after borrowing:")
    library.display_books()

    # Проверка на возврат книги
    library.return_book("1984")
    
    print("\nAvailable books after returning:")
    library.display_books()

if __name__ == "__main__":
    main()
