from lib.book_store import BookStore
# create class
# create function
# initialise function(self, connection)

# create all function

class BookRepository():

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = BookStore(row['id'], row['title'], row['author_name'])
            books.append(item)
        return books