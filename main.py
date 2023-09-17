# problem 3, 4, 5
import csv
from book import Book
from ui import insert_new_list_books

books = [
    Book('0', 'To Kill A Mockingbird', 'Harper Lee', '1960'),
    Book('1', 'A Brief History of Time', 'Stephen Hawking', '1988'),
    Book('2', 'The Great Gatsby', 'F.Scott Fitzgerald', '1922')
]
print([str(b) for b in books])
with open('Book.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([' ', 'Book', 'Author', 'Year Released'])
    for b in books:
        writer.writerow([b.number, b.book, b.author, b.year])
        print(b)

number_new_books = int(input('Please, enter how many books to insert?\n'))
new_l_b = insert_new_list_books(books, number_new_books)

with open('Book.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([' ', 'Book', 'Author', 'Year Released'])
    for b in books:
        writer.writerow([b.number, b.book, b.author, b.year])
    for b in range(number_new_books):
        writer.writerow([new_l_b[b].number + len(books) - 1 + b, new_l_b[b].book, new_l_b[b].author, new_l_b[b].year])

book_author_insert = input('Please, insert the book author preferred:\n')
with open('Book.csv', 'r') as f:
    reader = csv.reader(f)
    author_list = []
    for line in reader:
        if line[2] == book_author_insert:
            content = line
            author_list.append(content)
    print(author_list)
    if len(author_list) == 0:
        print('There is no book written by this author!\n')

book_start_year = int(input('Please, insert the start publishing year of the book!\n'))
book_end_year = int(input('Please, insert the end publishing year!\n'))
print(type(book_start_year))

with open('Book.csv', 'r') as f:
    reader = csv.reader(f)
    list_data_books = []
    for line in reader:
        list_data_books.append(line)
    books_no_row_title = list_data_books[1::]
    book_year_list = []
    for line in books_no_row_title:
        if book_start_year <= int(line[3]) <= book_end_year:
            content = line
            book_year_list.append(content)
    if book_year_list:
        print(book_year_list)
    else:
        print('There is no books from this author written between these years!\n')


with open('Book.csv', 'r') as f:
    reader = csv.reader(f)
    content = [line for line in reader if len(line) > 0]
    for row in content:
        print(row)
    # print(content)
