from library import Library
from book import Book

def main():
    book_1984 = Book("1984", "George Orll")
    book_1984 = Book("1984", "George Orwell")
    book_to_kill_a_mockingbird = Book("To Kill a Mockingbird", "Harper Lee")
    book_the_great_gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book_war_and_peace = Book("War and Peace", "Leo Tolstoy")
    # Создаем библиотеку с начальными книгами
    library_1 = Library([book_1984, book_to_kill_a_mockingbird, book_the_great_gatsby])
    #library_2 = Library()

    # Добавляем книги в библиотеку
    library_1.add_book(Book("1984", "George Orwell"))
    library_1.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library_1.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library_1.add_book(book_war_and_peace)

    print("Available books in the library:")
    library_1.display_books()

    # Проверка на выдачу книги
    library_1.borrow_book("1984")
    library_1.borrow_book("The Great Gatsby")

    print("\nAvailable books after borrowing:")
    library_1.display_books()

    # Проверка на возврат книги
    library_1.return_book("1984")
    
    print("\nAvailable books after returning:")
    library_1.display_books()

if __name__ == "__main__":
    main()
