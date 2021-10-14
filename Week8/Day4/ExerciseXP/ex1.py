# Exercise 1 : Pets
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

    def sing(self, sounds):
        return f'{sounds}'


class Cat(Pets):
    is_lazy = True

    def __init__(self, animals, name, age: int):
        super().__init__(animals)
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    pass


class Chartreuse(Cat):
    pass


class Manx(Cat):
    pass


cat1 = Bengal('Cat', "Banana", 2)
cat2 = Chartreuse('Cat', 'Monk', 1)
my_cats = [Bengal, Chartreuse, Manx]
my_pets = Pets(my_cats)
print(my_pets.walk())
