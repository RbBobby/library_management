import unittest
from io import StringIO
from unittest.mock import patch

from book import Book
from library import Library, PublicLibrary, SchoolLibrary, DigitalLibrary


class TestLibraryBaseBehavior(unittest.TestCase):
    """Общее поведение через конкретную PublicLibrary (Library — абстрактный)."""

    def setUp(self):
        self.book_1984 = Book("1984", "George Orwell")
        self.book_gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald")
        self.library = PublicLibrary([self.book_1984, self.book_gatsby])

    def test_library_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            Library()

    def test_init_with_books(self):
        self.assertEqual(len(self.library.books), 2)
        self.assertIn(self.book_1984, self.library.books)
        self.assertIn(self.book_gatsby, self.library.books)

    def test_init_with_empty_list(self):
        library = PublicLibrary([])

        self.assertEqual(library.books, [])

    def test_init_default_creates_independent_lists(self):
        library_a = PublicLibrary()
        library_b = PublicLibrary()
        library_a.add_book(Book("1984", "George Orwell"))

        self.assertEqual(len(library_a.books), 1)
        self.assertEqual(len(library_b.books), 0)

    def test_books_property_returns_copy(self):
        snapshot = self.library.books
        snapshot.clear()

        self.assertEqual(len(self.library.books), 2)
        self.assertEqual(len(self.library._books), 2)

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
        self.book_1984.borrow()

        self.library.borrow_book("1984")

        self.assertIn("'1984' is not available for borrowing.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_borrow_book_when_not_in_library(self, mock_stdout):
        self.library.borrow_book("Harry Potter")

        self.assertIn("'Harry Potter' is not available for borrowing.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_return_book_makes_book_available(self, mock_stdout):
        self.book_1984.borrow()

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


class TestPublicLibrary(unittest.TestCase):
    def test_is_subclass_of_library(self):
        self.assertTrue(issubclass(PublicLibrary, Library))

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_books_shows_city(self, mock_stdout):
        library = PublicLibrary(
            [Book("1984", "George Orwell")],
            name="Central",
            city="Moscow",
        )

        library.display_books()
        output = mock_stdout.getvalue()

        self.assertIn("Central", output)
        self.assertIn("Moscow", output)
        self.assertIn("1984", output)
        self.assertEqual(library.city, "Moscow")


class TestSchoolLibrary(unittest.TestCase):
    def setUp(self):
        self.library = SchoolLibrary(name="School No. 5", max_borrowed=2)

    def test_is_subclass_of_library(self):
        self.assertTrue(issubclass(SchoolLibrary, Library))

    @patch("sys.stdout", new_callable=StringIO)
    def test_add_book_rejects_duplicate_title(self, mock_stdout):
        self.library.add_book(Book("1984", "George Orwell"))
        self.library.add_book(Book("1984", "George Orwell"))

        self.assertEqual(len(self.library.books), 1)
        self.assertIn("Duplicate not added", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_borrow_respects_max_borrowed_limit(self, mock_stdout):
        self.library.add_book(Book("1984", "George Orwell"))
        self.library.add_book(Book("Gatsby", "Fitzgerald"))
        self.library.add_book(Book("War and Peace", "Tolstoy"))

        self.library.borrow_book("1984")
        self.library.borrow_book("Gatsby")
        self.library.borrow_book("War and Peace")

        self.assertIn("Borrow limit reached", mock_stdout.getvalue())
        self.assertTrue(self.library.get_book("War and Peace").is_available)


class TestDigitalLibrary(unittest.TestCase):
    def setUp(self):
        self.book = Book("1984", "George Orwell")
        self.library = DigitalLibrary([self.book], name="E-Library")

    def test_is_subclass_of_library(self):
        self.assertTrue(issubclass(DigitalLibrary, Library))

    @patch("sys.stdout", new_callable=StringIO)
    def test_borrow_keeps_book_available(self, mock_stdout):
        self.library.borrow_book("1984")

        self.assertTrue(self.book.is_available)
        self.assertIn("downloaded", mock_stdout.getvalue().lower())

    @patch("sys.stdout", new_callable=StringIO)
    def test_return_explains_no_return_needed(self, mock_stdout):
        self.library.return_book("1984")

        self.assertIn("No return needed", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
