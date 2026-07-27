class Library:
    """Базовый класс библиотеки: общее поведение для всех разновидностей."""

    def __init__(self, books=None, name="Library"):
        # None вместо [] — чтобы у разных библиотек не было общего списка
        self.books = list(books) if books is not None else []
        self.name = name

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print(f"[{self.name}]")
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                print(f"You have borrowed '{book.title}' from {self.name}")
                return
        print(f"'{title}' is not available for borrowing.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_available:
                book.is_available = True
                print(f"You have returned '{book.title}' to {self.name}")
                return
        print(f"'{title}' was not borrowed.")

    def get_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def available_count(self):
        count = 0
        for book in self.books:
            if book.is_available:
                count += 1
        return count


class PublicLibrary(Library):
    """Городская библиотека: открыта для всех, показывает город."""

    def __init__(self, books=None, name="Public Library", city="Unknown"):
        super().__init__(books=books, name=name)
        self.city = city

    def display_books(self):
        print(f"[{self.name} — {self.city}]")
        for book in self.books:
            print(book)


class SchoolLibrary(Library):
    """Школьная библиотека: нельзя дублировать названия, лимит выдач."""

    def __init__(self, books=None, name="School Library", max_borrowed=2):
        super().__init__(books=books, name=name)
        self.max_borrowed = max_borrowed

    def add_book(self, book):
        if self.get_book(book.title) is not None:
            print(f"'{book.title}' is already in {self.name}. Duplicate not added.")
            return
        super().add_book(book)

    def borrow_book(self, title):
        borrowed_now = len(self.books) - self.available_count()
        if borrowed_now >= self.max_borrowed:
            print(
                f"Borrow limit reached in {self.name} "
                f"(max {self.max_borrowed}). Return a book first."
            )
            return
        super().borrow_book(title)


class DigitalLibrary(Library):
    """Электронная библиотека: копия всегда доступна (не помечаем книгу занятой)."""

    def __init__(self, books=None, name="Digital Library"):
        super().__init__(books=books, name=name)

    def borrow_book(self, title):
        book = self.get_book(title)
        if book is None:
            print(f"'{title}' is not available for borrowing.")
            return
        # Цифровая копия: скачали, но физически книга не «уходит»
        print(f"You have downloaded '{book.title}' from {self.name}")

    def return_book(self, title):
        book = self.get_book(title)
        if book is None:
            print(f"'{title}' was not borrowed.")
            return
        print(f"No return needed for digital copy of '{book.title}' in {self.name}")
