from book import Book


def insert_new_book():
    book_name = input('Please, enter the book title:\n')
    book_author = input('Please, enter the book author:\n')
    book_year = input('Please, enter the book year:\n')
    book_number = 1
    print(book_number)
    new_book_data = Book(book_number, book_name, book_author, book_year)
    return new_book_data

