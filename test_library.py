import unittest
from io import StringIO
from unittest.mock import patch

from book import Book
from library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.book_1984 = Book("1984", "George Orwell")
        self.book_gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald")
        self.library = Library([self.book_1984, self.book_gatsby])

    def test_init_with_books(self):
        self.assertEqual(len(self.library.books), 2)
        self.assertIn(self.book_1984, self.library.books)
        self.assertIn(self.book_gatsby, self.library.books)

    def test_init_with_empty_list(self):
        library = Library([])

        self.assertEqual(library.books, [])

    def test_add_book(self):
        new_book = Book("War and Peace", "Leo Tolstoy")

        self.library.add_book(new_book)

        self.assertEqual(len(self.library.books), 3)
        self.assertIn(new_book, self.library.books)

    def test_get_book_returns_book_when_found(self):
        found = self.library.get_book("1984")

        self.assertIs(found, self.book_1984)

    def test_get_book_returns_none_when_not_found(self):
        found = self.library.get_book("Harry Potter")

        self.assertIsNone(found)

    @patch("sys.stdout", new_callable=StringIO)
    def test_borrow_book_makes_book_unavailable(self, mock_stdout):
        self.library.borrow_book("1984")

        self.assertFalse(self.book_1984.is_available)
        self.assertIn("You have borrowed '1984'", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_borrow_book_when_already_borrowed(self, mock_stdout):
        self.book_1984.is_available = False

        self.library.borrow_book("1984")

        self.assertIn("'1984' is not available for borrowing.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_borrow_book_when_not_in_library(self, mock_stdout):
        self.library.borrow_book("Harry Potter")

        self.assertIn("'Harry Potter' is not available for borrowing.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_return_book_makes_book_available(self, mock_stdout):
        self.book_1984.is_available = False

        self.library.return_book("1984")

        self.assertTrue(self.book_1984.is_available)
        self.assertIn("You have returned '1984'", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_return_book_when_not_borrowed(self, mock_stdout):
        self.library.return_book("1984")

        self.assertIn("'1984' was not borrowed.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_return_book_when_not_in_library(self, mock_stdout):
        self.library.return_book("Harry Potter")

        self.assertIn("'Harry Potter' was not borrowed.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_books_prints_all_books(self, mock_stdout):
        self.library.display_books()
        output = mock_stdout.getvalue()

        self.assertIn("'1984' by George Orwell - Available", output)
        self.assertIn("'The Great Gatsby' by F. Scott Fitzgerald - Available", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_borrow_then_return_flow(self, mock_stdout):
        self.library.borrow_book("1984")
        self.assertFalse(self.book_1984.is_available)

        self.library.return_book("1984")
        self.assertTrue(self.book_1984.is_available)


if __name__ == "__main__":
    unittest.main()
