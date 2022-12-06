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
    def __init__(self, title, author, rating, reviews, price, years, genre):
        self.title = title
        self.author = author
        self.rating = rating
        self.reviews = reviews
        self.price = price
        self.years = years
        self.genre = genre

    def __str__(self):
        return self.title


class Amazon:
    def __init__(self, bestsellers):
        self.bestsellers = bestsellers

class FictionBook(Book):
    def __init__(self, title, author, rating, reviews, price, years):
        super().__init__(title, author, rating, reviews, price, years, self.FICTION)

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
        super().__init__(title, author, rating, reviews, price, years, self.NON_FICTION)

    def __str__(self):
        output = ""
        separator = ", "
        for year in self.years:
            if year == self.years[-1]:
                separator = ""
            year_list = year + separator
        output = self.title + ":" + self.genre + "(" + year_list + ")"
        return output
