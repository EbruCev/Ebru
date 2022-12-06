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
