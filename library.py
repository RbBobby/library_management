from abc import ABC, abstractmethod


class Library(ABC):
    """Абстрактная библиотека — учебный пример абстракции.

    Описывает общий контракт: любая библиотека умеет показывать каталог,
    выдавать и принимать книги. Создавать Library() напрямую нельзя —
    нужен конкретный тип: PublicLibrary, SchoolLibrary, DigitalLibrary.

    В дебаггере смотрите _books и _name.
    """

    def __init__(self, books=None, name="Library"):
        self._books = list(books) if books is not None else []
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def books(self):
        return list(self._books)

    def add_book(self, book):
        self._books.append(book)

    def get_book(self, title):
        for book in self._books:
            if book.title == title:
                return book
        return None

    def available_count(self):
        count = 0
        for book in self._books:
            if book.is_available:
                count += 1
        return count

    def _print_books(self):
        """Общая реализация: печать списка книг (переиспользуют наследники)."""
        for book in self._books:
            print(book)

    def _borrow_physical_book(self, title):
        """Общая логика выдачи бумажной книги."""
        for book in self._books:
            if book.title == title and book.is_available:
                book.borrow()
                print(f"You have borrowed '{book.title}' from {self._name}")
                return
        print(f"'{title}' is not available for borrowing.")

    def _return_physical_book(self, title):
        """Общая логика возврата бумажной книги."""
        for book in self._books:
            if book.title == title and not book.is_available:
                book.give_back()
                print(f"You have returned '{book.title}' to {self._name}")
                return
        print(f"'{title}' was not borrowed.")

    @abstractmethod
    def display_books(self):
        """Показать каталог. Формат зависит от типа библиотеки."""

    @abstractmethod
    def borrow_book(self, title):
        """Выдать книгу. Правила зависят от типа библиотеки."""

    @abstractmethod
    def return_book(self, title):
        """Вернуть книгу. Правила зависят от типа библиотеки."""

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, books={len(self._books)})"


class PublicLibrary(Library):
    """Городская библиотека: открыта для всех, показывает город."""

    def __init__(self, books=None, name="Public Library", city="Unknown"):
        super().__init__(books=books, name=name)
        self._city = city

    @property
    def city(self):
        return self._city

    def display_books(self):
        print(f"[{self._name} — {self._city}]")
        self._print_books()

    def borrow_book(self, title):
        self._borrow_physical_book(title)

    def return_book(self, title):
        self._return_physical_book(title)


class SchoolLibrary(Library):
    """Школьная библиотека: нельзя дублировать названия, лимит выдач."""

    def __init__(self, books=None, name="School Library", max_borrowed=2):
        super().__init__(books=books, name=name)
        self._max_borrowed = max_borrowed

    @property
    def max_borrowed(self):
        return self._max_borrowed

    def add_book(self, book):
        if self.get_book(book.title) is not None:
            print(f"'{book.title}' is already in {self.name}. Duplicate not added.")
            return
        super().add_book(book)

    def display_books(self):
        print(f"[{self._name}]")
        self._print_books()

    def borrow_book(self, title):
        borrowed_now = len(self._books) - self.available_count()
        if borrowed_now >= self._max_borrowed:
            print(
                f"Borrow limit reached in {self.name} "
                f"(max {self._max_borrowed}). Return a book first."
            )
            return
        self._borrow_physical_book(title)

    def return_book(self, title):
        self._return_physical_book(title)


class DigitalLibrary(Library):
    """Электронная библиотека: копия всегда доступна (не помечаем книгу занятой)."""

    def __init__(self, books=None, name="Digital Library"):
        super().__init__(books=books, name=name)

    def display_books(self):
        print(f"[{self._name} — digital]")
        self._print_books()

    def borrow_book(self, title):
        book = self.get_book(title)
        if book is None:
            print(f"'{title}' is not available for borrowing.")
            return
        print(f"You have downloaded '{book.title}' from {self.name}")

    def return_book(self, title):
        book = self.get_book(title)
        if book is None:
            print(f"'{title}' was not borrowed.")
            return
        print(f"No return needed for digital copy of '{book.title}' in {self.name}")
