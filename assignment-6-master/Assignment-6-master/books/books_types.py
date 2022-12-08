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
    FICTION = 'Fiction'
    NON_FICTION = 'Non Fiction'
    recommended = False
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

    def recommend(self, rat, num_revs):
        if rat > self.rating or num_revs > self.reviews:
            self.recommended = False
        else:
            self.recommended = True


class FictionBook(Book):
    def __init__(self, title, author, rating, reviews, price, years):
        super().__init__(title, author, rating, reviews, price, years, self.FICTION)

    def __str__(self):
        output = ""
        separator = ", "
        year_list = ""
        for year in self.years:
            if year == self.years[-1]:
                separator = ""
            year_list += str(year) + separator
        output = self.title + ": " + self.genre + " (" + year_list + ")"
        return output


class NonFictionBook(Book):
    def __init__(self, title, author, rating, reviews, price, years):
        super().__init__(title, author, rating, reviews, price, years, self.NON_FICTION)

    def __str__(self):
        output = ""
        separator = ", "
        year_list = ""
        for year in self.years:
            if year == self.years[-1]:
                separator = ""
            year_list += str(year) + separator
        output = self.title + ": " + self.genre + " (" + year_list + ")"
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

    def best_year_rating(self):
        year_dict = {year: [] for year in range(2009, 2020)}
        for book in self.bestsellers:
            for year in book.years:
                year_dict[year].append(book.rating)
        for year in year_dict:
            mean = statistics.mean(year_dict[year])
            year_dict[year] = mean
        higher_rating = year_dict[2009]
        year_hr = 2009
        for year in year_dict:
            if higher_rating < year_dict[year]:
                higher_rating = year_dict[year]
                year_hr = year
        return int(year_hr)

    def best_year_reviews(self):
        year_dict = {year: [] for year in range(2009, 2020)}
        for book in self.bestsellers:
            for year in book.years:
                year_dict[year].append(book.reviews)
        for year in year_dict:
            mean = statistics.mean(year_dict[year])
            year_dict[year] = mean
        higher_reviews = year_dict[2009]
        year_hrev = 2009
        for year in year_dict:
            if higher_reviews < year_dict[year]:
                higher_reviews = year_dict[year]
                year_hrev = year
        return int(year_hrev)

    def recommend_book(self, rat, num_revs):
        for i in range(0, len(self.bestsellers)):
            self.bestsellers[i].recommend(rat, num_revs)

    def get_recommendations(self):
        recommended_list = []
        for book in self.bestsellers:
            if book.recommended:
                recommended_list.append(str(book))
        return recommended_list
