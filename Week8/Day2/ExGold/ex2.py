# Exercise 2 : Custom List Class
import random
from typing import List


class MyList:
    def __init__(self, letters: List):
        self.letters = letters

    def reverse_list(self):
        return self.letters.reverse()

    def sort_list(self):
        return self.letters.sort()

    def new_list(self):
        new_randoms_list = list(random.sample(range(100), len(self.letters)))
        print(new_randoms_list)


list1 = MyList(['a', 'm', 'k', 'b', 'd'])
print(list1.letters)
list1.reverse_list()
print(list1.letters)

list1.sort_list()
print(list1.letters)

list1.new_list()





