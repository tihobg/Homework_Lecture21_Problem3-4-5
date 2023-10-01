from insert_new_book import insert_new_book
from typing import List
import csv
from book import Book


def insert_new_list_books(num_new_books) -> List[Book]:
    new_book_list = []
    index_new_list = 0
    for b in range(num_new_books):
        index_new_list = index_new_list + 1
        new_book = insert_new_book(index_new_list)
        new_book_list.append(new_book)
    return new_book_list


def load_from_csv_file() -> List[Book]:
    with open('Book.csv', 'r') as f:
        reader = csv.reader(f)
        result = []
        i = -1
        for line in reader:
            i += 1
            line[0] = i
            book = Book(*line)
            result.append(book)
        print(*result, sep='\n')
    return result


def load_preferred_author_books(book_author_insert) -> List[Book]:
    with open('Book.csv', 'r') as f:
        reader = csv.reader(f)
        author_list = []
        for line in reader:
            if line[2] == book_author_insert:
                book = Book(*line)
                author_list.append(book)
        print(*author_list, sep='\n')
    return author_list


def write_data_to_csv_file(books):
    with open('Book.csv', 'w') as f:
        writer = csv.writer(f)
        i = -1
        # writer.writerow(['N', 'Book', 'Author', 'Year Released'])
        for b in books:
            i += 1
            # b[0] = i
            # book = Book(*b)
            writer.writerow([i, b.book, b.author, b.year])
            # print(b)


def find_books_start_end_year(start_end_year):
    with open('Book.csv', 'r') as f:
        reader = csv.reader(f)
        list_data_books = []
        for line in reader:
            list_data_books.append(line)
        books_no_row_title = list_data_books[1::]
        book_year_list = []
        for line in books_no_row_title:
            if start_end_year[0] <= int(line[3]) <= start_end_year[1]:
                book = Book(*line)
                # content = line
                book_year_list.append(book)
        if book_year_list:
            print(*book_year_list, sep='\n')
        else:
            print('There is no books from this author written between these years!\n')


def edit_book_line(edit_reply: str) -> List[Book]:
    if edit_reply == 'yes' or edit_reply == 'Yes':
        edit_line = int(input('Please, enter the book line number for edition!\n'))
        with open('Book.csv', 'r') as f:
            reader = csv.reader(f)
            list_edit_data_books = []
            i = -1
            for line in reader:
                i += 1
                if i == edit_line:
                    edit_book = input('Please, enter the new book title\n')
                    edit_author = input('Please, enter the new author\n')
                    edit_year = int(input('Please, enter the new year released\n'))
                    edit_book = Book(edit_line, edit_book, edit_author, edit_year)
                    list_edit_data_books.append(edit_book)
                else:
                    b = Book(*line)
                    list_edit_data_books.append(b)
            print(*list_edit_data_books, sep='\n')
    return list_edit_data_books
