def get_book_name():
    valid_book_name = False
    while not valid_book_name:
        book_name = input("Book name: ")
        if book_name:
            valid_book_name = True
    return book_name

def get_book_author():
    valid_book_author = False
    while not valid_book_author:
        book_author = input("Author name: ")
        if book_author:
            valid_book_author = True
    return book_author

def get_book_year():
    valid_book_year = False
    while not valid_book_year:
        try:
            book_year = int(input("Book year: "))
        except ValueError:
            print("Book year must be integer")
            continue

        if book_year < 1:
            print("Book year must be positive")
            continue
        
        valid_book_year = True
    return book_year

def get_book_id(books):
    if not books:
        print("No books found.")
        return None
        
    valid_book_id = False
    while not valid_book_id:
        try:
            book_id = int(input("Book ID: "))
        except ValueError:
            print("Book ID must be integer")
            continue

        if book_id < 1:
            print("Book ID must be positive")
            continue

        valid_book_id = True
    return book_id