"""
XB_0082: Bestselling Books
Author: Emanuela Dumitru

Copyright (c) 2021-2022 - Eindhoven University of Technology - VU Amsterdam, The Netherlands
This software is made available under the terms of the MIT License.
"""

from typing import Dict, List
import csv
import statistics

# TODO: Add your code to tasks 1 to 5 in this file.

class Book:
    def __init__(self, title, author, rating, reviews, price, years, genre = ""):
        self.title = title
        self.author = author
        self.rating = rating
        self.reviews = reviews
        self.price = price
        self.years = years
        self.genre = genre
        self.FICTION = 'Fiction'
        self.NON_FICTION = 'Non fiction'

    def __str__(self):
        return self.title




class FictionBook(Book):
    def __init__(self, title, author, rating, reviews, price, years):
        super().__init__(title, author, rating, reviews, price, years)
        self.genre = self.FICTION

    def __str__(self):
        output = ""
        separator = ", "
        for year in self.years:
            if year == self.years[-1]:
                separator = ""
            year_list = year + separator
        output = self.title + ":" + self.genre + "(" + year_list + ")"
        return output


class NonFictionBook(Book):
    def __init__(self, title, author, rating, reviews, price, years):
        super().__init__(title, author, rating, reviews, price, years)
        self.genre = self.NON_FICTION

    def __str__(self):
        output = ""
        separator = ", "
        for year in self.years:
            if year == self.years[-1]:
                separator = ""
            year_list = year + separator
        output = self.title + ":" + self.genre + "(" + year_list + ")"
        return output


class Amazon:
    def __init__(self, bestsellers):
        self.bestsellers = bestsellers

    def read_books_csv(self, path):
        with open(path, 'r', encoding='utf-8-sig') as csvdata:
            csvreader = csv.reader(csvdata)
            data_list = list(csvreader)
        books_dict = {}
        for row in data_list[1:]:
            if row[6] == "Fiction":
                book = FictionBook(row[0], row[1], float(row[2]), int(row[3]), int(row[4]), [int(row[5])])
            else:
                book = NonFictionBook(row[0], row[1], float(row[2]), int(row[3]), int(row[4]), [int(row[5])])
            if row[0] in books_dict:
                books_dict[row[0]].years.append(int(row[5]))
            else:
                books_dict.update({row[0]: book})
        self.bestsellers = list(books_dict.values())
