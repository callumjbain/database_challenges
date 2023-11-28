from lib.album import Album

"""
Constructs with
id, title, release_year, and artist_id
"""

def tests_constructs_with_fields():
    album = Album(1, "Red", 2017, 3)
    assert album.id == 1
    assert album.title == "Red"
    assert album.release_year == 2017
    assert album.artist_id == 3

"""
Album constructs with an id, name and genre
"""
def test_album_constructs():
    album = Album(1, "Red", 2017, 3)
    assert album.id == 1
    assert album.title == "Red"
    assert album.release_year == 2017
    assert album.artist_id == 3

"""
We can format artists to strings nicely
"""
def test_album_format_nicely():
    album = Album(1, "Red", 2017, 3)
    assert str(album) == "Album(1, Red, 2017, 3)"

"""
We can compare two identical artists
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Red", 2017, 3)
    album2 = Album(1, "Red", 2017, 3)
    assert album1 == album2
