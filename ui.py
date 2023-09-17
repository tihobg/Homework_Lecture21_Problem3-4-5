from insert_new_book import insert_new_book
from typing import List


def insert_new_list_books(b, num_new_books) -> List:
    # number_new_books = int(input('Please, enter how many books to insert?\n'))
    new_book_list = []
    for b in range(num_new_books):
        new_book = insert_new_book()
        new_book_list.append(new_book)
    return new_book_list

