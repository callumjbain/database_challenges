from lib.book_store import *
from lib.book_repository import *
# import from ...

"""
When i call all on the BookRepository
I get all the books back in a list
"""

# def lisst all atrists(db_connection)
# seed database 
# create bookstore repository(db_connection)
#  call all
# assert result is == seeds

def test_show_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)

    books = repository.all()

    assert books == [  BookStore(1, 'Nineteen Eighty-Four', 'George Orwell'),
                            BookStore(2, 'Mrs Dalloway', 'Virginia Woolf'),
                            BookStore(3, 'Emma', 'Jane Austen'),
                            BookStore(4, 'Dracula', 'Bram Stoker'),
                            BookStore(5, 'The Age of Innocence', 'Edith Wharton'),
]
    
