from typing import List


class Book:
    def __init__(self,
                 number,
                 book,
                 author,
                 year):
        self._number = number
        self._book = book
        self._author = author
        self._year = year

    @property
    def number(self):
        return self._number

    @property
    def book(self):
        return self._book

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    def __str__(self) -> str:
        return f"""Number: {self._number}
Book: {self._book}
Author: {self.author}
Year Revised: {self.year}
"""

    def serialize(self) -> List:
        return [self._number, self._book, self.author, self.year]
