
ask_birthday = int(input("When were you born? :"))

user_age = 2021 - ask_birthday

i = 'i' * (user_age % 10)
cake = '''
   ___'''+ i +'''___
    | :H:a:p:p:y |
 ___|____________|__ 
| ^^^^^^^^^^^^^^^   |
|:B:i:r:t:h:d:d:a:y |
|                   |
~~~~~~~~~~~~~~~~~~~~~
'''
print(cake)



