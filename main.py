from library import PublicLibrary, SchoolLibrary, DigitalLibrary
from book import Book


def main():
    book_1984 = Book("1984", "George Orwell")
    book_mockingbird = Book("To Kill a Mockingbird", "Harper Lee")
    book_gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book_war_and_peace = Book("War and Peace", "Leo Tolstoy")

    # Городская библиотека
    public = PublicLibrary(
        [book_1984, book_mockingbird, book_gatsby],
        name="Central Library",
        city="Moscow",
    )
    public.add_book(book_war_and_peace)

    print("=== Public library ===")
    public.display_books()
    public.borrow_book("1984")
    public.return_book("1984")

    # Школьная библиотека: дубликаты запрещены, лимит выдач = 2
    school = SchoolLibrary(name="School No. 5", max_borrowed=1)
    school.add_book(Book("1984", "George Orwell"))
    school.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    school.add_book(Book("1984", "George Orwell"))  # дубликат — не добавится

    print("\n=== School library ===")
    school.display_books()
    school.borrow_book("1984")
    school.borrow_book("The Great Gatsby")
    school.borrow_book("War and Peace")  # лимит уже достигнут / книги нет

    # Электронная библиотека: книга остаётся доступной после «скачивания»
    digital = DigitalLibrary(
        [Book("1984", "George Orwell"), Book("War and Peace", "Leo Tolstoy")],
        name="E-Library",
    )

    print("\n=== Digital library ===")
    digital.display_books()
    digital.borrow_book("1984")
    print("After download:")
    digital.display_books()  # 1984 всё ещё Available
    digital.return_book("1984")


if __name__ == "__main__":
    main()
