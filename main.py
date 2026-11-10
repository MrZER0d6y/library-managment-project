from data import books
from user_input import *
from library_managment import *

def main():
    exiting = False

    while not exiting:
        print("""
================================
       LIBRARY MANAGEMENT
================================

1. Display all books
2. Search book by name
3. Add new book
4. Borrow a book
5. Return a book
6. Display available books
7. Display books by author
8. Display books older than 2000
9. Sort books by year
10. Remove book by ID
11. Status update
12. Display oldest book
13. Exit
""")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Option must be integer")
            continue
        if choice < 1 or choice > 13:
            print("Option must be between 1-13")
            continue

        if choice == 1:
            display_books(books)
        elif choice == 2:
            search_book(books, get_book_name())
        elif choice == 3:
            add_book(books, get_book_name(), get_book_author(), get_book_year())
        elif choice == 4:
            borrow_book(books, get_book_id(books))
        elif choice == 5:
            return_book(books, get_book_id(books))
        elif choice == 6:
            for book in get_available_books(books):
                print(book)
        elif choice == 7:
            for book in get_books_by_author(books, get_book_author()):
                print(book)
        elif choice == 8:
            for book in get_old_books(books):
                print(book)
        elif choice == 9:
            sort_books_by_year(books)
        elif choice == 10:
            remove_book_by_id(books, get_book_id(books))
        elif choice == 11:
            status_update(books)
        elif choice == 12:
            get_oldest_book(books)
        elif choice == 13:
            print("Exiting...")
            exiting = True
    
    return 0

if __name__ == "__main__":
    main()