# Exercise 4 : Random
import random
def compare_numbers():
     for i in range(1,101):
        random_num = random.randrange(0, 101)
        if i == random_num:
             print(f'Success. First number was {i}, and second number was {random_num}')
        else:
            print(f'Fail. First number was {i}, and second number was {random_num}')

compare_numbers()

     


