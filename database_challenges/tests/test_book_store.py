from lib.book_store import *

"""
When i create a book
with the fields id, title and author_name
They are reflected in the instance properties 
"""

def test_book_store_contructs():
    book_store = BookStore(1, "Jurassic Park", "Michael Crichton")
    assert book_store.id == 1
    assert book_store.title == "Jurassic Park"
    assert book_store.author_name == "Michael Crichton"

def test_books_format_nicely():
    book = BookStore(1, "Jurassic Park", "Michael Crichton")
    assert str(book) == "BookStore(1, Jurassic Park, Michael Crichton)"

def test_books_are_equal():
    book1 = BookStore(1, "Test Book", "Test Author")
    book2 = BookStore(1, "Test Book", "Test Author")
    assert book1 == book2