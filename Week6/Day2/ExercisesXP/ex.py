# Exercise 1
print('Hello world\n' *4)

# Exercise 2
print((99 ** 3) * 8)

#Exercise 3
5 < 3 #False
3 == 3 #True
3 == "3" #False
"3" > 3 # Traceback (most recent call last):
  #File "<stdin>", line 1, in <module>
  # TypeError: '<' not supported between instances of 'str' and 'int'
"Hello" == "hello" #False

# Exercise 4
computer_brand = 'Asus'
 print('I have a ' + computer_brand + ' computer') # in shell code is ok. But here, I have a mistake with print fuction. Why?

# Exercise 5
name = 'Liza'
age = 30
shoe_size = 36
info = "My name is " + name + ", I am " + str(age) + " years old, and " + str(shoe_size) + " size of shoe"
print(info)

# Exercise 6
a = 20
b = 5
if a > b:
    print('Hello World')

# Exercise 7
if int(input('Write the number:')) % 2 == 0:
    print ('This is even')
else:
    print('This is odd')

# Exercise 8
user_name = input('What is your name:')


# Exercise 9
inch_1 = 2.54
user_height = int(input('What is your height in inches:')) * inch_1
if user_height > 145:
    print('You are tall enough to ride.')
else:
    print('You are not tall enough, you need to grow some more to ride.')







