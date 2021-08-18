# Exercise 7: When Will I Retire ?
from datetime import date, datetime


gender = input('Write your gender (m or f): ')
date_of_birth = datetime.strptime(input("What is your date of birth (yyyy mm dd)? :"), "%Y %m %d")

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
age = calculate_age(date_of_birth)

def can_retire(gender, age):
    if gender == 'm' and age >= 67:
        print('Ok. Tou can retire')
    elif gender == 'f' and age >= 62:
        print('Ok. Tou can retire')
    else:
        print('Sorry, you can\'t retire')

can_retire(gender, age)





    

