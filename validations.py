def book_name_existed(books, book_name):
    book_name = book_name.lower()
    for book in books:
        if book["name"].lower() == book_name:
            return True
    return False

def book_author_existed(books, book_author):
    book_author = book_author.lower()
    for book in books:
        if book["author"].lower() == book_author:
            return True
    return False

def book_id_existed(books, book_id):
    for book in books:
        if book["id"] == book_id:
            return True
    return False
