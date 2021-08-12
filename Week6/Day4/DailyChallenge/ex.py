
ask_birthday = int(input("When were you born? :"))
user_age = list(str(2021 - ask_birthday))
i = 'i' * int(user_age[-1])
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



