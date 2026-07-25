import unittest

from book import Book


class TestBook(unittest.TestCase):
    def test_init_sets_title_and_author(self):
        book = Book("1984", "George Orwell")

        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "George Orwell")

    def test_new_book_is_available_by_default(self):
        book = Book("1984", "George Orwell")

        self.assertTrue(book.is_available)

    def test_str_when_available(self):
        book = Book("1984", "George Orwell")

        self.assertEqual(str(book), "'1984' by George Orwell - Available")

    def test_str_when_not_available(self):
        book = Book("1984", "George Orwell")
        book.is_available = False

        self.assertEqual(str(book), "'1984' by George Orwell - Not available")


if __name__ == "__main__":
    unittest.main()
