from validations import *

def display_books(books):
    if not books:
        print("No books found.")
        return None

    print("\nBook list:")
    for book in books:
        print(f"- {book["name"]} by {book["author"]} ({book["year"]})")
    return

def search_book(books, name):
    if not books:
        print("No books found.")
        return None

    found_books = []
    name = name.lower()

    for book in books:
        if name in book["name"].lower():
            found_books.append(book)

    if not found_books:
        print("\nBook name not found")
        return None

    print(f"\n{len(found_books)} books found:")
    for book in found_books:
        print(f"- {book["name"]} by {book["author"]} ({book["year"]})")
    return found_books


def get_next_book_id(books):
    if not books:
        print("No books found.")
        return None

    return books[-1]["id"] + 1

def add_book(books, name, author, year):
    if not books:
        print("No books found.")
        return None

    if book_name_existed(books, name) and book_author_existed(books, author):
        print("\nBook is already existed (name and author)")
        return False

    book_id = get_next_book_id(books)

    new_book = {"id": book_id, "name": name, "author": author, "year": year, "available": True}
    books.append(new_book)

    if books[-1] == new_book:
        print("\nBook added successfully")
        return True

    print("\nBook was not added")
    return False

def borrow_book(books, book_id):
    if not books:
        print("No books found.")
        return None

    if not book_id_existed(books, book_id):
        print("Book ID does not exists")
        return False

    for book in books:
        if book["id"] == book_id:
            if book["available"] == True:
                book["available"] = False
                print("\nThe book was successfully borrowed")
                return True
            print("\nBook is already borrowed")
            return False

def return_book(books, book_id):
    if not books:
        print("No books found.")
        return None

    if not book_id_existed(books, book_id):
        print("Book ID does not exists")
        return False

    for book in books:
        if book["id"] == book_id:
            if book["available"] == False:
                book["available"] = True
                print("\nThe book was successfully returned")
                return True
            print("\nBook is not borrowed")
            return False

def get_available_books(books):
    if not books:
        print("No books found.")
        return None

    available_books = []

    for book in books:
        if book["available"] == True:
            available_books.append(f"- {book["name"]} by {book["author"]} ({book["year"]})")
    
    if not available_books:
        print("No available books found")
        return available_books
    
    print(f"\n{len(available_books)} available books found:")
    return available_books

def get_books_by_author(books, author):
    if not books:
        print("No books found.")
        return None

    authors_books = []
    author = author.lower()

    for book in books:
        if book["author"].lower() == author:
            authors_books.append(f"- {book["name"]} by {book["author"]} ({book["year"]})")
    
    if not authors_books:
        print(f"\nNo books by {author} found")
        return authors_books
    
    print(f"\n{len(authors_books)} books by {author} found:")
    return authors_books

def get_old_books(books):
    if not books:
        print("No books found.")
        return None

    old_books = []
    
    for book in books:
        if book["year"] < 2000:
            old_books.append(f"- {book["name"]} by {book["author"]} ({book["year"]})")
    
    if not old_books:
        print("\nNo old books found")
        return old_books
    
    print(f"\n{len(old_books)} books older than 2000 found:")
    return old_books

def sort_books_by_year(books):
    if not books:
        print("No books found.")
        return None

    books.sort(key=lambda book: book["year"])
    print("\nBooks sorted by year")
    return

def remove_book_by_id(books, book_id):
    if not books:
        print("No books found.")
        return None

    if not book_id_existed(books, book_id):
        print("Book ID does not exists")
        return False

    index = 0
    for book in books:
        if book["id"] == book_id:
            books.pop(index)
            print(f"{book["name"]} by {book["author"]} removed from library")
            return
        index += 1

def status_update(books):
    if not books:
        print("No books found.")
        return None

    book_in_library = len(books)
    available_books = len(get_available_books(books))
    borrowed_books = book_in_library - available_books

    print(f"\n--- Status Update ---\nBooks in library: {book_in_library}\nAvailable books: {available_books}\nBorrowed books: {borrowed_books}")
    return

def get_oldest_book(books):
    if not books:
        print("No books found.")
        return None

    oldest_book = min(books, key=lambda book: book["year"])
    print(f"\nOldest book:\n{oldest_book["name"]} by {oldest_book["author"]} ({oldest_book["year"]})")
    return