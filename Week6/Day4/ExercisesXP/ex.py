# # Exercise 1
#1
my_fav_numbers = {3, 16, 7, 8}
#2
new_numbers = [30, 55]
my_fav_numbers.update(new_numbers)
print(my_fav_numbers)
#3
my_fav_numbers = set(list(my_fav_numbers)[:-1])
print(my_fav_numbers)
#4-5
friend_fav_numbers = {1, 7, 90, 100}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#Exercise 2
# Only if tuple convert into a list, and then back

#Exercise 3
item = 1
for i in range(1, 21):
    print(item)
    item +=1

#Exercise 4 How to start fromm 1.5
import decimal

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

print(list(float_range(1, 5, '0.5')))

# Exercise 5
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
basket.remove('Blueberries')
basket.append('Kiwi')
basket.insert(0, 'Apples')
print(basket.count('Apples'))
basket.clear()
print(basket)

# Exercise 6
user_name = ''
while user_name != 'Liza':
    user_name = input('What is yor name? ')
print('Ok, I recognized you')

# Exercise 7
my_list = ['a', 2, 16, 'd', 'abc', 'loop']
for idx, val in enumerate(my_list):
    if idx %2 == 0 :
        print(val)

# Exercise 8
for i in range(1500, 2501):
    if i%5==0 and i%7==0 :
        print(i)


