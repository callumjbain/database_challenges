book_store
class - BookStore

initialise class with id, title and author_name
def __innit__(self, id, title, author_name)
create instances of each argument

create methor which allowes tests to assert objects are the ones we expect
def __eq__(self, other)

create method to make output look nicer
def __repr__(self)


book_repository
class - BookRepository

initiialise the class with connection as argument
def __init__(self, connection)

def all(self)
returns all entries in database
