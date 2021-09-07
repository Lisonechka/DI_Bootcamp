# Exercise 1: Cats
from typing import List


class Cat:
    def __init__(self, name=List, age=List):
        self.name = name
        self.age = age


cats = Cat(["Big", "Toto", "Manu"], [3, 1, 5])


def oldest_cat():
    the_oldest_cat = max(cats.age)
    oldest_idx = cats.age.index(the_oldest_cat)
    oldest_name = cats.name[oldest_idx]
    return oldest_name


print(f'The oldest cat is {oldest_cat()}, and he is {max(cats.age)} years old.')
