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
        book.borrow()

        self.assertEqual(str(book), "'1984' by George Orwell - Not available")

    def test_borrow_and_give_back(self):
        book = Book("1984", "George Orwell")

        self.assertTrue(book.borrow())
        self.assertFalse(book.is_available)
        self.assertFalse(book.borrow())  # уже выдана

        self.assertTrue(book.give_back())
        self.assertTrue(book.is_available)
        self.assertFalse(book.give_back())  # уже доступна

    def test_title_and_author_are_read_only_via_properties(self):
        book = Book("1984", "George Orwell")

        with self.assertRaises(AttributeError):
            book.title = "Animal Farm"

        with self.assertRaises(AttributeError):
            book.author = "Someone Else"

        with self.assertRaises(AttributeError):
            book.is_available = False


if __name__ == "__main__":
    unittest.main()
