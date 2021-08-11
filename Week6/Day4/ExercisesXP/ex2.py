# Exercise 9
favorite_fruits = list(input('What is your favorit fruit? if several,separate the fruits with a single space:'))
any_fruit = input('Choose any fruit:')
if any_fruit in favorite_fruits:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')
    