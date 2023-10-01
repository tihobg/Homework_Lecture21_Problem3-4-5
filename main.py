# problem 3, 4, 5

from ui import insert_new_list_books, load_from_csv_file, write_data_to_csv_file, load_preferred_author_books,\
    find_books_start_end_year, edit_book_line
from user_input_handler import num_books_to_insert, book_insert_author, no_book_author_preferred,\
    insert_start_end_pub_year, insert_delete_book_line, insert_edit_reply
from BOOKS import BOOKS

write_data_to_csv_file(BOOKS)
start_book_list = load_from_csv_file()
print()
number_new_books = num_books_to_insert()
print()
print(*start_book_list, sep='\n')
print()
new_l_b = insert_new_list_books(number_new_books)
total_list = start_book_list + new_l_b
write_data_to_csv_file(total_list)
new_book_list = load_from_csv_file()
print()
book_author_insert = book_insert_author()

author_list = load_preferred_author_books(book_author_insert)
no_book_author_preferred(author_list)
print()
start_end_year = insert_start_end_pub_year()

find_books_start_end_year(start_end_year)

delete_book = insert_delete_book_line()

new_book_list.pop(delete_book)
write_data_to_csv_file(new_book_list)
new_l_b = load_from_csv_file()

edit_reply = insert_edit_reply()
edit_book_line(edit_reply)
