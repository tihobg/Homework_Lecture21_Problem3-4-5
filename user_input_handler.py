from typing import Tuple


def num_books_to_insert() -> int:
    while True:
        try:
            number_new_books = int(input('Please, enter how many books to insert?\n'))
            break
        except ValueError:
            print('Enter an integer, please!\n')
    return number_new_books


def book_insert_author() -> str:
    while True:
        author_insert = input('Please, insert the book author preferred:\n')
        if not author_insert.isnumeric():
            break
        else:
            print('Enter a string, not an integer, please!\n')
    return author_insert


def no_book_author_preferred(author_list):
    if len(author_list) == 0:
        print('There is no book written by this author!\n')


def insert_start_end_pub_year() -> Tuple:
    book_start_year = int(input('Please, insert the start publishing year of the book!\n'))
    book_end_year = int(input('Please, insert the end publishing year!\n'))
    start_end_year = (book_start_year, book_end_year)
    return start_end_year


def insert_delete_book_line() -> int:
    delete_book = int(input('Please, enter the line that you want to delete!\n'))
    return delete_book


def insert_edit_reply() -> str:
    edit_reply = input('Do you want to edit a book information\n')
    return edit_reply
