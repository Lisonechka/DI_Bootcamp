user_string = input('Please, write a string:')

#1
if len(user_string) < 10:
    print('string not long enough')
elif len(user_string) > 10:
    print('string too long')
else:
    print('ok')

#2
print(user_string[0], user_string[len(user_string)-1])

#3

for i in range(1, len(user_string)):
    print(user_string[i] + i)

#4
import random
sr = ''.join(random.sample(user_string, len(user_string)))
print(sr)

