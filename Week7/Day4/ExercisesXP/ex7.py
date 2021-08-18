# Exercise 7: When Will I Retire ?
from datetime import date, datetime

date_of_birth = datetime.strptime(input("What is your date of birth (yyyy mm dd)? :"), "%Y %m %d")

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

print(calculate_age(date_of_birth))




    

