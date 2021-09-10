# Exercise 4 : Afternoon At The Zoo
import string


class Zoo:
    def __init__(self, zoo_name: str):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(' already exist')

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        self.animals.remove(animal_sold)
        print(self.animals)

    def sort_animals(self):
        for letter in list(string.ascii_uppercase):
            animals_list = [animal for animal in self.animals if animal.startswith(letter)]
            sorted_list = sorted(animals_list)
            if sorted_list:
                return dict(enumerate(sorted_list))

    # def get_groups(self):
    #     animals = self.sort_animals()
    #     for key, values in animals:
    #         print(f'{key}: {values}') don't know how to solve



zoo1 = Zoo("Moonlight")
zoo1.add_animal('Ape')
zoo1.add_animal('Cat')
zoo1.add_animal('Baboon')
zoo1.add_animal("Bear")
zoo1.add_animal('Eel')
zoo1.add_animal('Cougar')
zoo1.add_animal('Emu')
zoo1.get_animals()

zoo1.sell_animal("Bear")
zoo1.get_animals()
print(zoo1.sort_animals())
zoo1.get_groups()
