# Exercise 9
# favorite_fruits = list(input('What is your favorit fruit? if several,separate the fruits with a single space:'))
# any_fruit = input('Choose any fruit:')
# if any_fruit in favorite_fruits:
#     print('You chose one of your favorite fruits! Enjoy!')
# else:
#     print('You chose a new fruit. I hope you enjoy')

# Exercise 10
topping = True
while topping:
    add_topping = input("Please enter the pizza topping (enter 'quit' when you are finished): ")
    print('We\'ll add ' + add_topping + ' to your pizza')
    if add_topping == 'quit':
        topping = False
    