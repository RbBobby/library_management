class Book:
    """Книга с инкапсулированным состоянием.

    В дебаггере смотрите поля с `_` (_title, _author, _is_available).
    Снаружи читайте через свойства, меняйте статус через borrow()/give_back().
    """

    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._is_available = True

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def is_available(self):
        return self._is_available

    def borrow(self):
        """Выдать книгу. True — удалось, False — уже выдана."""
        if not self._is_available:
            return False
        self._is_available = False
        return True

    def give_back(self):
        """Вернуть книгу. True — удалось, False — книга и так была доступна."""
        if self._is_available:
            return False
        self._is_available = True
        return True

    def __str__(self):
        availability = "Available" if self._is_available else "Not available"
        return f"'{self._title}' by {self._author} - {availability}"

    def __repr__(self):
        # Удобно читать объект в Debug Console / Variables
        return (
            f"Book(title={self._title!r}, author={self._author!r}, "
            f"available={self._is_available})"
        )
