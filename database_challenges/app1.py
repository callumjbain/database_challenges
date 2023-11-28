from lib.database_connection import DatabaseConnection
from lib.book_repository import *

connection = DatabaseConnection()
connection.connect()

connection.seed('seeds/book_store.sql')

book_repository = BookRepository(connection)
books = book_repository.all()

for book in books:
    print(book)