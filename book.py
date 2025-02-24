class Book:
    def __init__(self, title, author):
        self.title = title  # Название книги
        self.author = author  # Автор книги
        self.is_available = True  # Статус доступности книги

    def __str__(self):
        availability = "Available" if self.is_available else "Not available"
        return f"'{self.title}' by {self.author} - {availability}"
