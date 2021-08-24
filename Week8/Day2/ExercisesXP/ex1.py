# Exercise 1: Cats

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat('Big', 3)
cat2 = Cat('Toto', 1)
cat3 = Cat('Manu', 5)

oldest_cat = max(cat1.age, cat2.age, cat3.age)
print(oldest_cat)