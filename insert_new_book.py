from book import Book
from BOOKS import BOOKS


def insert_new_book(index_new_list) -> Book:
    book_name = input('Please, enter the book title:\n')
    book_author = input('Please, enter the book author:\n')
    book_year = input('Please, enter the book year:\n')
    new_book_data = Book(len(BOOKS) + index_new_list - 2, book_name, book_author, book_year)
    return new_book_data
