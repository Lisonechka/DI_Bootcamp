# Exercise 1
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

